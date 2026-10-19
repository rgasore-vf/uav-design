# Historique

## v0.2 (2026-10-19)

- Exigence MIS-02 révisée : 2 h de vol en conservant 30 % de réserve.
- `calc/model.py` : fonction `size_for_flight_time`, nouvelle sortie `calc/out/endurance_2h.csv` (5 cellules, 3 variantes aéro-propulsives, 3 technologies de cellules, vents de 0, 5 et 8 m/s).
- Dossier 03b : étude de faisabilité 2 h, contrôle indépendant contre le DeltaQuad Evo.
- Registres : R28 à R31, H21 à H24, REQ-2026-10-19, D-06, D-07.

## v0.1 (2026-10-19)

Phases 0 à 2 : audit et reprise, recherche et exigences, avant-projets.

- Dossier 01 : audit contradictoire de la sortie Blueprint (26 constats, dont 6 bloquants).
- Dossier 02 : cahier des charges provisoire (33 exigences, méthodes de vérification).
- Dossier 03 : comparatif Believer 1960, Moose, Skywalker X8, Ranger 2000 ; architectures VTOL ; ADR-001 (QuadPlane).
- Dossiers 04 et 05 : avant-projets A (Believer 1960 + parachute) et B (Fighter VTOL QuadPlane).
- Modèle paramétrique `calc/model.py` : atmosphère, polaire, mission avec vent, stationnaire, photogrammétrie, lancement, sensibilité.
- Registres : 27 références, 20 hypothèses, 5 décisions ouvertes, 3 ADR.
- Tests de cohérence (11) et intégration continue GitHub Actions.
