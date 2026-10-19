# uav-design : UAV de cartographie, prototypes A (Fixed Wing) et B (VTOL)

Version 0.2, 19 octobre 2026. Phases couvertes : 0 (audit et reprise), 1 (recherche et exigences) et 2 (avant-projets). Les dossiers 06 à 09 seront produits en Phases 3 à 5. Je ne crée pas de fichiers vides pour les annoncer.

## 1. Objectifs et contraintes reformulés

Il s'agit de concevoir, à coût maîtrisé, une plateforme de cartographie photogrammétrique emportant une Sony ILX-LR1, exploitable sans infrastructure dans l'environnement du Parc national des Virunga. Deux avant-projets sont menés à précision comparable, sur une mission, une charge utile et des critères identiques, avant toute décision.

| Contrainte connue | Valeur | Origine |
|---|---|---|
| Transit | 20 km aller + 20 km retour | Utilisateur ; définition à confirmer (D-01) |
| Charge utile | ILX-LR1, ≤ 500 g avec objectif et support | Utilisateur |
| Altitude du site / hauteur maximale | 960 m AMSL / 1000 m AGL | Utilisateur |
| Réserve | 30 % de l'énergie utilisable | Utilisateur |
| Autopilote | CUAV X7+ Pro existant (ArduPilot) | Utilisateur |
| Climat | Tropical d'altitude ; dimensionnement à ISA+21 °C | Hypothèse H16 |

## 2. Organisation du dépôt

```
uav-design/
├── README.md                     Ce document : objectifs, résultats, programme, décisions
├── CHANGELOG.md                  Historique des versions du dossier
├── Makefile                      make calc / make test
├── docs/
│   ├── 01_audit/                 Dossier 01 : audit de Blueprint (rapport + matrice CSV, 26 constats)
│   ├── 02_cahier_des_charges/    Dossier 02 : 33 exigences identifiées et méthodes de vérification
│   ├── 03_plateformes/           Dossier 03 : comparatif des cellules et architectures VTOL (ADR-001) ; 03b : faisabilité 2 h
│   ├── 04_prototype_A/           Dossier 04 : avant-projet Fixed Wing
│   └── 05_prototype_B/           Dossier 05 : avant-projet VTOL QuadPlane
├── calc/
│   ├── params.json               Toutes les entrées, avec leur statut SRC / HYP / EST
│   ├── model.py                  Modèle paramétrique (Python 3, bibliothèque standard uniquement)
│   └── out/                      Sorties générées (CSV + summary.md), versionnées pour la traçabilité
├── registres/
│   ├── references.csv            R01 à R27 : sources consultées, date, données extraites
│   ├── hypotheses.csv            H01 à H20 : hypothèses, plages, essai permettant de les lever
│   └── decisions.csv             D-01 à D-05 (décisions ouvertes), ADR-001 à ADR-003
├── sources/blueprint_2026-10-19/ Fichiers Blueprint d'origine, objet de l'audit (non modifiés)
└── tests/test_model.py           Tests de cohérence physique et de format (unittest)
```

Les dossiers 06 à 09 (économie, risques, fabrication, décision) seront ajoutés en Phases 3 à 5. Aucun fichier vide n'est créé pour les annoncer.

**Recalcul.** `make calc` (ou `python3 calc/model.py`) relit `calc/params.json` et régénère toutes les sorties de `calc/out/`. Toute valeur modifiée dans `params.json` (masse, batterie, vitesse, température, vent, durée d'acquisition, rendements) se propage aux bilans de masse, d'énergie, de lancement, de photogrammétrie et de sensibilité. Un autre jeu de paramètres peut être passé en argument ou via la variable d'environnement `UAV_PARAMS`.

**Tests.** `make test` (ou `python3 -m unittest discover -s tests -v`) vérifie l'atmosphère ISA, la cohérence polaire/finesse, la théorie de Froude contre les données de banc, la réserve, la monotonie énergie/vent/acquisition, la marge de décrochage et le format des CSV. Ces tests contrôlent la cohérence interne, pas la réalité : ils ne remplacent aucun essai.

**Règles de contribution.**
1. Toute nouvelle donnée entre dans `registres/references.csv` avec sa date de consultation.
2. Toute hypothèse entre dans `registres/hypotheses.csv` avec sa plage et l'essai qui la lèvera.
3. Après une modification de `params.json`, relancer `make calc` et mettre à jour les chiffres cités dans `docs/`.
4. Toute décision d'architecture est consignée dans `registres/decisions.csv`.

## 3. Résultats de l'avant-projet (estimations, non validées)

Mission de référence : 2 × 20 km, 30 min d'acquisition, vent de 5 m/s, ISA+21 °C, cas nominal.

| Critère | A : Believer 1960 + parachute | B : Fighter VTOL QuadPlane |
|---|---|---|
| Masse au décollage | 4,47 kg (81 % MTOW) | 8,12 kg (71 % MTOW) |
| Batterie | Li-ion 6S4P, 1,85 kg | Li-ion 6S8P, 3,70 kg |
| Énergie de mission / avec réserve | 224 / 320 Wh | 453 / 648 Wh |
| Marge | +11 Wh | +13 Wh |
| Vent de 8 m/s | Non tenu (6S5P nécessaire) | Non tenu (acquisition réduite à 15 min nécessaire) |
| Infrastructure au sol | Catapulte + zone de parachute d'environ 100 × 100 m | Environ 10 × 10 m |
| Paramètre le plus incertain | Rendement propulsif, CD0 | Masse sèche de la cellule VTOL, rotors de 4 à 5 kgf non sélectionnés |

**Lecture.** Les deux avant-projets bouclent en cas nominal, avec des marges trop minces pour un prototype. Aucun vainqueur n'est désigné. Le VTOL coûte environ deux fois l'énergie et la masse de cellules de batterie. Son avantage est entièrement conditionné par la surface disponible sur les sites (D-04).

### 3.1 Révision v0.2 : endurance de 2 h avec 30 % de réserve

L'exigence MIS-02 est passée à 2 h de vol avec 30 % de réserve, soit environ 171 minutes d'énergie embarquée à la puissance de croisière. Détail dans `docs/03_plateformes/03b_etude_endurance_2h.md` et `calc/out/endurance_2h.csv`.

| Configuration (vent de 5 m/s) | Li-ion P45B | Li-ion P50B | Haute énergie (HYP) |
|---|---|---|---|
| A : Believer, hypothèses nominales | Non faisable | Non faisable | 4,92 kg |
| A : Believer, cellule propre + hélice optimisée | 4,93 kg (90 % MTOW) | 4,90 kg | 4,15 kg |
| FW de classe 2,6 m, cellule propre + hélice optimisée | 5,99 kg | 5,50 kg | 4,75 kg |
| B : Fighter VTOL, cellule propre + hélice optimisée | Non faisable | 8,97 kg, 1080 Wh | 7,48 kg, 960 Wh |

**Lecture.** 2 h avec réserve est atteignable en Fixed Wing si la traînée et l'hélice sont optimisées, ce qui reste à mesurer. Le VTOL n'y parvient qu'avec des cellules haute énergie et environ 1 kWh de batterie. Le DeltaQuad Evo (R28) montre qu'un VTOL de la classe 8 à 10 kg le fait commercialement, d'abord grâce à son efficacité aérodynamique. Notre modèle reproduit sa puissance implicite à environ 10 % près.

## 4. Exigences critiques pour le choix entre A et B

1. **Surface de lancement et de récupération disponible sur les sites types (D-04).** C'est le critère qui peut rendre le VTOL obligatoire ou superflu.
2. **Durée ou surface d'acquisition par sortie (D-01).** Premier facteur de sensibilité pour A comme pour B. Le VTOL y est deux fois plus sensible (333 Wh contre 190 Wh d'amplitude).
3. **Vent opérationnel (MIS-06).** À 8 m/s, aucune des deux configurations de référence ne tient la mission.
4. **Exposition de la caméra au risque d'impact.** Environ 406 J sur le ventre et 56 J sous parachute pour A ; une descente verticale contrôlée pour B, mais sans tolérance à la perte d'un rotor en quad.
5. **Coût complet et fréquence des réparations** (Phase 4) : 48 contre 24 cellules Li-ion, 5 contre 2 groupes propulseurs, catapulte et parachute pour A.

## 5. Programme de dimensionnement détaillé (Phase 3)

| Lot | Contenu | Données d'entrée nécessaires | Sortie |
|---|---|---|---|
| P3-1 | Obtenir les fiches constructeur (masses à vide, CG, motorisations) de la Believer et du Fighter VTOL ; identifier au moins une autre cellule VTOL de la classe | Contact MakeFlyEasy et revendeurs | Mise à jour de H06 et H07 |
| P3-2 | Sélection moteur-hélice-ESC pour A (2 × 2814, choix 4S/6S) et B (croisière + 4 rotors de 4 à 5 kgf), sur courbes constructeur à la tension et l'hélice retenues | Courbes T-Motor, LDPOWER, etc. | Point de fonctionnement en croisière, en montée et en stationnaire à la densité chaude |
| P3-3 | Batterie : choix S/P, interconnexions, protection, comportement thermique ; essai de décharge d'un module 1S au profil de mission | Cellules P45B réelles | H09 mesurée |
| P3-4 | Centrage et implantation : tableau des bras de levier, CG par configuration (batterie, objectif 24 ou 35 mm), marge statique | CG constructeur, pesées | Plage de centrage |
| P3-5 | Structure : charges de catapulte (A), de stationnaire et d'atterrissage (B), fixations batterie et caméra, bras VTOL | STR-01, STR-02 | Notes de calcul + essais |
| P3-6 | Électrique : schéma complet, sections de câbles, protections, double alimentation de l'autopilote à modes de panne indépendants (vérifier Power A et Power C sur le X7+ Pro) | Documentation CUAV | Schéma + bilan électrique |
| P3-7 | Interface caméra : prototype sur banc, mesure des délais TRIGGER vers EXPOSURE, intervalle minimal réel | ILX-LR1 en main | PL-04 et PL-05 vérifiées au banc |
| P3-8 | Radio et réglementation : demande ARPTC (bande, puissance), dossier AAC, bilan de liaison sur 20 km avec relief | Réponses écrites | Choix de la radio |
| P3-9 | Simulation SITL des deux missions (ArduPilot), y compris les transitions et les failsafes | params.json | Scénarios de pannes simulés (pas une validation) |
| P3-10 | Essais précoces des deux paramètres dominants : identification de la polaire et du rendement propulsif sur une Believer instrumentée | Cellule A | H01 et H04 mesurés |

## 6. Décisions humaines bloquantes

Je ne vous demande que ce qui change réellement la conception. Les travaux P3-1 à P3-7 avancent sur les hypothèses en attendant vos réponses.

- **D-01** : que recouvrent exactement les 40 km, et quelle durée ou surface d'acquisition par sortie ? Hypothèse actuelle : 20 km de rayon et 30 min.
- **D-02** : quel GSD et quelle précision absolue visez-vous, en ortho ou en 3D ? Hypothèse : 3 cm/px, avec points de contrôle au sol.
- **D-04** : quelle surface dégagée existe sur les sites de lancement types ?
- **D-03** : faut-il demander une licence institutionnelle à Flightory, ou exclure leurs cellules ? Par défaut, exclusion.
- **D-05** : quel est le plafond budgétaire, et la caméra et un objectif sont-ils déjà en votre possession ?
- **D-06** : acceptez-vous des cellules de batterie haute énergie (classe 300 à 400 Wh/kg), plus chères et à durée de vie plus courte ?
- **D-07** : faut-il élargir la recherche à une cellule FW de 2,4 à 3 m optimisée pour l'endurance, puisque la Believer devient limite pour 2 h ?
