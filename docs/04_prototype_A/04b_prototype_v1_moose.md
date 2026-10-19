# Dossier 04b : Prototype v1, Fixed Wing sur cellule Flightory Moose

Version 0.3, 19 octobre 2026. Ce document intègre les décisions de l'utilisateur du 19 octobre 2026 et définit **le prototype v1** : un appareil simple, construit proprement, instrumenté et testé avec méthode. L'objectif de 2 h de vol (Dossier 03b) reste la cible de la version suivante.

Les calculs sont faits avec le scénario `calc/scenarios/prototype_moose_v1.json` (sorties dans `calc/out_prototype_v1/`, régénérées par `make calc`). Ce sont des estimations, pas des mesures.

## 1. Décisions intégrées

| Décision | Contenu | Conséquence |
|---|---|---|
| D-01 | Commencer avec 20 à 30 km de transit au total | Référence 2 × 15 km, variante 2 × 10 km |
| D-02 | GSD de 10 à 12 cm/px ; GNSS standard pour le prototype, RTK plus tard | Vol à 425-765 m AGL selon la focale (section 4) ; points de contrôle au sol pour vérifier la précision |
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
| Caméra | Sony ILX-LR1 ; objectif de 24 mm (Samyang AF 24 mm F2.8 FE, 93 g, 37 mm) en référence | R07, R24 |
| Lancement | Catapulte élastique, course de 3 à 4 m | Section 5 |
| Récupération | Atterrissage sur patins si les abords sont dégagés ; parachute sinon | Section 5, D-08 |

### 3.1 Bilan de masse (configuration 6S4P, patins)

| Poste | Masse (g) | Statut |
|---|---|---|
| Cellule imprimée, carbone, 2 moteurs, 2 ESC, 4 servos, câblage | 1200 (1000 à 1500) | HYP |
| Avionique (X7+ Pro, GNSS, radio, Pitot, BEC, interface caméra) | 320 | SRC + EST |
| Charge utile dimensionnante | 500 (réelle estimée 436) | SRC + EST |
| Batterie 6S4P (24 × 70 g + 10 %) | 1848 | SRC + HYP |
| **Total** | **3868**, soit 86 % de la MTOW de 4,5 kg | |

En configuration 6S3P (premiers vols), la masse est de 3,41 kg, soit 76 % de la MTOW. Avec un parachute (+0,2 kg estimé), le 6S4P passe à 4,07 kg, soit 90 % de la MTOW.

**Logement de la batterie.** Le compartiment fait 225 mm de long, 90 mm de haut, et 120 à 60 mm de large en se rétrécissant vers le nez (R01). Un 6S4P en cellules 21700 couchées, 3 en longueur × 4 en hauteur × 2 en largeur, occupe environ 210 × 86 × 43 mm. Il tient sur le papier, mais le câblage et les barrettes de connexion sont à vérifier en CAO.

## 4. Photogrammétrie pour un GSD de 10 à 12 cm

Capteur : 35,8 × 23,9 mm, 9504 × 6336 px, pas de 3,77 µm (R09). La relation est H = GSD × f / pas.

| Focale | Hauteur AGL pour 10 à 12 cm | Empreinte à 11 cm | Intervalle de déclenchement (ortho 80/70, 18 m/s) | Couverture |
|---|---|---|---|---|
| 16 mm | 425 à 510 m | 1045 × 697 m | 7 à 8,5 s | 15 à 18 km²/h |
| 20 mm | 531 à 637 m | idem | idem | idem |
| 24 mm (référence) | 637 à 765 m | idem | 7,7 s à 700 m | 16 km²/h |

- **Couverture par vol.** 30 minutes d'acquisition correspondent à environ 8 km² en ortho. En 3D (80/80), le chiffre tombe à environ 5,4 km².
- **Flou et cadence.** Le flou est négligeable (0,16 px à 1/1000 s), et la cadence ne contraint pas (un déclenchement toutes les 7 s ou plus).
- **Volume de données.** Environ 23 images par km², soit environ 2,4 Go/km² en RAW brut.

**Trois contraintes nouvelles apparaissent avec ce GSD :**

1. **Hauteur de vol.** Voler à 425-765 m AGL demande une autorisation explicite de l'AAC. Une focale plus courte réduit la hauteur nécessaire d'environ 30 %.
2. **Nébulosité.** Dans la région des Virunga, une base de nuages sous la hauteur de vol interdit l'acquisition. Plus la focale est courte, plus on vole bas, ce qui donne un argument pour 16 à 20 mm. Il faut une statistique de base de nuages sur les sites.
3. **Relief.** Avec une altitude AMSL constante, une variation de terrain de ±200 m fait varier le GSD de ±30 % à 700 m AGL. Il faut planifier en suivi de terrain sur un MNT, ou calculer les recouvrements au point le plus haut (PL-06).

**Précision.** Un GNSS autonome donne un géoréférencement absolu de l'ordre du mètre au mieux, qui dépend du récepteur et des conditions. Pour un prototype, c'est acceptable à condition de **mesurer** la précision obtenue sur des points de contrôle au sol, plutôt que de la supposer.

**Choix de caméra.** À 10-12 cm/px, la résolution de 61 MP de l'ILX-LR1 sert surtout à couvrir plus de surface par image. Un appareil plus léger et moins cher atteindrait ce GSD à plus basse altitude. Je garde l'ILX-LR1, qui est ton choix et prépare les GSD plus fins de l'avenir, mais c'est un arbitrage à reconsidérer si le budget ou la masse deviennent limitants.

## 5. Lancement et récupération dans une zone d'environ 100 m

**Lancement** (3,87 kg, site à 960 m par 30 °C, CLmax de 1,1) :

| Grandeur | Valeur |
|---|---|
| Vs | 13,5 m/s |
| Vitesse de lancement visée | 16,9 m/s |
| Catapulte de 3 m | 4,8 g en moyenne, environ 7,7 g en crête, environ 293 N |
| Catapulte de 4 m | 3,6 g en moyenne, environ 5,8 g en crête |

Le lancement à la main n'est pas réaliste à cette masse. Une catapulte de 3 à 4 m tient largement dans 100 m.

**Atterrissage sur patins.** Au toucher à 1,1 Vs (environ 15 m/s), l'énergie vaut environ 426 J. La glissade sur herbe est d'environ V²/(2μg) ≈ 25 m, avec un coefficient de frottement μ ≈ 0,45 (hypothèse). Le facteur limitant n'est pas la glissade mais **l'approche**. Sans volets, la pente d'approche est d'environ 1/(L/D), soit environ 1/10. Pour passer au-dessus d'obstacles de 20 m, il faut donc environ 200 m dégagés en amont du point de toucher.

**Conséquence (D-08).**
- Si les 100 m sont une bande avec des abords dégagés, comme un champ ou une piste, l'atterrissage sur patins convient.
- Si c'est une clairière entourée d'arbres, il faut un **parachute**. La configuration passe alors à 4,07 kg et 90 % de la MTOW, ce qui reste faisable (marge de 49 Wh à 30 minutes d'acquisition), ou à un VTOL.

## 6. Performances de la mission prototype

Mission : 2 × 15 km, acquisition à 700 m AGL, vent de 5 m/s, ISA+21 °C, 30 % de réserve.

| Configuration | Acquisition | Masse | Besoin avec réserve | Utilisable | Marge |
|---|---|---|---|---|---|
| Moose, patins, 6S4P | 30 min | 3,87 kg | 267 Wh | 330 Wh | **+64 Wh** |
| Moose, patins, 6S4P | 45 min | 3,87 kg | 320 Wh | 330 Wh | +10 Wh |
| Moose, patins, 6S3P | 30 min | 3,41 kg | 240 Wh | 248 Wh | +7 Wh |
| Moose, parachute, 6S4P | 30 min | 4,07 kg | | | +49 Wh |
| B, Fighter VTOL, 6S8P (rappel) | 30 min | 8,12 kg | 629 Wh | 661 Wh | +32 Wh |

**Mission de référence.** Le prototype v1 en 6S4P tient 30 minutes d'acquisition, soit environ 8 km² à 11 cm/px, avec une vraie marge. Il tient encore à 8 m/s de vent (+47 Wh) et à 10 m/s (+28 Wh). La durée de vol est d'environ 70 minutes, réserve non consommée.

**Sensibilité** (`calc/out_prototype_v1/sensibilite.csv`) :

| Paramètre | Amplitude |
|---|---|
| Durée d'acquisition | 160 Wh |
| Rendement propulsif | 92 Wh |
| CD0 | 67 Wh |
| Énergie utilisable de la batterie | 58 Wh |
| Vent | 44 Wh |
| Masse sèche | 35 Wh |

**Pire cas plausible.** Avec un rendement de 0,40, la marge tombe à −2 Wh. Le rendement propulsif est donc le premier paramètre à mesurer.

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
