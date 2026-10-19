# Synthese automatique du modele v0.1

Densite croisiere de reference: 1960 m AMSL, ISA+21.0 C -> rho = 0.939 kg/m3
Puissance auxiliaire totale (avec rendement BEC): 15.6 W
Masse avionique: 320 g; charge utile dimensionnante: 516 g (reelle estimee 516 g)

## Batteries

- LI-6S2P: 194 Wh nominal, 165 Wh utilisables, 924 g, 210 Wh/kg pack, Imax 90 A
- LI-6S3P: 292 Wh nominal, 248 Wh utilisables, 1386 g, 210 Wh/kg pack, Imax 135 A
- LI-6S4P: 389 Wh nominal, 330 Wh utilisables, 1848 g, 210 Wh/kg pack, Imax 180 A
- LI-6S5P: 486 Wh nominal, 413 Wh utilisables, 2310 g, 210 Wh/kg pack, Imax 225 A
- LI-6S6P: 583 Wh nominal, 496 Wh utilisables, 2772 g, 210 Wh/kg pack, Imax 270 A
- LI-6S8P: 778 Wh nominal, 661 Wh utilisables, 3696 g, 210 Wh/kg pack, Imax 360 A
- LIPO-6S-16000: 355 Wh nominal, 284 Wh utilisables, 1932 g, 184 Wh/kg pack, Imax 240 A

## Batterie minimale par scenario (vent 5 m/s)

| Type | Cas | Cellule | Cartographie (min) | Batterie | Masse (kg) | Marge (Wh) |
|---|---|---|---|---|---|---|
| FW | optimiste | Moose-patins | 0 | LI-6S2P | 2.76 | 59.0 |
| FW | optimiste | Moose-patins | 15 | LI-6S2P | 2.76 | 27.0 |
| FW | optimiste | Moose-patins | 30 | LI-6S3P | 3.22 | 58.0 |
| FW | optimiste | Moose-patins | 45 | LI-6S3P | 3.22 | 23.0 |
| FW | optimiste | Moose-patins | 60 | LI-6S4P | 3.68 | 43.0 |
| FW | optimiste | Moose-parachute | 0 | LI-6S2P | 2.96 | 53.0 |
| FW | optimiste | Moose-parachute | 15 | LI-6S2P | 2.96 | 20.0 |
| FW | optimiste | Moose-parachute | 30 | LI-6S3P | 3.42 | 49.0 |
| FW | optimiste | Moose-parachute | 45 | LI-6S3P | 3.42 | 13.0 |
| FW | optimiste | Moose-parachute | 60 | LI-6S4P | 3.88 | 31.0 |
| FW | optimiste | Believer-1960 | 0 | LI-6S2P | 3.36 | 42.0 |
| FW | optimiste | Believer-1960 | 15 | LI-6S2P | 3.36 | 2.0 |
| FW | optimiste | Believer-1960 | 30 | LI-6S3P | 3.82 | 28.0 |
| FW | optimiste | Believer-1960 | 45 | LI-6S4P | 4.28 | 48.0 |
| FW | optimiste | Believer-1960 | 60 | LI-6S4P | 4.28 | 3.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 0 | LI-6S3P | 5.22 | 39.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 15 | LI-6S4P | 5.68 | 44.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 30 | LI-6S5P | 6.15 | 43.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 45 | LI-6S6P | 6.61 | 36.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 60 | LI-6S8P | 7.53 | 75.0 |
| VTOL | optimiste | Believer-QuadPlane | 0 | LI-6S3P | 4.82 | 50.0 |
| VTOL | optimiste | Believer-QuadPlane | 15 | LI-6S4P | 5.28 | 60.0 |
| VTOL | optimiste | Believer-QuadPlane | 30 | LI-6S4P | 5.28 | 5.0 |
| VTOL | optimiste | Believer-QuadPlane | 45 | AUCUNE |  |  |
| VTOL | optimiste | Believer-QuadPlane | 60 | AUCUNE |  |  |
| FW | nominal | Moose-patins | 0 | LI-6S2P | 2.96 | 25.0 |
| FW | nominal | Moose-patins | 15 | LI-6S3P | 3.42 | 40.0 |
| FW | nominal | Moose-patins | 30 | LI-6S4P | 3.88 | 42.0 |
| FW | nominal | Moose-patins | 45 | LI-6S5P | 4.35 | 23.0 |
| FW | nominal | Moose-patins | 60 | AUCUNE |  |  |
| FW | nominal | Moose-parachute | 0 | LI-6S2P | 3.16 | 16.0 |
| FW | nominal | Moose-parachute | 15 | LI-6S3P | 3.62 | 30.0 |
| FW | nominal | Moose-parachute | 30 | LI-6S4P | 4.08 | 26.0 |
| FW | nominal | Moose-parachute | 45 | AUCUNE |  |  |
| FW | nominal | Moose-parachute | 60 | AUCUNE |  |  |
| FW | nominal | Believer-1960 | 0 | LI-6S2P | 3.56 | 2.0 |
| FW | nominal | Believer-1960 | 15 | LI-6S3P | 4.02 | 9.0 |
| FW | nominal | Believer-1960 | 30 | LI-6S4P | 4.48 | 8.0 |
| FW | nominal | Believer-1960 | 45 | LI-6S6P | 5.41 | 42.0 |
| FW | nominal | Believer-1960 | 60 | AUCUNE |  |  |
| VTOL | nominal | MFE-Fighter-VTOL | 0 | LI-6S5P | 6.75 | 51.0 |
| VTOL | nominal | MFE-Fighter-VTOL | 15 | LI-6S6P | 7.21 | 9.0 |
| VTOL | nominal | MFE-Fighter-VTOL | 30 | AUCUNE |  |  |
| VTOL | nominal | MFE-Fighter-VTOL | 45 | AUCUNE |  |  |
| VTOL | nominal | MFE-Fighter-VTOL | 60 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 0 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 15 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 30 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 45 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 60 | AUCUNE |  |  |
| FW | pessimiste | Moose-patins | 0 | LI-6S4P | 4.18 | 45.0 |
| FW | pessimiste | Moose-patins | 15 | AUCUNE |  |  |
| FW | pessimiste | Moose-patins | 30 | AUCUNE |  |  |
| FW | pessimiste | Moose-patins | 45 | AUCUNE |  |  |
| FW | pessimiste | Moose-patins | 60 | AUCUNE |  |  |
| FW | pessimiste | Moose-parachute | 0 | LI-6S4P | 4.38 | 32.0 |
| FW | pessimiste | Moose-parachute | 15 | AUCUNE |  |  |
| FW | pessimiste | Moose-parachute | 30 | AUCUNE |  |  |
| FW | pessimiste | Moose-parachute | 45 | AUCUNE |  |  |
| FW | pessimiste | Moose-parachute | 60 | AUCUNE |  |  |
| FW | pessimiste | Believer-1960 | 0 | LI-6S4P | 4.78 | 16.0 |
| FW | pessimiste | Believer-1960 | 15 | AUCUNE |  |  |
| FW | pessimiste | Believer-1960 | 30 | AUCUNE |  |  |
| FW | pessimiste | Believer-1960 | 45 | AUCUNE |  |  |
| FW | pessimiste | Believer-1960 | 60 | AUCUNE |  |  |
| VTOL | pessimiste | MFE-Fighter-VTOL | 0 | AUCUNE |  |  |
| VTOL | pessimiste | MFE-Fighter-VTOL | 15 | AUCUNE |  |  |
| VTOL | pessimiste | MFE-Fighter-VTOL | 30 | AUCUNE |  |  |
| VTOL | pessimiste | MFE-Fighter-VTOL | 45 | AUCUNE |  |  |
| VTOL | pessimiste | MFE-Fighter-VTOL | 60 | AUCUNE |  |  |
| VTOL | pessimiste | Believer-QuadPlane | 0 | AUCUNE |  |  |
| VTOL | pessimiste | Believer-QuadPlane | 15 | AUCUNE |  |  |
| VTOL | pessimiste | Believer-QuadPlane | 30 | AUCUNE |  |  |
| VTOL | pessimiste | Believer-QuadPlane | 45 | AUCUNE |  |  |
| VTOL | pessimiste | Believer-QuadPlane | 60 | AUCUNE |  |  |

## Controles independants

- FM x eta_ME implicite du banc MN4014 16x5.4 (rho banc suppose 1.20): 0.599 (modele nominal 0.68x0.85 = 0.578)
- Believer 4.5 kg, 20 m/s, niveau mer, cas optimiste: Wh/km modele: 2.34 (essai vendeur: 355 Wh x (0.8 a 1.0) / 90 km = 3.2 a 3.9 Wh/km (conditions inconnues))
- Believer 4.5 kg, 20 m/s, niveau mer, cas nominal: Wh/km modele: 3.29 (essai vendeur: 355 Wh x (0.8 a 1.0) / 90 km = 3.2 a 3.9 Wh/km (conditions inconnues))
- Believer 4.5 kg, 20 m/s, niveau mer, cas pessimiste: Wh/km modele: 5.03 (essai vendeur: 355 Wh x (0.8 a 1.0) / 90 km = 3.2 a 3.9 Wh/km (conditions inconnues))
- Energie potentielle 5 kg sur 300 m (Wh), avant rendement: 4.09 (m g h / 3600)
