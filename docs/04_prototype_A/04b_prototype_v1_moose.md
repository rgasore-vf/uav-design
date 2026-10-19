# Dossier 04b : Prototype v1, Fixed Wing sur cellule Flightory Moose

Version 0.4, 19 octobre 2026. Révision v0.4 : objectif imposé Sony FE 40 mm F2.5 G, licence Flightory en cours de demande. Ce document intègre les décisions de l'utilisateur du 19 octobre 2026 et définit **le prototype v1** : un appareil simple, construit proprement, instrumenté et testé avec méthode. L'objectif de 2 h de vol (Dossier 03b) reste la cible de la version suivante.

Les calculs sont faits avec le scénario `calc/scenarios/prototype_moose_v1.json` (sorties dans `calc/out_prototype_v1/`, régénérées par `make calc`). Ce sont des estimations, pas des mesures.

## 1. Décisions intégrées

| Décision | Contenu | Conséquence |
|---|---|---|
| D-01 | Commencer avec 20 à 30 km de transit au total | Référence 2 × 15 km, variante 2 × 10 km |
| D-02 | GSD de 10 à 12 cm/px ; GNSS standard pour le prototype, RTK plus tard | Avec l'objectif de 40 mm, 10-12 cm exigeraient 1062-1274 m AGL, au-dessus du plafond de 1000 m : **9,4 cm à 1000 m AGL** (section 4) ; points de contrôle au sol pour vérifier la précision |
| D-09 | Objectif Sony FE 40 mm F2.5 G (0,28 m / 0,92 ft, Φ 49 mm) | 173 g, 68 × 45 mm (R38) |
| D-10 | Contact avec Flightory pour la licence | En cours |
| D-03 | Prototype sur fuselage Flightory, puis licence institutionnelle ou fuselage propre | Moose retenu pour le prototype v1 ; voir la section 2 sur la licence |
| D-04 | Zone d'environ 100 m disponible | Catapulte et atterrissage sur patins ou parachute ; la nature des abords reste à préciser (D-08) |
| D-07 | Chercher d'autres cellules FW, sans viser une performance exceptionnelle | Section 7 |

## 2. Licence Flightory : ce que dit le texte

Je ne suis pas juriste. Ce qui suit est une lecture factuelle de la licence (R02), à faire confirmer par Flightory.

- La section 1 interdit l'usage « commercial ou institutionnel » sans licence séparée. Un prototype construit et opéré par une organisation relève déjà de ce cas, même s'il s'agit d'un essai.
- La section 4 autorise la modification uniquement pour un usage personnel.
- La section 5 précise que tout aéronef imprimé à partir de ces fichiers reste soumis à la licence. **Un fuselage obtenu en modifiant les fichiers Flightory n'échappe donc pas à leur licence.**
- Seule une conception indépendante, qui ne dérive pas de leurs fichiers, constituerait un fuselage réellement « propre ».

**Recommandation.** Écrire à Flightory dès maintenant pour obtenir le prix et les conditions de la licence institutionnelle, avant d'imprimer. Le coût est probablement faible au regard du projet, mais je n'ai pas trouvé de prix publié. Le travail de conception et de calcul peut avancer en parallèle.

## 3. Configuration du prototype v1

| Sous-système | Choix | Source ou statut |
|---|---|---|
| Cellule | Flightory Moose, 1600 mm, 36,5 dm², S3021, empennage en V, version avec patins TPU | R01 |
| Propulsion | 2 moteurs de classe 28XX tractifs. Exemple du manuel : Avenger 2812 910 kV, hélices de 9 à 10 pouces, ESC de 35 à 60 A, 4S à 6S | R01. Sélection finale en Phase 3 : un KV plus faible avec une hélice plus grande améliorerait le rendement en croisière, si la garde au sol et la nacelle le permettent (à vérifier) |
| Batterie | Li-ion P45B 6S3P pour les premiers vols, puis **6S4P** pour la mission | R04 |
| Autopilote | CUAV X7+ Pro existant, ArduPilot Plane | R15 |
| GNSS | Récepteur standard, sans RTK ; journalisation brute activée si le récepteur le permet, pour préparer le PPK | D-02 |
| Caméra | Sony ILX-LR1 + **Sony FE 40 mm F2.5 G** (173 g, Ø 68 × 45 mm, filtre de 49 mm, mise au point minimale de 0,28 m en AF) | R07, R38 |
| Lancement | Catapulte élastique, course de 3 à 4 m | Section 5 |
| Récupération | Atterrissage sur patins si les abords sont dégagés ; parachute sinon | Section 5, D-08 |

### 3.1 Bilan de masse (configuration 6S4P, patins)

| Poste | Masse (g) | Statut |
|---|---|---|
| Cellule imprimée, carbone, 2 moteurs, 2 ESC, 4 servos, câblage | 1200 (1000 à 1500) | HYP |
| Avionique (X7+ Pro, GNSS, radio, Pitot, BEC, interface caméra) | 320 | SRC + EST |
| Charge utile : boîtier 243 + objectif 173 + support et câbles 100 | **516**, soit 16 g au-dessus de l'enveloppe de 500 g (PL-01) | SRC + EST |
| Batterie 6S4P (24 × 70 g + 10 %) | 1848 | SRC + HYP |
| **Total** | **3884**, soit 86 % de la MTOW de 4,5 kg | |

En configuration 6S3P (premiers vols), la masse est de 3,42 kg, soit 76 % de la MTOW. Avec un parachute (+0,2 kg estimé), le 6S4P passe à 4,08 kg, soit 91 % de la MTOW.

**PL-01.** Pour respecter l'enveloppe de 500 g, le support, l'amortissement et les câbles doivent peser 84 g au plus. Sinon, il faut acter 516 g, ce qui a un effet négligeable sur l'énergie (inclus dans les calculs).

**Intégration dans la soute.** La soute fait 90 mm de haut. Le boîtier (42,5 mm) et l'objectif (45 mm) font 87,5 mm, ce qui laisse 2,5 mm. C'est trop peu pour un support amorti, dont le débattement demande plusieurs millimètres. L'objectif devra probablement dépasser sous le fuselage à travers une ouverture. Il serait alors exposé à l'atterrissage sur patins. Il faut soit un carénage avec fenêtre optique, soit un parachute, soit un support escamotable. **C'est un point à résoudre en CAO avant toute impression.**

**Logement de la batterie.** Le compartiment fait 225 mm de long, 90 mm de haut, et 120 à 60 mm de large en se rétrécissant vers le nez (R01). Un 6S4P en cellules 21700 couchées, 3 en longueur × 4 en hauteur × 2 en largeur, occupe environ 210 × 86 × 43 mm. Il tient sur le papier, mais le câblage et les barrettes de connexion sont à vérifier en CAO.

## 4. Photogrammétrie avec l'objectif Sony FE 40 mm

Capteur : 35,8 × 23,9 mm, 9504 × 6336 px, pas de 3,77 µm (R09). La relation est H = GSD × f / pas.

**Conflit entre exigences.** Avec f = 40 mm, un GSD de 10 à 12 cm demande de voler à **1062 à 1274 m AGL**, au-dessus du plafond de 1000 m (MIS-04). Le maximum atteignable sous ce plafond est **9,4 cm/px à 1000 m**, plus fin que la cible : la qualité y gagne, la couverture un peu moins. Je retiens 1000 m AGL comme hauteur de référence.

| Hauteur AGL | GSD | Empreinte | Interligne (ortho 80/70) | Intervalle à 18 m/s | Couverture ortho | Images/km² | RAW brut |
|---|---|---|---|---|---|---|---|
| 700 m | 6,6 cm | 626 × 418 m | 188 m | 4,6 s | 9,7 km²/h | 64 | 6,7 Go/km² |
| 850 m | 8,0 cm | 761 × 507 m | 228 m | 5,6 s | 11,8 km²/h | 43 | 4,6 Go/km² |
| **1000 m (référence)** | **9,4 cm** | **895 × 597 m** | **269 m** | **6,6 s** | **13,9 km²/h** | **31** | **3,3 Go/km²** |
| 1062 m (hors plafond) | 10,0 cm | 950 × 634 m | 285 m | 7,0 s | 14,8 km²/h | 28 | 2,9 Go/km² |

- **Couverture par vol.** 30 minutes d'acquisition à 1000 m couvrent environ 7 km² en ortho, ou environ 4,6 km² en 3D (80/80).
- **Flou et cadence.** Le flou est négligeable (0,19 px à 1/1000 s), et la cadence ne contraint pas (un déclenchement toutes les 6,6 s).
- **Réglages de l'objectif, à vérifier au banc.** Mise au point à l'infini, ouverture de f/5,6 à f/8 (hypothèse de netteté). Comme la mise au point est commandée électroniquement, sa tenue après la mise sous tension et sous vibrations doit être vérifiée : il faut soit déclencher en AF-S via la broche FOCUS, soit vérifier que la position MF est conservée. Les bagues de l'objectif (ouverture, commutateurs) doivent être immobilisées.

**Contraintes de la hauteur de 1000 m AGL :**

1. **Autorisation.** Elle doit être obtenue explicitement auprès de l'AAC.
2. **Nébulosité.** La base des nuages doit être au-dessus de 1000 m AGL sur la zone de travail. Il faut une statistique de base de nuages sur les sites ; à défaut, voler plus bas, ce qui affine le GSD et réduit la couverture.
3. **Relief.** Une variation de terrain de ±200 m fait varier le GSD d'environ ±20 % à 1000 m. Il faut planifier en suivi de terrain, ou calculer les recouvrements au point le plus haut.
4. **Densité de l'air.** La croisière se fait à environ 1960 m AMSL, avec une densité de 0,94 kg/m³ par temps chaud. C'est pris en compte dans les calculs.

**Précision.** Un GNSS autonome donne un géoréférencement absolu de l'ordre du mètre au mieux. La précision réelle doit être **mesurée** sur des points de contrôle au sol.

## 5. Lancement et récupération dans une zone d'environ 100 m

**Lancement** (3,88 kg, site à 960 m par 30 °C, CLmax de 1,1) :

| Grandeur | Valeur |
|---|---|
| Vs | 13,5 m/s |
| Vitesse de lancement visée | 16,9 m/s |
| Catapulte de 3 m | 4,9 g en moyenne, environ 7,8 g en crête, environ 296 N |
| Catapulte de 4 m | 3,6 g en moyenne, environ 5,8 g en crête |

Le lancement à la main n'est pas réaliste à cette masse. Une catapulte de 3 à 4 m tient largement dans 100 m.

**Atterrissage sur patins.** Au toucher à 1,1 Vs (environ 15 m/s), l'énergie vaut environ 429 J. La glissade sur herbe est d'environ V²/(2μg) ≈ 25 m, avec un coefficient de frottement μ ≈ 0,45 (hypothèse). Le facteur limitant n'est pas la glissade mais **l'approche**. Sans volets, la pente d'approche est d'environ 1/(L/D), soit environ 1/10. Pour passer au-dessus d'obstacles de 20 m, il faut donc environ 200 m dégagés en amont du point de toucher.

**Conséquence (D-08).**
- Si les 100 m sont une bande avec des abords dégagés, comme un champ ou une piste, l'atterrissage sur patins convient.
- Si c'est une clairière entourée d'arbres, il faut un **parachute**. La configuration passe alors à 4,08 kg et 91 % de la MTOW, ce qui reste faisable (marge de 26 Wh à 30 minutes d'acquisition), ou à un VTOL.
- Dans les deux cas, l'objectif qui dépasse sous le fuselage (section 3.1) doit être protégé.

## 6. Performances de la mission prototype

Mission : 2 × 15 km, acquisition à 1000 m AGL (9,4 cm/px), vent de 5 m/s, ISA+21 °C, 30 % de réserve, charge utile de 516 g.

| Configuration | Acquisition | Masse | Besoin avec réserve | Utilisable | Marge |
|---|---|---|---|---|---|
| Moose, patins, 6S4P | 30 min | 3,88 kg | 288 Wh | 330 Wh | **+42 Wh** |
| Moose, patins, 6S4P, vent de 8 m/s | 30 min | 3,88 kg | 305 Wh | 330 Wh | +26 Wh |
| Moose, patins, 6S4P, vent de 10 m/s | 30 min | 3,88 kg | 324 Wh | 330 Wh | +6 Wh |
| Moose, patins, 6S4P | 45 min | 3,88 kg | 343 Wh | 330 Wh | −12 Wh |
| Moose, patins, 6S3P | 30 min | 3,42 kg | 256 Wh | 248 Wh | −9 Wh (6S3P limité à environ 15 min d'acquisition) |
| Moose, parachute, 6S4P | 30 min | 4,08 kg | 304 Wh | 330 Wh | +26 Wh |
| B, Fighter VTOL, 6S8P (rappel) | 30 min | 8,13 kg | 672 Wh | 661 Wh | −11 Wh |

**Mission de référence.** Le prototype v1 en 6S4P tient 30 minutes d'acquisition, soit environ 7 km² à 9,4 cm/px, avec une marge confortable jusqu'à 8 m/s de vent. La durée de vol est d'environ 75 minutes, dont environ 8 minutes de montée jusqu'à 1000 m et environ 6 minutes de descente. **Voler à 1000 m plutôt qu'à 700 m, avec un objectif plus lourd, coûte environ 22 Wh de marge** : montée plus longue et air moins dense.

**Sensibilité** (`calc/out_prototype_v1/sensibilite.csv`) :

| Paramètre | Amplitude |
|---|---|
| Durée d'acquisition | 164 Wh |
| Rendement propulsif | 100 Wh |
| CD0 | 70 Wh |
| Énergie utilisable | 58 Wh |
| Vent | 44 Wh |
| Masse sèche | 41 Wh |

**Pire cas plausible.** Avec un rendement de 0,40, la marge tombe à −29 Wh. Le rendement propulsif reste le premier paramètre à mesurer.

**Prototype B.** Dans ce scénario, le VTOL ne tient plus 30 minutes d'acquisition avec un 6S8P (−11 Wh), à cause de la montée et de la croisière à 1000 m. Il reste limité à environ 15 minutes en 6S6P.

## 7. Autres cellules Fixed Wing recherchées

| Cellule | Données vérifiées | Avis pour un prototype |
|---|---|---|
| **MakeFlyEasy Believer 1960** | 51 dm², MTOW 5,5 kg, bimoteur, soute de 120 × 150 × 119 mm, parachute prévu (R11, R12) | **Meilleure alternative.** Plus de marge de masse que le Moose, produit commercial sans contrainte de licence. Disponibilité à vérifier (rupture chez deux revendeurs). |
| **MFD Crosswind Nimbus Pro 1900** | 1900 mm, AUW de 4 à 6,5 kg, 4S à 6S, moteur 2820 600 kV recommandé, 319,99 USD (R33) | **Candidate sérieuse.** Enveloppe de masse plus large que le Moose. La surface alaire n'est pas publiée : à mesurer ou à obtenir avant de la modéliser. |
| Skywalker X8 | 2122 mm, 80 dm², charge utile de 1 à 2 kg (R19, secondaire) | Aile volante robuste à l'atterrissage sur le ventre. MTOW non documentée en source primaire. |
| Skywalker 1800 | 45 dm², masse en vol de 1,3 à 1,8 kg (R34) | Écartée : enveloppe trop légère pour la caméra et la batterie |
| Heewing T2 Cruza | 1,2 m d'envergure (revendeurs) | Écartée : trop petite |
| Flightory Stork | 1620 mm, AUW de 1,4 à 3,1 kg (site Flightory) | Écartée : enveloppe plus faible que le Moose, même licence |
| X-UAV Talon (fiche xboom.in) | Page incohérente : nom « 1718 » mais 2,5 m indiqués, 4,5 kg à vide, 2 h annoncées (R35) | Non retenue : données non fiables |

## 8. Ce que « bien fait » veut dire pour ce prototype

1. **Pesée et centrage réels** avant tout vol : CG à 48 mm du bord d'attaque à l'emplanture, selon le manuel (R01), vérifié sur trois points d'appui.
2. **Banc de propulsion** : poussée statique, courant et température ; vérification de l'alimentation sous charge (chute de tension, BEC).
3. **Interface caméra validée au banc** : séquence FOCUS puis TRIGGER, mesure du délai entre TRIGGER et EXPOSURE, retour d'exposition journalisé par ArduPilot.
4. **Vols progressifs** avec critères d'arrêt écrits :
   1. vol sans caméra, avec une masse factice de 500 g ;
   2. réglage automatique (AUTOTUNE) ;
   3. identification de la polaire et du rendement : paliers à 14, 16, 18 et 20 m/s, avec relevé de la puissance électrique ;
   4. acquisition sur 1 km² avec points de contrôle au sol ;
   5. extension de distance : 2 × 5 km, puis 2 × 10 km, puis 2 × 15 km.
5. **Journal de vol et registre des anomalies.** Chaque vol met à jour les hypothèses H01, H04, H09 et H17 du registre.
