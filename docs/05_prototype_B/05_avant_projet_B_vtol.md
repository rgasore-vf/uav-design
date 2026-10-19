# Dossier 05 : Prototype B, VTOL QuadPlane (avant-projet v0.1)

Version 0.1, 19 octobre 2026. Avant-projet (Phase 2), avec la même mission, la même charge utile, la même réserve et les mêmes hypothèses aérodynamiques et propulsives que le prototype A (règle 5 du mandat). Seules les données propres au VTOL diffèrent : rotors, temps de stationnaire, pénalité de traînée.

## 1. Architecture retenue

| Sous-système | Choix | Justification |
|---|---|---|
| Architecture | QuadPlane : 4 rotors de sustentation fixes + 1 moteur de croisière | ADR-001 (Dossier 03 section 2) |
| Cellule | MakeFlyEasy Fighter VTOL : 2430 mm, 72,5 dm², MTOW 11,5 kg, charge utile max 2,5 kg (R18) | Seule cellule VTOL documentée de la classe ; la conversion de la Believer est éliminée par la MTOW |
| Énergie | Li-ion P45B, 6S8P (référence nominale) | Batterie minimale satisfaisant la mission de référence (`selection_batterie.csv`) |
| Autopilote | CUAV X7+ Pro, ArduPilot Plane en mode QuadPlane | ADR-003 ; support natif des transitions (R17) |
| Décollage et atterrissage | Verticaux, sans équipement au sol | Objectif de l'architecture |
| Charge utile, liaison, déclenchement | Identiques au prototype A | Comparaison équitable |

## 2. Bilan de masse préliminaire

| Poste | Masse (g) | Statut |
|---|---|---|
| Cellule + 4 rotors de sustentation + moteur de croisière + 5 ESC + servos + bras + câblage | 3600 (plage 3000 à 4500) | **HYP H07, donnée la plus incertaine du projet** |
| Avionique (identique à A) | 320 | SRC + EST |
| Charge utile dimensionnante | 500 | SRC + EST |
| Batterie 6S8P P45B (48 × 70 g + 10 %) | 3696 | SRC R04 + HYP H10 |
| **Total** | **8116** | Soit 71 % de la MTOW de 11,5 kg |

Il n'y a pas de parachute : la récupération est verticale. C'est un choix discutable du point de vue de la sécurité, puisqu'un parachute de secours couvrirait la perte de sustentation. Je le traiterai dans l'analyse de risques (Dossier 07).

## 3. Performances (cas nominal)

| Grandeur | Valeur | Méthode |
|---|---|---|
| Charge alaire | 112 g/dm² | m/S |
| Vitesse de décrochage (CLmax 1,1, 1260 m, ISA+21) | 14,1 m/s | |
| Vitesse de transit et d'acquisition | 18,3 m/s (borne 1,3 Vs atteinte) | La vitesse optimale serait plus faible, mais elle est limitée par MIS-07 |
| Finesse en croisière (avec ΔCD0 VTOL de 0,006) | 9,7 | |
| Puissance électrique en palier (avec auxiliaires) | 310 W | 2,1 fois celle de A |
| Puissance de stationnaire à 960 m par 30 °C | 1183 W | Théorie de Froude, avec FM 0,68 et η 0,85 |
| Charge de disque | 153 N/m² (4 hélices de 16 pouces) | T/A |
| Puissance en transition (× 1,2) | environ 1420 W, soit 79 A à 18 V | H transition_power_factor |
| Courant par cellule en transition | environ 9,9 A pour 45 A admissibles (R04) | 79 A / 8 |
| Poussée maximale requise par rotor | **4,31 kgf** en équivalent niveau de la mer | m · (T/W 1,8) / 4 / σ, avec σ = 0,848 |

**Contrôle indépendant de la puissance de stationnaire.** Au banc, le T-Motor MN4014 KV330 avec une hélice 16×5,4 à 65 % (1420 g pour 155,4 W, R20) donne un produit FM × η implicite de 0,60, pour une densité de banc supposée de 1,20. Le modèle utilise 0,68 × 0,85 = 0,58. Les deux méthodes concordent à 4 % près.

**Conséquence sur les rotors.** Le MN4014 plafonne vers 1,9 à 2,6 kg de poussée par rotor (R20, valeur incohérente sur la page du constructeur). Il est donc **insuffisant d'un facteur 1,7 à 2,3**. Il faut des rotors de sustentation de la classe 4 à 5 kgf en 6S, avec des hélices de 18 pouces ou plus. Leur masse est incluse dans H07, mais n'est pas vérifiée. La sélection se fera en Phase 3 sur des courbes constructeur à 6S, à la densité du site.

## 4. Bilan énergétique de la mission de référence (2 × 20 km, 30 min d'acquisition, vent de 5 m/s)

| Phase | B, VTOL (Wh) | A, Fixed Wing (Wh), rappel |
|---|---|---|
| Phases VTOL : stationnaire et transitions (120 s × 1,2) | 47,8 | sans objet |
| Contingence verticale (60 s de stationnaire) | 20,0 | sans objet |
| Tour de piste | sans objet | 7,5 |
| Montée à 300 m | 25,9 | 13,4 |
| Transit de 40 km | 203,8 | 113,9 |
| Acquisition, 30 min | 155,2 | 88,6 |
| Descente | 0,4 | 0,4 |
| **Mission** | **453** | **224** |
| **Besoin avec 30 % de réserve** | **648** | **320** |
| Énergie utilisable | 661 (6S8P) | 330 (6S4P) |
| **Marge** | **+13 Wh (2 %)** | **+11 Wh (3 %)** |
| Masse au décollage | 8,12 kg | 4,47 kg |
| Durée de vol | environ 72 min | environ 78 min |

**Le résultat principal de l'avant-projet** est que le surcoût énergétique du VTOL ne vient pas d'abord du stationnaire. Les phases verticales représentent 68 Wh, soit 15 % de l'énergie de mission. L'essentiel de l'écart (environ 2 fois) vient de la croisière : on transporte sur tout le vol environ 1,8 kg de cellule plus grande et de système VTOL de plus que A (3,6 kg contre 1,8 kg avec parachute), plus la batterie supplémentaire que cette masse exige, plus la traînée des bras et des rotors arrêtés. C'est l'effet d'une spirale de masse classique.

Ce résultat dépend fortement de H07 (masse sèche) et de H13 (ΔCD0). La sensibilité est la suivante (`calc/out/sensibilite.csv`) :

| Paramètre | Amplitude |
|---|---|
| Durée d'acquisition | 333 Wh |
| Rendement propulsif | 201 Wh |
| CD0 | 150 Wh |
| Masse sèche | 132 Wh |
| Énergie utilisable | 117 Wh |
| Vent | 115 Wh |
| ΔCD0 VTOL | 68 Wh |
| Temps de stationnaire | 51 Wh |
| Coefficient e | 31 Wh |
| Figure de mérite | 22 Wh |

Le temps de stationnaire et la figure de mérite, souvent mis en avant dans les discussions sur le VTOL, sont parmi les paramètres les **moins** influents pour cette mission.

**Vent.** À 8 m/s, la mission de référence n'est plus tenue en 6S8P (marge de −29 Wh). Avec 15 minutes d'acquisition, elle redevient possible (+82 Wh).

## 5. Transitions et modes dégradés (premier examen)

**Transition avant.** ArduPilot maintient la sustentation des rotors jusqu'à AIRSPEED_MIN, puis réduit leur puissance sur Q_TRANSITION_MS (5000 ms par défaut, R17). Avec AIRSPEED_MIN ≥ 1,3 Vs ≈ 18 m/s à 8,1 kg par temps chaud, la transition est longue, et le moteur de croisière doit accélérer 8,1 kg à 18 m/s pendant que les rotors portent l'appareil. C'est la phase de plus forte puissance totale, et celle où la chute de tension est la plus marquée (R17 cite un seuil de 3,0 V/cellule pour les LiPo). Le Li-ion, plus résistif, doit être vérifié sous ce courant combiné.

**Échec de transition.** Q_TRANS_FAIL vaut 0 par défaut, ce qui désactive le délai d'échec (R17). Pour un prototype, il faut le régler à une valeur non nulle, avec une action définie (Q_TRANS_FAIL_ACT).

**Passage en MANUAL ou ACRO.** Les rotors s'arrêtent immédiatement, d'où un risque de décrochage sous la vitesse de vol (R17). Il faut une procédure et une configuration des modes qui l'empêchent.

| Mode dégradé | Conséquence probable | Parade candidate |
|---|---|---|
| Perte d'un rotor en stationnaire (quad) | Perte de contrôle en lacet et en roulis ; pas de récupération standard | Octo-quad (masse et coût en plus), ou limiter le temps passé en stationnaire au-dessus de 10 m |
| Perte du moteur de croisière | Plané, ou retour en mode Q si l'énergie le permet | Q_ASSIST, avec réserve dédiée à la descente verticale |
| ESC de sustentation défaillant | Équivalent à la perte d'un rotor | Contrôle de température ESC, télémétrie ESC si disponible |
| Capteur de vitesse air incohérent | Transition terminée trop tôt (décrochage) ou jamais (épuisement) | Comparaison avec la vitesse sol et le vent estimé ; Q_TRANS_FAIL |
| Rafale ou vent arrière en transition | Vitesse air insuffisante ; transition prolongée | Transition face au vent obligatoire (procédure) |
| Chute de tension en transition | Brown-out des ESC, perte de poussée | Dimensionnement en courant, BATT_WATT_MAX (R17), essais au banc à état de charge faible |

## 6. Ce que le VTOL apporte et ce qu'il coûte, à quantifier en Phase 4

**Apport.** Aucun équipement de lancement ou de récupération. La surface nécessaire au sol est de l'ordre de 10 × 10 m (estimation) contre environ 100 × 100 m pour le parachute de A (section 5 du Dossier 04). Pas d'impact sur la caméra à l'atterrissage.

**Coût.**
- 1,8 fois la masse au décollage.
- 2,0 fois l'énergie par mission (et donc 2 fois la masse de cellules Li-ion, à environ 48 cellules contre 24).
- 5 moteurs et 5 ESC au lieu de 2.
- Une phase de transition à mettre au point.
- Un mode de panne sans récupération (perte d'un rotor) tant que la configuration reste un quad.

La question opérationnelle décisive est la décision D-04 : **les sites de Virunga offrent-ils, ou non, une surface de 100 × 100 m dégagée pour la catapulte et le parachute ?** Si oui, l'avantage du VTOL se réduit à la commodité. Sinon, il devient une exigence.
