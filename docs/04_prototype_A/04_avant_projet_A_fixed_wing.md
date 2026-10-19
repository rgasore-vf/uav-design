# Dossier 04 : Prototype A, Fixed Wing (avant-projet v0.1)

Version 0.1, 19 octobre 2026. Ce document est un **avant-projet** (Phase 2). Il fixe l'architecture et les premiers budgets. Le dimensionnement détaillé (choix exact des moteurs, hélices et ESC, centrage chiffré, nomenclature datée) relève de la Phase 3. Aucun chiffre de ce document ne constitue une validation.

## 1. Architecture retenue

| Sous-système | Choix | Justification | Source |
|---|---|---|---|
| Cellule | MakeFlyEasy Believer 1960, bimoteur, EPO | Voir le Dossier 03 : MTOW 5,5 kg, soute compatible, essai vendeur avec un plein format | R11, R12 |
| Propulsion | 2 moteurs de classe 2814 tractifs, KV adapté à la tension du pack | Configuration d'origine ; poussée répartie ; bimoteur sans redondance garantie (à évaluer) | R12 |
| Énergie | Li-ion Molicel P45B, 6S4P en référence, 6S5P en variante | 210 Wh/kg pack (modèle) contre 184 Wh/kg pour la LiPo de référence ; le besoin en puissance de croisière est faible (environ 7 A) | R04, R21 |
| Autopilote | CUAV X7+ Pro existant, ArduPilot Plane | ADR-003 ; H743, 3 IMU, 2 baromètres, 2 CAN | R15 |
| Lancement | Catapulte élastique (course de 3 à 4 m) | Le lancement à la main à 4,5 kg n'est pas démontré | Section 5 |
| Récupération | Parachute (vitesse de descente de 4 à 6 m/s) ; atterrissage sur le ventre en secours | Protège la caméra : environ 56 J contre 406 J | Section 5 |
| Charge utile | Sony ILX-LR1 + Samyang AF 24 mm F2.8 FE (variante 35 mm) | 93 g et 37 mm de long ; tient dans la soute de 119 mm | R07, R24 |
| Liaison | Radio de télémétrie et C2 longue portée, bande à confirmer (RFD868x en candidate) | A14 ; puissance et bande soumises à l'ARPTC | R23 |

**Point à trancher en Phase 3 : 6S ou 4S.**

- **En 4S Li-ion** (12,0 à 16,8 V sur la plage 3,0 à 4,2 V/cellule), la caméra peut en principe être alimentée directement (10 à 18 V). Il est possible d'utiliser les moteurs 2814 KV900, spécifiés pour 3 à 4S (R22).
- **En 6S**, les courants sont plus faibles d'un tiers. Il faut un régulateur pour la caméra et des moteurs de KV plus faible, comme le LDPOWER 2814 KV510 cité par le vendeur (R12), dont la plage de tension reste à vérifier.

Le modèle énergétique est indépendant de ce choix au premier ordre. Le choix se fera sur les données moteur et sur la simplicité électrique.

## 2. Bilan de masse préliminaire

| Poste | Masse (g) | Statut |
|---|---|---|
| Cellule, 2 moteurs, 2 ESC, servos, câblage de puissance | 1600 (plage 1400 à 1900) | HYP H06 |
| Parachute et éjection | 200 | EST |
| Autopilote X7+ Pro | 105 | SRC R15 |
| GNSS | 50 | EST |
| Radio RFD868x | 14,5 | SRC R23 |
| Antennes et câbles radio | 40 | EST |
| Récepteur RC et antennes | 20 | EST |
| Pitot et capteur | 20 | EST |
| Capteur de courant et BEC | 60 | EST |
| Interface de déclenchement | 10 | EST |
| **Charge utile dimensionnante** | **500** (réel estimé 436 : boîtier 243 + objectif 93 + support et câbles 100) | SRC + EST |
| Batterie 6S4P P45B (24 × 70 g + 10 %) | 1848 | SRC R04 + HYP H10 |
| **Total** | **4468** | Soit 81 % de la MTOW de 5,5 kg |

Les masses souvent oubliées (visserie, connecteurs XT90, gaines, renforts de fixation pour les charges de catapulte) sont pour l'instant contenues dans le poste « cellule ». Elles seront détaillées par pesée en Phase 3. Une incertitude de ±300 g sur le total est réaliste à ce stade.

## 3. Performances (cas nominal, croisière à 1260 m AMSL et ISA+21 °C, densité 1,008 kg/m³)

| Grandeur | Valeur | Méthode |
|---|---|---|
| Charge alaire | 88 g/dm² | m/S |
| Vitesse de décrochage (CLmax 1,1) | 12,4 m/s à 1260 m ; 12,3 m/s au site à 960 m par temps chaud | √(2mg/ρSCLmax) |
| Vitesse de décrochage en virage à 30° | environ 13,3 m/s | Vs·√n, avec n = 1/cos 30° |
| Vitesse de transit optimale (vent de 5 m/s) | 16,2 m/s | Minimisation de P(V)·[1/(V−w) + 1/(V+w)] |
| Vitesse d'acquisition | 18 m/s, soit 1,45 Vs | H14, contrainte MIS-07 |
| Finesse en transit | 10,3 | Polaire parabolique, CD0 0,040, e 0,78, allongement 7,5 |
| Puissance électrique en palier (transit, avec auxiliaires) | 150 W | |
| Puissance électrique en acquisition (18 m/s) | 177 W | |
| Puissance en montée à 2 m/s | environ 320 W (environ 400 W à 3 m/s) | P_palier + mg·Vz/η |
| Courant batterie en croisière | environ 7 A en 6S | P/U |
| Rayon de virage à 30° et 18 m/s | 57 m | V²/(g·tan φ) |

**Contrôle indépendant.** À 4,5 kg, 20 m/s et au niveau de la mer, le modèle donne 3,29 Wh/km. L'essai vendeur (R12) correspond à 3,2 à 3,9 Wh/km. Les ordres de grandeur concordent, ce qui n'est pas une validation, car les conditions de l'essai vendeur sont inconnues.

## 4. Bilan énergétique de la mission de référence (2 × 20 km, 30 min d'acquisition, vent de 5 m/s)

| Phase | Énergie (Wh) |
|---|---|
| Montée à 300 m AGL (2 m/s) | 13,4 |
| Transit de 40 km (16,2 m/s air, vent de 5 m/s) | 113,9 |
| Acquisition, 30 min à 18 m/s | 88,6 |
| Descente | 0,4 |
| Tour de piste et approche (180 s) | 7,5 |
| **Mission** | **224** |
| **Besoin avec 30 % de réserve** | **320** |
| Énergie utilisable du 6S4P (0,85 × 389 Wh) | 330 |
| **Marge** | **+11 Wh (3 %)** |

Durée totale de vol : environ 78 minutes.

**Lecture.** La marge est trop faible pour un prototype. Trois leviers sont possibles, à arbitrer avec la décision D-01 :

1. Passer au 6S5P : 4,93 kg, 90 % de la MTOW, marge de 70 Wh à 5 m/s et de 39 Wh à 8 m/s.
2. Limiter l'acquisition à 15 minutes en 6S4P.
3. Mesurer tôt les deux paramètres dominants, le rendement propulsif et le CD0 (H04 et H01), qui peuvent déplacer la marge de ±50 à 100 Wh.

**Sensibilité** (`calc/out/sensibilite.csv`, amplitude de marge entre bornes) :

| Paramètre | Amplitude |
|---|---|
| Durée d'acquisition | 190 Wh |
| Rendement propulsif | 111 Wh |
| CD0 | 94 Wh |
| Vent | 83 Wh |
| Énergie utilisable | 58 Wh |
| Masse sèche | 25 Wh |
| Coefficient e | 18 Wh |

**Cas pessimiste.** Si les trois hypothèses défavorables (traînée, rendement, CLmax) se cumulent, aucune batterie compatible avec la MTOW ne permet 30 minutes d'acquisition (`calc/out/selection_batterie.csv`). Ce cumul est un coin de domaine, pas un cas probable. Il justifie toutefois de mesurer ces paramètres avant d'engager la nomenclature.

## 5. Lancement et récupération (masse de 4,47 kg, site à 960 m par 30 °C)

| CLmax | Vs (m/s) | V lancement (m/s) | Course 2 m : moy / crête (g) | Course 3 m | Course 4 m |
|---|---|---|---|---|---|
| 1,3 | 11,3 | 14,1 | 5,1 / 8,1 | 3,4 / 5,4 | 2,5 / 4,1 |
| 1,1 | 12,3 | 15,3 | 6,0 / 9,6 | 4,0 / 6,4 | 3,0 / 4,8 |
| 1,0 | 12,9 | 16,1 | 6,6 / 10,5 | 4,4 / 7,0 | 3,3 / 5,3 |

Hypothèses : accélération moyenne a = V²/(2L) ; rapport crête/moyenne de 1,6 (H20) pour une catapulte élastique. L'énergie à fournir vaut environ 520 J à 15,3 m/s, ce qui est à la portée d'une catapulte élastique de construction locale.

**Conséquence structurelle.** Avec une course de 3 m, la fixation de la batterie de 1,85 kg doit tenir environ 6,4 g × 1,85 × 9,81 ≈ 116 N en crête, dans l'axe longitudinal. La caméra et son objectif (environ 0,44 kg) doivent tenir environ 28 N. Ces efforts, et non les charges de vol, dimensionnent les supports (exigence STR-02).

**Récupération.** L'énergie cinétique vaut environ 406 J en atterrissage sur le ventre à 1,1 Vs (13,5 m/s), contre environ 56 J sous parachute à 5 m/s. Le parachute réduit l'énergie d'impact d'un facteur 7. Il ajoute en revanche une dérive au vent : un déploiement à 60 m donne 12 s de descente à 5 m/s, soit environ 60 m de dérive par 5 m/s de vent et un mécanisme d'éjection à fiabiliser. Au sol, une surface dégagée d'environ 100 × 100 m semble nécessaire au premier ordre, à confirmer par essais (D-04).

## 6. Photogrammétrie

Capteur : 35,8 × 23,9 mm, 9504 × 6336 px, pas de 3,77 µm (R09).

| Configuration | GSD | Empreinte (transversale × longitudinale) | Interligne (ortho 80/70) | Intervalle à 18 m/s | Flou à 1/2000 s | Couverture |
|---|---|---|---|---|---|---|
| 24 mm, 200 m AGL | 3,14 cm | 298 × 199 m | 89,5 m | 2,2 s | 0,29 px | 4,6 km²/h |
| 35 mm, 300 m AGL | 3,23 cm | 307 × 205 m | 92,1 m | 2,3 s | 0,28 px | 4,8 km²/h |
| 24 mm, 100 m AGL | 1,57 cm | 149 × 99 m | 44,8 m | 1,1 s | 0,57 px | 2,3 km²/h |

- **Couverture.** 30 minutes d'acquisition à 3 cm/px représentent environ 2,3 km², avec un rendement de virage de 0,8 (hypothèse).
- **Obturation.** À 1/1000 s, le flou atteint 0,57 px à 3 cm/px. Il faut donc fixer **1/2000 s ou plus court** pour respecter PL-03 (≤ 0,5 px). L'obturateur mécanique va jusqu'à 1/4000 s (R09).
- **Relief.** Le GSD et le recouvrement se dégradent au-dessus des points hauts du terrain. Il faut planifier à hauteur AGL constante (suivi de terrain sur MNT) ou calculer les recouvrements au point le plus haut (PL-06).
- **Données.** Environ 280 images par km² en ortho à 3 cm. En RAW non compressé de 14 bits, cela représente de l'ordre de 30 Go/km². La taille réelle des fichiers est à mesurer.

## 7. Architecture électrique (principe)

```
Pack 6S Li-ion ─ connecteur anti-étincelle ─┬─ capteur Hall Mauch HS-100 ─ BEC Mauch LV 5,35 V/3 A ─ X7 Power A
                                            ├─ ESC 1 ─ moteur gauche
                                            ├─ ESC 2 ─ moteur droit
                                            ├─ BEC servos 6 V (≥ 5 A) ─ rail servos
                                            ├─ BEC radio 5 V (≥ 2 A) ─ radio de télémétrie
                                            ├─ régulateur 12 V (≥ 1,5 A) ─ caméra broches 3 (+) et 2 (0 V)
                                            └─ seconde source autopilote, indépendante (à définir, voir PWR-01)
```

| Sous-système | Tension | Puissance moyenne | Crête | Statut |
|---|---|---|---|---|
| Propulsion (2 moteurs) | 6S, 18 à 25,2 V | 130 à 160 W | environ 400 W en montée à 3 m/s, plus le lancement | Modèle |
| Caméra | 12 V | 3,8 W | à mesurer (appel à la mise sous tension) | R10 |
| Autopilote + GNSS + Pitot | 5,35 V | environ 4 W | | EST |
| Radio RFD868x | 5 V | environ 2 W | 4 W (0,8 A) | R23 + EST |
| Servos | 6 V | environ 3 W | à mesurer en rafale | EST |

**Interface de déclenchement** (R08) :

- **FOCUS (broche 4)** : maintenu à 0 V par un transistor en drain ouvert piloté par une sortie de l'autopilote. Il faut régler la caméra en mise au point manuelle à l'infini, ou en priorité au déclenchement, pour éviter un refus de déclenchement.
- **TRIGGER (broche 5)** : impulsion vers 0 V par un second transistor en drain ouvert. La largeur minimale n'est pas publiée et doit être mesurée.
- **EXPOSURE (broche 6)** : sortie en drain ouvert avec un pull-up de 10 kΩ vers 3,3 V, reliée à une entrée de capture de l'autopilote. Condition Sony : V_IL ≥ A/(B+1) = 3,3/11 = 0,30 V, à comparer au V_IL de l'entrée (à vérifier sur la documentation CUAV ; de l'ordre de 1 V pour une entrée 3,3 V usuelle).
- Le 0 V de l'autopilote doit être relié à la broche 2.
- Les paramètres ArduPilot de déclenchement et de retour (CAM1_*) sont à vérifier sur la documentation de la version installée.

## 8. Risques propres à A, à traiter en Phase 3

1. La marge énergétique est faible à la mission de référence (section 4).
2. La catapulte et la fiabilité du parachute deviennent les fonctions critiques pour la sécurité de la caméra.
3. L'EPO, la soute fermée et la caméra limitée à 50 °C posent un problème thermique au soleil.
4. Bimoteur : la perte d'un moteur crée un moment de lacet. Il faut évaluer la capacité de l'appareil à rentrer sur un moteur, et non la supposer.
5. Disponibilité de la cellule : elle est en rupture chez deux revendeurs. Il faut identifier le stock ou une cellule de repli.
