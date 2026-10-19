# Synthese automatique du modele v0.1

Densite croisiere de reference: 1260 m AMSL, ISA+21.0 C -> rho = 1.008 kg/m3
Puissance auxiliaire totale (avec rendement BEC): 15.6 W
Masse avionique: 320 g; charge utile dimensionnante: 500 g (reelle estimee 436 g)

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
| FW | optimiste | Believer-1960 | 0 | LI-6S2P | 3.34 | 45.0 |
| FW | optimiste | Believer-1960 | 15 | LI-6S2P | 3.34 | 4.0 |
| FW | optimiste | Believer-1960 | 30 | LI-6S3P | 3.81 | 31.0 |
| FW | optimiste | Believer-1960 | 45 | LI-6S4P | 4.27 | 52.0 |
| FW | optimiste | Believer-1960 | 60 | LI-6S4P | 4.27 | 7.0 |
| FW | optimiste | Flightory-Moose | 0 | LI-6S2P | 2.94 | 58.0 |
| FW | optimiste | Flightory-Moose | 15 | LI-6S2P | 2.94 | 24.0 |
| FW | optimiste | Flightory-Moose | 30 | LI-6S3P | 3.41 | 55.0 |
| FW | optimiste | Flightory-Moose | 45 | LI-6S3P | 3.41 | 18.0 |
| FW | optimiste | Flightory-Moose | 60 | LI-6S4P | 3.87 | 39.0 |
| FW | optimiste | Skywalker-X8 | 0 | LI-6S2P | 3.44 | 21.0 |
| FW | optimiste | Skywalker-X8 | 15 | LI-6S3P | 3.91 | 33.0 |
| FW | optimiste | Skywalker-X8 | 30 | LI-6S4P | 4.37 | 41.0 |
| FW | optimiste | Skywalker-X8 | 45 | LI-6S5P | 4.83 | 44.0 |
| FW | optimiste | Skywalker-X8 | 60 | LI-6S6P | 5.29 | 40.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 0 | LI-6S3P | 5.21 | 45.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 15 | LI-6S4P | 5.67 | 49.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 30 | LI-6S5P | 6.13 | 48.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 45 | LI-6S6P | 6.59 | 42.0 |
| VTOL | optimiste | MFE-Fighter-VTOL | 60 | LI-6S8P | 7.52 | 85.0 |
| VTOL | optimiste | Believer-QuadPlane | 0 | LI-6S3P | 4.81 | 58.0 |
| VTOL | optimiste | Believer-QuadPlane | 15 | LI-6S3P | 4.81 | 6.0 |
| VTOL | optimiste | Believer-QuadPlane | 30 | LI-6S4P | 5.27 | 14.0 |
| VTOL | optimiste | Believer-QuadPlane | 45 | AUCUNE |  |  |
| VTOL | optimiste | Believer-QuadPlane | 60 | AUCUNE |  |  |
| FW | nominal | Believer-1960 | 0 | LI-6S2P | 3.54 | 4.0 |
| FW | nominal | Believer-1960 | 15 | LI-6S3P | 4.01 | 10.0 |
| FW | nominal | Believer-1960 | 30 | LI-6S4P | 4.47 | 11.0 |
| FW | nominal | Believer-1960 | 45 | LI-6S5P | 4.93 | 3.0 |
| FW | nominal | Believer-1960 | 60 | AUCUNE |  |  |
| FW | nominal | Flightory-Moose | 0 | LI-6S2P | 3.14 | 20.0 |
| FW | nominal | Flightory-Moose | 15 | LI-6S3P | 3.61 | 35.0 |
| FW | nominal | Flightory-Moose | 30 | LI-6S4P | 4.07 | 39.0 |
| FW | nominal | Flightory-Moose | 45 | AUCUNE |  |  |
| FW | nominal | Flightory-Moose | 60 | AUCUNE |  |  |
| FW | nominal | Skywalker-X8 | 0 | LI-6S3P | 4.21 | 32.0 |
| FW | nominal | Skywalker-X8 | 15 | LI-6S4P | 4.67 | 11.0 |
| FW | nominal | Skywalker-X8 | 30 | LI-6S6P | 5.59 | 43.0 |
| FW | nominal | Skywalker-X8 | 45 | LI-6S8P | 6.52 | 57.0 |
| FW | nominal | Skywalker-X8 | 60 | AUCUNE |  |  |
| VTOL | nominal | MFE-Fighter-VTOL | 0 | LI-6S4P | 6.27 | 1.0 |
| VTOL | nominal | MFE-Fighter-VTOL | 15 | LI-6S6P | 7.19 | 18.0 |
| VTOL | nominal | MFE-Fighter-VTOL | 30 | LI-6S8P | 8.12 | 13.0 |
| VTOL | nominal | MFE-Fighter-VTOL | 45 | AUCUNE |  |  |
| VTOL | nominal | MFE-Fighter-VTOL | 60 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 0 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 15 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 30 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 45 | AUCUNE |  |  |
| VTOL | nominal | Believer-QuadPlane | 60 | AUCUNE |  |  |
| FW | pessimiste | Believer-1960 | 0 | LI-6S4P | 4.77 | 23.0 |
| FW | pessimiste | Believer-1960 | 15 | AUCUNE |  |  |
| FW | pessimiste | Believer-1960 | 30 | AUCUNE |  |  |
| FW | pessimiste | Believer-1960 | 45 | AUCUNE |  |  |
| FW | pessimiste | Believer-1960 | 60 | AUCUNE |  |  |
| FW | pessimiste | Flightory-Moose | 0 | LI-6S4P | 4.37 | 45.0 |
| FW | pessimiste | Flightory-Moose | 15 | AUCUNE |  |  |
| FW | pessimiste | Flightory-Moose | 30 | AUCUNE |  |  |
| FW | pessimiste | Flightory-Moose | 45 | AUCUNE |  |  |
| FW | pessimiste | Flightory-Moose | 60 | AUCUNE |  |  |
| FW | pessimiste | Skywalker-X8 | 0 | LI-6S5P | 5.43 | 27.0 |
| FW | pessimiste | Skywalker-X8 | 15 | LI-6S8P | 6.82 | 33.0 |
| FW | pessimiste | Skywalker-X8 | 30 | AUCUNE |  |  |
| FW | pessimiste | Skywalker-X8 | 45 | AUCUNE |  |  |
| FW | pessimiste | Skywalker-X8 | 60 | AUCUNE |  |  |
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

## Etude endurance: 120 min de vol + 30 % de reserve (vent 5 m/s)

| Cellule | Aero | Cellules batterie | Batterie | Masse (kg) | Wh nominal | P palier (W) | Acquisition (min) |
|---|---|---|---|---|---|---|---|
| Believer-1960 | nominal | P45B | AUCUNE |  |  |  |  |
| Believer-1960 | nominal | P50B | AUCUNE |  |  |  |  |
| Believer-1960 | nominal | SEMI-SOLIDE-350 | 6S3P SEMI-SOLIDE-350 | 4.92 | 720.0 | 171.0 | 72.0 |
| Believer-1960 | cellule propre | P45B | 6S6P P45B | 5.39 | 583.0 | 167.0 | 74.0 |
| Believer-1960 | cellule propre | P50B | 6S5P P50B | 4.9 | 540.0 | 148.0 | 72.0 |
| Believer-1960 | cellule propre | SEMI-SOLIDE-350 | 6S2P SEMI-SOLIDE-350 | 4.15 | 480.0 | 121.0 | 69.0 |
| Believer-1960 | cellule propre + helice optimisee | P45B | 6S5P P45B | 4.93 | 486.0 | 136.0 | 72.0 |
| Believer-1960 | cellule propre + helice optimisee | P50B | 6S5P P50B | 4.9 | 540.0 | 134.0 | 72.0 |
| Believer-1960 | cellule propre + helice optimisee | SEMI-SOLIDE-350 | 6S2P SEMI-SOLIDE-350 | 4.15 | 480.0 | 111.0 | 69.0 |
| Classe-FW-2.6m | nominal | P45B | 6S10P P45B | 7.84 | 972.0 | 255.0 | 72.0 |
| Classe-FW-2.6m | nominal | P50B | 6S8P P50B | 6.86 | 864.0 | 212.0 | 68.0 |
| Classe-FW-2.6m | nominal | SEMI-SOLIDE-350 | 6S3P SEMI-SOLIDE-350 | 5.52 | 720.0 | 157.0 | 62.0 |
| Classe-FW-2.6m | cellule propre | P45B | 6S7P P45B | 6.45 | 680.0 | 165.0 | 67.0 |
| Classe-FW-2.6m | cellule propre | P50B | 6S6P P50B | 5.95 | 648.0 | 149.0 | 65.0 |
| Classe-FW-2.6m | cellule propre | SEMI-SOLIDE-350 | 6S3P SEMI-SOLIDE-350 | 5.52 | 720.0 | 136.0 | 63.0 |
| Classe-FW-2.6m | cellule propre + helice optimisee | P45B | 6S6P P45B | 5.99 | 583.0 | 136.0 | 65.0 |
| Classe-FW-2.6m | cellule propre + helice optimisee | P50B | 6S5P P50B | 5.5 | 540.0 | 124.0 | 63.0 |
| Classe-FW-2.6m | cellule propre + helice optimisee | SEMI-SOLIDE-350 | 6S2P SEMI-SOLIDE-350 | 4.75 | 480.0 | 105.0 | 59.0 |
| Classe-FW-3.0m | nominal | P45B | 6S9P P45B | 7.78 | 875.0 | 230.0 | 70.0 |
| Classe-FW-3.0m | nominal | P50B | 6S8P P50B | 7.26 | 864.0 | 209.0 | 68.0 |
| Classe-FW-3.0m | nominal | SEMI-SOLIDE-350 | 6S3P SEMI-SOLIDE-350 | 5.92 | 720.0 | 158.0 | 62.0 |
| Classe-FW-3.0m | cellule propre | P45B | 6S7P P45B | 6.85 | 680.0 | 161.0 | 67.0 |
| Classe-FW-3.0m | cellule propre | P50B | 6S6P P50B | 6.35 | 648.0 | 146.0 | 64.0 |
| Classe-FW-3.0m | cellule propre | SEMI-SOLIDE-350 | 6S3P SEMI-SOLIDE-350 | 5.92 | 720.0 | 132.0 | 62.0 |
| Classe-FW-3.0m | cellule propre + helice optimisee | P45B | 6S6P P45B | 6.39 | 583.0 | 133.0 | 64.0 |
| Classe-FW-3.0m | cellule propre + helice optimisee | P50B | 6S5P P50B | 5.9 | 540.0 | 120.0 | 62.0 |
| Classe-FW-3.0m | cellule propre + helice optimisee | SEMI-SOLIDE-350 | 6S2P SEMI-SOLIDE-350 | 5.15 | 480.0 | 101.0 | 57.0 |
| MFE-Fighter-VTOL | nominal | P45B | AUCUNE |  |  |  |  |
| MFE-Fighter-VTOL | nominal | P50B | AUCUNE |  |  |  |  |
| MFE-Fighter-VTOL | nominal | SEMI-SOLIDE-350 | 6S5P SEMI-SOLIDE-350 | 8.25 | 1200.0 | 318.0 | 76.0 |
| MFE-Fighter-VTOL | cellule propre | P45B | AUCUNE |  |  |  |  |
| MFE-Fighter-VTOL | cellule propre | P50B | 6S14P P50B | 10.8 | 1512.0 | 401.0 | 82.0 |
| MFE-Fighter-VTOL | cellule propre | SEMI-SOLIDE-350 | 6S4P SEMI-SOLIDE-350 | 7.48 | 960.0 | 238.0 | 74.0 |
| MFE-Fighter-VTOL | cellule propre + helice optimisee | P45B | AUCUNE |  |  |  |  |
| MFE-Fighter-VTOL | cellule propre + helice optimisee | P50B | 6S10P P50B | 8.97 | 1080.0 | 277.0 | 78.0 |
| MFE-Fighter-VTOL | cellule propre + helice optimisee | SEMI-SOLIDE-350 | 6S4P SEMI-SOLIDE-350 | 7.48 | 960.0 | 215.0 | 74.0 |
| Classe-VTOL-2.7m | nominal | P45B | AUCUNE |  |  |  |  |
| Classe-VTOL-2.7m | nominal | P50B | AUCUNE |  |  |  |  |
| Classe-VTOL-2.7m | nominal | SEMI-SOLIDE-350 | 6S6P SEMI-SOLIDE-350 | 9.92 | 1440.0 | 379.0 | 77.0 |
| Classe-VTOL-2.7m | cellule propre | P45B | AUCUNE |  |  |  |  |
| Classe-VTOL-2.7m | cellule propre | P50B | AUCUNE |  |  |  |  |
| Classe-VTOL-2.7m | cellule propre | SEMI-SOLIDE-350 | 6S5P SEMI-SOLIDE-350 | 9.15 | 1200.0 | 289.0 | 75.0 |
| Classe-VTOL-2.7m | cellule propre + helice optimisee | P45B | AUCUNE |  |  |  |  |
| Classe-VTOL-2.7m | cellule propre + helice optimisee | P50B | AUCUNE |  |  |  |  |
| Classe-VTOL-2.7m | cellule propre + helice optimisee | SEMI-SOLIDE-350 | 6S4P SEMI-SOLIDE-350 | 8.38 | 960.0 | 230.0 | 73.0 |

## Controles independants

- FM x eta_ME implicite du banc MN4014 16x5.4 (rho banc suppose 1.20): 0.599 (modele nominal 0.68x0.85 = 0.578)
- Believer 4.5 kg, 20 m/s, niveau mer, cas optimiste: Wh/km modele: 2.34 (essai vendeur: 355 Wh x (0.8 a 1.0) / 90 km = 3.2 a 3.9 Wh/km (conditions inconnues))
- Believer 4.5 kg, 20 m/s, niveau mer, cas nominal: Wh/km modele: 3.29 (essai vendeur: 355 Wh x (0.8 a 1.0) / 90 km = 3.2 a 3.9 Wh/km (conditions inconnues))
- Believer 4.5 kg, 20 m/s, niveau mer, cas pessimiste: Wh/km modele: 5.03 (essai vendeur: 355 Wh x (0.8 a 1.0) / 90 km = 3.2 a 3.9 Wh/km (conditions inconnues))
- Energie potentielle 5 kg sur 300 m (Wh), avant rendement: 4.09 (m g h / 3600)
