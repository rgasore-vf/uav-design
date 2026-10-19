"""Tests de coherence du modele de dimensionnement (stdlib unittest).

Lancer depuis la racine du depot:  python3 -m unittest discover -s tests -v
Ces tests verifient la physique et la coherence interne, pas la realite:
aucun test ne remplace un essai au banc ou en vol.
"""
import csv
import math
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "calc"))
import model  # noqa: E402

G = 9.80665


class TestAtmosphere(unittest.TestCase):
    def test_isa_sea_level(self):
        self.assertAlmostEqual(model.rho_isa(0), 1.225, places=3)

    def test_density_decreases_with_altitude_and_heat(self):
        self.assertLess(model.rho_isa(1960), model.rho_isa(960))
        self.assertLess(model.rho_isa(960, 21), model.rho_isa(960))


class TestAerodynamics(unittest.TestCase):
    def test_power_matches_lift_to_drag_formulation(self):
        """Controle independant: P = W V / (L/D * eta) a partir de la finesse calculee."""
        m, rho, V, S, b = 4.5, 1.0, 18.0, 0.51, 1.96
        P, CL, LD = model.polar_power(m, rho, V, S, b * b / S, 0.04, 0.78, 0.51)
        self.assertAlmostEqual(P, m * G * V / (LD * 0.51), delta=1e-6)

    def test_stall_speed_scales_with_sqrt_mass(self):
        v1 = model.vstall(4.0, 1.0, 0.5, 1.1)
        v2 = model.vstall(8.0, 1.0, 0.5, 1.1)
        self.assertAlmostEqual(v2 / v1, math.sqrt(2), places=6)


class TestHover(unittest.TestCase):
    def test_momentum_theory_against_bench(self):
        """Banc T-Motor MN4014 16x5.4 (1420 g, 155.4 W): FM*eta implicite ~0.60."""
        T = 1.420 * G
        A = math.pi * (16 * 0.0254 / 2) ** 2
        fm_eta = T ** 1.5 / math.sqrt(2 * 1.20 * A) / 155.4
        self.assertTrue(0.5 < fm_eta < 0.7, fm_eta)

    def test_hover_power_increases_with_altitude(self):
        p_low, _ = model.hover_power(8.0, model.rho_isa(0), 4, 16, 0.68, 0.85)
        p_high, _ = model.hover_power(8.0, model.rho_isa(1960, 21), 4, 16, 0.68, 0.85)
        self.assertGreater(p_high, p_low)


class TestMission(unittest.TestCase):
    def setUp(self):
        self.case = model.case_vals(1)
        self.batt = {b["id"]: b for b in model.BATTS}

    def _fw(self, mapping, wind):
        c = [x for x in model.P["fixed_wing_candidates"] if x["id"] == "Believer-1960"][0]
        m = model.mass_total(c["dry_kg"][1] + c.get("recovery_kg", 0), self.batt["LI-6S4P"])
        return model.mission(m, None, c["S_m2"], c["b_m"], self.case, mapping, wind)

    def test_reserve_applied(self):
        res = self._fw(30, 5)
        self.assertAlmostEqual(res["E_req"], res["E_mission"] / (1 - model.mis["reserve_frac"]), places=6)

    def test_energy_monotonic_in_wind_and_mapping(self):
        self.assertLess(self._fw(30, 0)["E_req"], self._fw(30, 8)["E_req"])
        self.assertLess(self._fw(15, 5)["E_req"], self._fw(45, 5)["E_req"])

    def test_cruise_respects_stall_margin(self):
        res = self._fw(30, 5)
        self.assertGreaterEqual(res["V"], model.AC["min_speed_margin"] * res["Vs"] - 1e-9)


class TestOutputs(unittest.TestCase):
    def test_main_writes_consistent_csv(self):
        with tempfile.TemporaryDirectory() as d:
            model.main(d)
            for name in ["fw_sizing.csv", "vtol_sizing.csv", "selection_batterie.csv",
                         "photogrammetrie.csv", "lancement_recuperation.csv", "sensibilite.csv",
                         "atmosphere.csv", "controles.csv"]:
                path = os.path.join(d, name)
                self.assertTrue(os.path.exists(path), name)
                with open(path, encoding="utf-8") as f:
                    rows = list(csv.reader(f))
                self.assertGreater(len(rows), 1, name)
                self.assertTrue(all(len(r) == len(rows[0]) for r in rows), name)


class TestRegistries(unittest.TestCase):
    def test_csv_registries_are_well_formed(self):
        for rel in ["registres/references.csv", "registres/hypotheses.csv",
                    "registres/decisions.csv", "docs/01_audit/matrice_audit.csv"]:
            with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
                rows = list(csv.reader(f))
            self.assertTrue(all(len(r) == len(rows[0]) for r in rows), rel)


if __name__ == "__main__":
    unittest.main()
