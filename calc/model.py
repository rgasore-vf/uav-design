#!/usr/bin/env python3
"""
Modele de dimensionnement preliminaire UAV cartographie (Fixed Wing et VTOL QuadPlane).
Version 0.1 du 2026-10-19. Toutes les entrees sont dans params.json avec leur statut
(SRC / HYP / EST). Ce script ne valide rien: il propage des hypotheses explicites.

Usage:  python3 calc/model.py [params.json] [dossier_sortie]
        (ou variable d'environnement UAV_PARAMS pour le fichier de parametres)
Sorties: CSV et summary.md dans calc/out/ par defaut.
Le module peut etre importe sans effet de bord (fonctions de calcul seules).
"""
import csv, json, math, os, sys, itertools

G = 9.80665
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PARAMS = os.path.join(HERE, "params.json")
if os.environ.get("UAV_PARAMS"):
    PFILE = os.environ["UAV_PARAMS"]
elif __name__ == "__main__" and len(sys.argv) > 1:
    PFILE = sys.argv[1]
else:
    PFILE = DEFAULT_PARAMS
OUT = os.path.join(HERE, "out")
with open(PFILE, encoding="utf-8") as _f:
    P = json.load(_f)

def v(x):
    """Valeur d'un champ [valeur, statut] ou valeur brute."""
    return x[0] if isinstance(x, list) and len(x) == 2 and isinstance(x[1], str) else x

# ---------------------------------------------------------------- atmosphere
def rho_isa(h_m, dT=0.0):
    """Densite (kg/m3): pression ISA a l'altitude h, temperature ISA + dT."""
    T_isa = 288.15 - 0.0065 * h_m
    p = 101325.0 * (T_isa / 288.15) ** 5.25588
    return p / (287.05 * (T_isa + dT))

RHO0 = 1.225
site = {k: v(x) for k, x in P["site"].items()}
mis = {k: v(x) for k, x in P["mission"].items()}
H0, HMAX, DT = site["takeoff_elev_m"], site["max_agl_m"], site["hot_day_dT_C"]
H_CRUISE = H0 + mis["cruise_agl_m"]

# ---------------------------------------------------------------- cas aero
AC = {k: v(x) for k, x in P["aero_common"].items()}
CASES = {  # index 0 optimiste, 1 nominal, 2 pessimiste
    "optimiste": 0, "nominal": 1, "pessimiste": 2}
def case_vals(i):
    return dict(CD0=AC["CD0"][i], e=AC["e_oswald"][i], CLmax=AC["CLmax"][i],
                eta=AC["eta_prop"][i] * AC["eta_motor_esc"][i])

aux = {k: v(x) for k, x in P["aux_power_W"].items()}
P_AUX = sum(val for k, val in aux.items() if k != "bec_efficiency") / aux["bec_efficiency"]
M_AVIO = sum(v(x) for x in P["avionics_mass_g"].values()) / 1000.0
pl = {k: v(x) for k, x in P["payload_mass_g"].items()}
M_PAYLOAD_REAL = (pl["ILX-LR1_body"] + pl["lens_Samyang_AF24_F2.8"] + pl["mount_damping_cables"]) / 1000.0
M_PAYLOAD = max(M_PAYLOAD_REAL, pl["allowance_total"] / 1000.0)  # on dimensionne sur l'enveloppe

# ---------------------------------------------------------------- batteries
def batt(b):
    if "pack_Wh" in b:
        Wh, kg, Imax = b["pack_Wh"], b["pack_g"] / 1000.0, b["pack_Acont"]
    else:
        n = b["s"] * b["p"]
        Wh = n * b["cell_Wh"]
        kg = n * b["cell_g"] * (1 + b["overhead"]) / 1000.0
        Imax = b["p"] * b["cell_Amax"]
    return dict(id=b["id"], chem=b["chem"], s=b["s"], p=b["p"], Wh=Wh, kg=kg,
                use_Wh=Wh * b["usable"], Imax=Imax)
BATTS = [batt(b) for b in P["batteries"]]

# ---------------------------------------------------------------- aerodynamique
def polar_power(m, rho, V, S, AR, CD0, e, eta):
    """Puissance electrique de propulsion (W) en palier, polaire parabolique."""
    W = m * G
    q = 0.5 * rho * V * V
    CL = W / (q * S)
    CD = CD0 + CL * CL / (math.pi * e * AR)
    D = q * S * CD
    return D * V / eta, CL, CL / CD

def vstall(m, rho, S, CLmax):
    return math.sqrt(2 * m * G / (rho * S * CLmax))

def best_speed(m, rho, S, AR, CD0, e, eta, vmin, wind=0.0, vmax=35.0):
    """Vitesse air minimisant l'energie du transit aller-retour avec vent w
    (vent de face a l'aller, arriere au retour): E ~ P(V) * (1/(V-w) + 1/(V+w))."""
    best = None
    V = max(vmin, wind + 3.0)
    while V <= vmax:
        Pp, CL, LD = polar_power(m, rho, V, S, AR, CD0, e, eta)
        epk = (Pp + P_AUX) * (1 / (V - wind) + 1 / (V + wind))
        if best is None or epk < best[0]:
            best = (epk, V)
        V += 0.1
    return best[1]

# ---------------------------------------------------------------- VTOL stationnaire
VT = {k: v(x) for k, x in P["vtol"].items()}
def hover_power(m, rho, n, prop_in, FM, eta):
    A = n * math.pi * (prop_in * 0.0254 / 2) ** 2
    T = m * G
    return T ** 1.5 / math.sqrt(2 * rho * A) / (FM * eta), T / A

# ---------------------------------------------------------------- mission
def mission(m, ac, S, b, case, map_min, wind, vtol=None, V_fixed=None):
    """Retourne dict energie (Wh) par phase et grandeurs de vol."""
    AR = b * b / S
    CD0 = case["CD0"] + (vtol["dCD0"] if vtol else 0.0)
    rho_c = rho_isa(H_CRUISE, DT)
    vs = vstall(m, rho_c, S, case["CLmax"])
    vmin = AC["min_speed_margin"] * vs
    V = V_fixed if V_fixed else best_speed(m, rho_c, S, AR, CD0, case["e"], case["eta"], vmin, wind)
    V = max(V, vmin)
    Vm = max(vmin, mis["mapping_airspeed_ms"])
    Pp, CL, LD = polar_power(m, rho_c, V, S, AR, CD0, case["e"], case["eta"])
    Pl = Pp + P_AUX
    Pm = polar_power(m, rho_c, Vm, S, AR, CD0, case["e"], case["eta"])[0] + P_AUX
    out = dict(V=V, Vm=Vm, Vs=vs, CL=CL, LD=LD, P_level=Pl, P_map=Pm)
    if V <= wind + 2:
        out["E_req"] = float("inf"); return out
    h = mis["cruise_agl_m"]
    t_climb = h / mis["climb_rate_ms"]
    E = {}
    E["montee"] = (Pl + m * G * mis["climb_rate_ms"] / case["eta"]) * t_climb / 3600
    D = mis["transit_one_way_km"] * 1000
    t_tr = D / (V - wind) + D / (V + wind)
    E["transit"] = Pl * t_tr / 3600
    E["cartographie"] = Pm * map_min * 60 / 3600
    E["descente"] = P_AUX * (h / mis["descent_rate_ms"]) / 3600
    if vtol:
        rho_s = rho_isa(H0, DT)
        Ph, DL = hover_power(m, rho_s, vtol["n"], vtol["prop_in"], vtol["FM"], vtol["eta_h"])
        E["vtol_stationnaire"] = (Ph * VT["transition_power_factor"] + P_AUX) * vtol["t_hover"] / 3600
        E["vtol_contingence"] = (Ph + P_AUX) * VT["contingency_hover_s"] / 3600
        out.update(P_hover=Ph, disk_loading=DL)
    else:
        E["tour_de_piste"] = Pl * mis["pattern_landing_s"] / 3600
    tot = sum(E.values())
    out.update(E=E, E_mission=tot, E_req=tot / (1 - mis["reserve_frac"]),
               t_total_min=(t_climb + t_tr + map_min * 60) / 60)
    return out

def mass_total(dry, bt):
    return dry + M_AVIO + M_PAYLOAD + bt["kg"]


# ---------------------------------------------------------------- etude endurance (temps de vol cible)
def size_for_flight_time(af, cell, aero, target_min, wind, case_index=1, max_cells=240):
    """Plus petite batterie 6S (pas de 6 cellules) tenant `target_min` de vol
    avec la reserve, sous la MTOW. L'acquisition remplit le temps restant
    apres montee, transit aller-retour et approche."""
    case = case_vals(case_index)
    case["CD0"] = max(0.01, case["CD0"] + aero["CD0_offset"])
    case["eta"] = aero["eta"]
    vt = None
    if af["type"] == "VTOL":
        vt = dict(n=4, prop_in=af["prop_in"], dCD0=af["dCD0"], FM=VT["figure_of_merit"][case_index],
                  eta_h=VT["eta_motor_esc_hover"][case_index], t_hover=VT["hover_s_per_sortie"][case_index])
    for n in range(6, max_cells + 1, 6):
        bt = dict(id=f"6S{n // 6}P {cell['id']}", s=6, p=n // 6, Wh=n * cell["Wh"],
                  kg=n * cell["g"] * (1 + cell["overhead"]) / 1000.0)
        bt["use_Wh"] = bt["Wh"] * cell["usable"]
        m = mass_total(af["dry_kg"], bt)
        if af["mtow_kg"] and m > af["mtow_kg"]:
            return None
        r0 = mission(m, AC, af["S_m2"], af["b_m"], case, 0, wind, vtol=vt)
        if not math.isfinite(r0["E_req"]):
            continue
        overhead_min = (mis["pattern_landing_s"] / 60) if vt is None else (VT["hover_s_per_sortie"][case_index] / 60)
        t_map = max(0.0, target_min - r0["t_total_min"] - overhead_min)
        r = mission(m, AC, af["S_m2"], af["b_m"], case, t_map, wind, vtol=vt)
        if bt["use_Wh"] >= r["E_req"]:
            return dict(batterie=bt["id"], cellules=n, masse_kg=m, batt_kg=bt["kg"], Wh_nominal=bt["Wh"],
                        E_req_Wh=r["E_req"], marge_Wh=bt["use_Wh"] - r["E_req"], P_palier_W=r["P_level"],
                        V_transit_ms=r["V"], acquisition_min=t_map, finesse=r["LD"])
    return None

# ---------------------------------------------------------------- balayage
def write_csv(name, rows):
    if not rows: return
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def r(x, n=1):
    return round(x, n) if isinstance(x, (int, float)) and math.isfinite(x) else x

def main(out_dir=None, verbose=False):
    """Execute tous les balayages et ecrit les sorties dans out_dir."""
    global OUT
    OUT = out_dir or OUT
    os.makedirs(OUT, exist_ok=True)
    rows_fw, rows_vt, sel = [], [], []
    maps, winds = mis["mapping_min"], mis["wind_ms"]
    for cname, ci in CASES.items():
        case = case_vals(ci)
        # Fixed wing
        for c in P["fixed_wing_candidates"]:
            dry = c["dry_kg"][ci] + c.get("recovery_kg", 0.0)
            for mp, w in itertools.product(maps, winds):
                best = None
                for bt in BATTS:
                    m = mass_total(dry, bt)
                    res = mission(m, AC, c["S_m2"], c["b_m"], case, mp, w)
                    margin = bt["use_Wh"] - res["E_req"]
                    mt_ok = (c["mtow_kg"] is None) or (m <= c["mtow_kg"])
                    row = dict(cas=cname, cellule=c["id"], batterie=bt["id"], cartographie_min=mp, vent_ms=w,
                               masse_kg=r(m, 2), mtow_kg=c["mtow_kg"], charge_alaire_g_dm2=r(m * 1000 / (c["S_m2"] * 100), 0),
                               Vs_ms=r(res["Vs"]), V_transit_ms=r(res["V"]), V_carto_ms=r(res["Vm"]), finesse_transit=r(res.get("LD", 0)),
                               P_palier_W=r(res["P_level"], 0), E_mission_Wh=r(res.get("E_mission", float("inf")), 0),
                               E_req_reserve_Wh=r(res["E_req"], 0), E_util_batt_Wh=r(bt["use_Wh"], 0),
                               marge_Wh=r(margin, 0), MTOW_ok=mt_ok, energie_ok=margin >= 0)
                    rows_fw.append(row)
                    if mt_ok and margin >= 0 and (best is None or bt["kg"] < best[1]["kg"]):
                        best = (row, bt)
                sel.append(dict(type="FW", cas=cname, cellule=c["id"], cartographie_min=mp, vent_ms=w,
                                batterie_min=best[0]["batterie"] if best else "AUCUNE",
                                masse_kg=best[0]["masse_kg"] if best else "",
                                marge_Wh=best[0]["marge_Wh"] if best else ""))
        # VTOL
        for c in P["vtol_candidates"]:
            dry = c["dry_kg"][ci]
            vt = dict(n=c["n_lift"], prop_in=c["prop_in"], dCD0=c["dCD0_vtol"][ci],
                      FM=VT["figure_of_merit"][ci], eta_h=VT["eta_motor_esc_hover"][ci],
                      t_hover=VT["hover_s_per_sortie"][ci])
            for mp, w in itertools.product(maps, winds):
                best = None
                for bt in BATTS:
                    m = mass_total(dry, bt)
                    res = mission(m, AC, c["S_m2"], c["b_m"], case, mp, w, vtol=vt)
                    margin = bt["use_Wh"] - res["E_req"]
                    mt_ok = m <= c["mtow_kg"]
                    I_hover = res.get("P_hover", 0) * VT["transition_power_factor"] / (3.0 * bt["s"])
                    i_ok = I_hover <= bt["Imax"]
                    rho_s = rho_isa(H0, DT)
                    T_req_motor_kgf_SL = m * VT["twr_lift_required"] / c["n_lift"] / (rho_s / RHO0)
                    row = dict(cas=cname, cellule=c["id"], batterie=bt["id"], cartographie_min=mp, vent_ms=w,
                               masse_kg=r(m, 2), mtow_kg=c["mtow_kg"], Vs_ms=r(res["Vs"]), V_transit_ms=r(res["V"]),
                               V_carto_ms=r(res["Vm"]), finesse_transit=r(res.get("LD", 0)), P_palier_W=r(res["P_level"], 0),
                               P_stationnaire_W=r(res.get("P_hover", 0), 0),
                               charge_disque_N_m2=r(res.get("disk_loading", 0), 0),
                               I_transition_A=r(I_hover, 0), I_batt_max_A=bt["Imax"],
                               poussee_moteur_requise_kgf_niveau_mer=r(T_req_motor_kgf_SL, 2),
                               E_vtol_Wh=r(res["E"].get("vtol_stationnaire", 0) + res["E"].get("vtol_contingence", 0), 0) if "E" in res else "",
                               E_req_reserve_Wh=r(res["E_req"], 0), E_util_batt_Wh=r(bt["use_Wh"], 0),
                               marge_Wh=r(margin, 0), MTOW_ok=mt_ok, courant_ok=i_ok, energie_ok=margin >= 0)
                    rows_vt.append(row)
                    if mt_ok and i_ok and margin >= 0 and (best is None or bt["kg"] < best[1]["kg"]):
                        best = (row, bt)
                sel.append(dict(type="VTOL", cas=cname, cellule=c["id"], cartographie_min=mp, vent_ms=w,
                                batterie_min=best[0]["batterie"] if best else "AUCUNE",
                                masse_kg=best[0]["masse_kg"] if best else "",
                                marge_Wh=best[0]["marge_Wh"] if best else ""))

    write_csv("fw_sizing.csv", rows_fw)
    write_csv("vtol_sizing.csv", rows_vt)
    write_csv("selection_batterie.csv", sel)

    # ---------------------------------------------------------------- atmosphere
    atm = []
    for h in [0, H0, H_CRUISE, H0 + HMAX]:
        for dT in [0, DT]:
            rho = rho_isa(h, dT)
            atm.append(dict(altitude_m=h, dT_C=dT, rho=r(rho, 3), sigma=r(rho / RHO0, 3),
                            facteur_Vs=r(math.sqrt(RHO0 / rho), 3)))
    write_csv("atmosphere.csv", atm)

    # ---------------------------------------------------------------- photogrammetrie
    cam = {k: v(x) for k, x in P["camera"].items()}
    pitch_mm = cam["sensor_w_mm"] / cam["px_w"]
    pg = []
    for f in cam["focal_mm"]:
        for mode, of, os_ in [("ortho", cam["overlap_fwd"][0], cam["overlap_side"][0]),
                              ("3D", cam["overlap_fwd"][1], cam["overlap_side"][1])]:
            for H in [100, 150, 200, 300]:
                gsd = pitch_mm * H / f  # m/px car pitch en mm et f en mm
                Wf = gsd * cam["px_w"]; Lf = gsd * cam["px_h"]
                bfwd = Lf * (1 - of); line = Wf * (1 - os_)
                Vmax_trig = bfwd / cam["min_trigger_interval_s"]
                for V in [18, 20, 22]:
                    pg.append(dict(focale_mm=f, mode=mode, H_agl_m=H, GSD_cm=r(gsd * 100, 2),
                                   empreinte_trav_m=r(Wf, 0), empreinte_long_m=r(Lf, 0),
                                   base_m=r(bfwd, 1), interligne_m=r(line, 1), V_sol_ms=V,
                                   intervalle_s=r(bfwd / V, 2), V_max_declenchement_ms=r(Vmax_trig, 1),
                                   flou_px_1_2000=r(V * cam["exposure_s"][0] / gsd, 2),
                                   flou_px_1_1000=r(V * cam["exposure_s"][1] / gsd, 2),
                                   km2_par_h=r(V * line * cam["turn_efficiency"] * 3600 / 1e6, 2),
                                   images_par_km2=r(1e6 / (bfwd * line), 0),
                                   Go_RAW_par_km2_brut=r(1e6 / (bfwd * line) * cam["px_w"] * cam["px_h"] * cam["raw_bits"] / 8 / 1e9, 1)))
    write_csv("photogrammetrie.csv", pg)

    # ---------------------------------------------------------------- lancement / recuperation
    LR = {k: v(x) for k, x in P["launch_recovery"].items()}
    lr = []
    rho_s = rho_isa(H0, DT)
    for c in P["fixed_wing_candidates"]:
        for ci_name, ci in CASES.items():
            case = case_vals(ci)
            m = mass_total(c["dry_kg"][1] + c.get("recovery_kg", 0.0), [b for b in BATTS if b["id"] == "LI-6S4P"][0])
            vs = vstall(m, rho_s, c["S_m2"], case["CLmax"])
            vl = LR["launch_speed_factor"] * vs
            for L in LR["catapult_stroke_m"]:
                a = vl * vl / (2 * L)
                lr.append(dict(cellule=c["id"], cas_CLmax=ci_name, CLmax=case["CLmax"], masse_kg=r(m, 2),
                               Vs_site_chaud_ms=r(vs), V_lancement_ms=r(vl), course_m=L,
                               accel_moy_g=r(a / G, 1), accel_pic_g=r(a * LR["peak_to_mean_accel"] / G, 1),
                               force_pic_N=r(m * a * LR["peak_to_mean_accel"], 0),
                               energie_lancement_J=r(0.5 * m * vl * vl, 0),
                               Ec_atterr_ventre_J=r(0.5 * m * (LR["belly_landing_speed_factor"] * vs) ** 2, 0),
                               Ec_parachute_5ms_J=r(0.5 * m * 25, 0)))
    write_csv("lancement_recuperation.csv", lr)

    # ---------------------------------------------------------------- sensibilite (un facteur a la fois)
    def ref_fw(over=None):
        over = over or {}
        c = [x for x in P["fixed_wing_candidates"] if x["id"] == "Believer-1960"][0]
        case = case_vals(1); case.update({k: over[k] for k in ("CD0", "e", "eta", "CLmax") if k in over})
        bt = dict([b for b in BATTS if b["id"] == over.get("batt", "LI-6S4P")][0])
        if "usable" in over: bt["use_Wh"] = bt["Wh"] * over["usable"]
        dry = over.get("dry", c["dry_kg"][1]) + c.get("recovery_kg", 0.0)
        m = mass_total(dry, bt)
        res = mission(m, AC, c["S_m2"], c["b_m"], case, over.get("map", 30), over.get("wind", 5))
        return bt["use_Wh"] - res["E_req"], m

    def ref_vt(over=None):
        over = over or {}
        c = [x for x in P["vtol_candidates"] if x["id"] == "MFE-Fighter-VTOL"][0]
        case = case_vals(1); case.update({k: over[k] for k in ("CD0", "e", "eta") if k in over})
        bt = dict([b for b in BATTS if b["id"] == over.get("batt", "LI-6S8P")][0])
        if "usable" in over: bt["use_Wh"] = bt["Wh"] * over["usable"]
        vt = dict(n=4, prop_in=c["prop_in"], dCD0=over.get("dCD0", c["dCD0_vtol"][1]),
                  FM=over.get("FM", VT["figure_of_merit"][1]), eta_h=VT["eta_motor_esc_hover"][1],
                  t_hover=over.get("t_hover", VT["hover_s_per_sortie"][1]))
        m = mass_total(over.get("dry", c["dry_kg"][1]), bt)
        res = mission(m, AC, c["S_m2"], c["b_m"], case, over.get("map", 30), over.get("wind", 5), vtol=vt)
        return bt["use_Wh"] - res["E_req"], m

    sens = []
    eta_n = AC["eta_prop"][1] * AC["eta_motor_esc"][1]
    fw_tests = [("CD0", 0.030, 0.050), ("e", 0.85, 0.70), ("eta", AC["eta_prop"][0] * AC["eta_motor_esc"][0], AC["eta_prop"][2] * AC["eta_motor_esc"][2]),
                ("dry", 1.4, 1.9), ("usable", 0.90, 0.75), ("wind", 0, 10), ("map", 15, 60)]
    base_fw, m_fw = ref_fw()
    for k, lo, hi in fw_tests:
        a, _ = ref_fw({k: lo}); b_, _ = ref_fw({k: hi})
        sens.append(dict(prototype="A Believer FW / LI-6S4P", parametre=k, bas=r(lo, 3), haut=r(hi, 3),
                         marge_ref_Wh=r(base_fw, 0), marge_bas_Wh=r(a, 0), marge_haut_Wh=r(b_, 0),
                         amplitude_Wh=r(abs(a - b_), 0)))
    vt_tests = fw_tests[:3] + [("dry", 3.0, 4.5), ("usable", 0.90, 0.75), ("wind", 0, 10), ("map", 15, 60),
                               ("FM", 0.75, 0.60), ("t_hover", 90, 180), ("dCD0", 0.003, 0.012)]
    base_vt, m_vt = ref_vt()
    for k, lo, hi in vt_tests:
        a, _ = ref_vt({k: lo}); b_, _ = ref_vt({k: hi})
        sens.append(dict(prototype="B Fighter VTOL / LI-6S8P", parametre=k, bas=r(lo, 3), haut=r(hi, 3),
                         marge_ref_Wh=r(base_vt, 0), marge_bas_Wh=r(a, 0), marge_haut_Wh=r(b_, 0),
                         amplitude_Wh=r(abs(a - b_), 0)))
    sens.sort(key=lambda d: (d["prototype"], -d["amplitude_Wh"]))
    write_csv("sensibilite.csv", sens)

    # ---------------------------------------------------------------- controles independants
    checks = []
    # 1. Stationnaire: theorie de Froude vs banc T-Motor MN4014 KV330 16x5.4 a 65 % (1420 g, 155.4 W)
    T = 1.420 * G; A = math.pi * (16 * 0.0254 / 2) ** 2
    P_id = T ** 1.5 / math.sqrt(2 * 1.20 * A)
    checks.append(dict(controle="FM x eta_ME implicite du banc MN4014 16x5.4 (rho banc suppose 1.20)",
                       valeur=r(P_id / 155.4, 3),
                       reference=f"modele nominal {VT['figure_of_merit'][1]}x{VT['eta_motor_esc_hover'][1]} = {r(VT['figure_of_merit'][1]*VT['eta_motor_esc_hover'][1],3)}"))
    # 2. Consommation specifique Believer vs essai vendeur (~90 km avec LiPo 6S 16000 mAh, ~4.5 kg)
    c = [x for x in P["fixed_wing_candidates"] if x["id"] == "Believer-1960"][0]
    for nm, ci in CASES.items():
        cs = case_vals(ci)
        rho = rho_isa(0, 15)  # essai vendeur: conditions non publiees, on suppose ~niveau mer
        AR = c["b_m"] ** 2 / c["S_m2"]
        Pp, CL, LD = polar_power(4.5, rho, 20, c["S_m2"], AR, cs["CD0"], cs["e"], cs["eta"])
        whkm = (Pp + P_AUX) / 20 / 3.6
        checks.append(dict(controle=f"Believer 4.5 kg, 20 m/s, niveau mer, cas {nm}: Wh/km modele",
                           valeur=r(whkm, 2),
                           reference="essai vendeur: 355 Wh x (0.8 a 1.0) / 90 km = 3.2 a 3.9 Wh/km (conditions inconnues)"))
    # 3. Conservation: energie de montee potentielle vs calcul
    m = 5.0; dh = 300
    checks.append(dict(controle="Energie potentielle 5 kg sur 300 m (Wh), avant rendement",
                       valeur=r(m * G * dh / 3600, 2), reference="m g h / 3600"))
    write_csv("controles.csv", checks)


    # ------------------------------------------------------------ etude endurance 2 h
    ES = P.get("endurance_study")
    end_rows = []
    if ES and mis.get("target_flight_min"):
        for af in ES["airframes"]:
            for aero in ES["aero_variants"]:
                for cell in ES["cells"]:
                    for w in (0, 5, 8):
                        s_ = size_for_flight_time(af, cell, aero, mis["target_flight_min"], w)
                        end_rows.append(dict(cellule=af["id"], type=af["type"], aero=aero["id"], cellule_batterie=cell["id"],
                                             vent_ms=w, faisable=bool(s_),
                                             batterie=s_["batterie"] if s_ else "AUCUNE",
                                             masse_kg=r(s_["masse_kg"], 2) if s_ else "", mtow_kg=af["mtow_kg"],
                                             batt_kg=r(s_["batt_kg"], 2) if s_ else "", Wh_nominal=r(s_["Wh_nominal"], 0) if s_ else "",
                                             P_palier_W=r(s_["P_palier_W"], 0) if s_ else "", finesse=r(s_["finesse"], 1) if s_ else "",
                                             acquisition_min=r(s_["acquisition_min"], 0) if s_ else "",
                                             marge_Wh=r(s_["marge_Wh"], 0) if s_ else ""))
        write_csv("endurance_2h.csv", end_rows)
    # ---------------------------------------------------------------- synthese
    def pick(rows, **kw):
        return [x for x in rows if all(x[k] == val for k, val in kw.items())]

    lines = ["# Synthese automatique du modele v0.1", "",
             f"Densite croisiere de reference: {H_CRUISE} m AMSL, ISA+{DT} C -> rho = {rho_isa(H_CRUISE, DT):.3f} kg/m3",
             f"Puissance auxiliaire totale (avec rendement BEC): {P_AUX:.1f} W",
             f"Masse avionique: {M_AVIO*1000:.0f} g; charge utile dimensionnante: {M_PAYLOAD*1000:.0f} g (reelle estimee {M_PAYLOAD_REAL*1000:.0f} g)",
             "", "## Batteries", ""]
    for b in BATTS:
        lines.append(f"- {b['id']}: {b['Wh']:.0f} Wh nominal, {b['use_Wh']:.0f} Wh utilisables, {b['kg']*1000:.0f} g, {b['Wh']/b['kg']:.0f} Wh/kg pack, Imax {b['Imax']} A")
    lines += ["", "## Batterie minimale par scenario (vent 5 m/s)", "",
              "| Type | Cas | Cellule | Cartographie (min) | Batterie | Masse (kg) | Marge (Wh) |", "|---|---|---|---|---|---|---|"]
    for s in sel:
        if s["vent_ms"] == 5:
            lines.append(f"| {s['type']} | {s['cas']} | {s['cellule']} | {s['cartographie_min']} | {s['batterie_min']} | {s['masse_kg']} | {s['marge_Wh']} |")
    if end_rows:
        lines += ["", f"## Etude endurance: {mis['target_flight_min']} min de vol + {int(mis['reserve_frac']*100)} % de reserve (vent 5 m/s)", "",
                  "| Cellule | Aero | Cellules batterie | Batterie | Masse (kg) | Wh nominal | P palier (W) | Acquisition (min) |", "|---|---|---|---|---|---|---|---|"]
        for e in end_rows:
            if e["vent_ms"] == 5:
                lines.append(f"| {e['cellule']} | {e['aero']} | {e['cellule_batterie']} | {e['batterie']} | {e['masse_kg']} | {e['Wh_nominal']} | {e['P_palier_W']} | {e['acquisition_min']} |")
    lines += ["", "## Controles independants", ""]
    for ck in checks:
        lines.append(f"- {ck['controle']}: {ck['valeur']} ({ck['reference']})")
    open(os.path.join(OUT, "summary.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    if verbose:
        print("\n".join(lines))
    return dict(rows_fw=rows_fw, rows_vt=rows_vt, selection=sel, sensibilite=sens, controles=checks, endurance=end_rows)


if __name__ == "__main__":
    main(sys.argv[2] if len(sys.argv) > 2 else None, verbose=True)
