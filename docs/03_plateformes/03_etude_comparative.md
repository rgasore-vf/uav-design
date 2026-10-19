# Dossier 03 : Étude comparative des plateformes

Version 0.1, 19 octobre 2026. Les données sont tirées des références R01 à R27. Les résultats du modèle sont des estimations issues des hypothèses H01 à H20.

## 1. Cellules à voilure fixe

### 1.1 Données vérifiées

| Critère | Believer 1960 (MakeFlyEasy) | Moose (Flightory) | Skywalker X8 | Ranger 2000 (Volantex) |
|---|---|---|---|---|
| Envergure | 1960 mm (R11) | 1600 mm (R01) | 2122 mm (R19, secondaire) | 2000 mm (R13) |
| Surface alaire | 51 à 51,4 dm² (R11, R12) | 36,5 dm² (R01) | 80 dm² (R19) | Non publiée |
| Allongement (b²/S) | 7,5 | 7,0 (6,9 selon le manuel) | 5,6 | n.d. |
| MTOW documentée | 5,5 kg (R11, R12) | 4,5 kg (R01) | Non trouvée en source primaire | Non publiée ; environ 1,1 kg sans batterie |
| Propulsion d'origine | 2 × 2814 (R12) | 2 × 28XX (R01) | 1 moteur propulsif | 1 moteur 28 mm ≥ 150 W, 3S 2200 mAh |
| Soute charge utile | 120 × 150 × 119 mm (R12) | 140 × 118 × 90 mm (R01) | n.d. | n.d. |
| Essai avec appareil plein format | Sony A7R II, 670 g (R12, vendeur) | Non | Non | Non |
| Récupération prévue | Lancement main, parachute (R12) | Patins TPU en option (R01) | n.d. | n.d. |
| Matériau | EPO, EVA, carbone (R11) | LW-PLA/ASA + PC/PETG imprimés (R01) | EPP/EPO (non vérifié) | EPO, fuselage plastique soufflé |
| Licence | Produit commercial | **Usage institutionnel interdit sans licence** (R02) | Produit commercial | Produit commercial |
| Prix relevé le 2026-10-19 | 549,99 USD (GetFPV) ou 398,70 USD (rcdrone), **en rupture** | Fichiers à 39,99 USD | Non relevé | 91,99 USD |

### 1.2 Résultats du modèle v0.1 (cas nominal, vent de 5 m/s)

Batterie minimale satisfaisant l'énergie, la réserve de 30 % et la MTOW, choisie dans la liste Li-ion P45B de 6S2P à 6S8P et LiPo 6S de 16 000 mAh. Les masses des cellules fixes incluent un système de parachute estimé à 0,2 kg :

| Acquisition | Believer | Moose | X8 |
|---|---|---|---|
| 0 min | 6S2P, 3,54 kg | 6S2P, 3,14 kg | 6S3P, 4,21 kg |
| 15 min | 6S3P, 4,01 kg | 6S3P, 3,61 kg | 6S4P, 4,67 kg |
| 30 min | 6S4P, 4,47 kg (81 % MTOW), marge 11 Wh | 6S4P, 4,07 kg (90 % MTOW) | 6S6P, 5,59 kg |
| 45 min | 6S5P, 4,93 kg (90 % MTOW), marge 3 Wh | Aucune | 6S8P, 6,52 kg |
| 60 min | Aucune | Aucune | Aucune |

**Réserve d'interprétation pour le X8.** Le modèle applique le même CD0 à toutes les cellules. Une aile volante sans fuselage ni empennage a probablement un CD0 plus faible, mais je n'ai pas de donnée pour le chiffrer. Le résultat défavorable au X8 vient donc en partie de l'hypothèse et ne constitue pas une conclusion.

### 1.3 Décision de short-list

- **Believer 1960 : retenue comme base du prototype A.** C'est la seule cellule qui combine une MTOW documentée offrant de la marge (81 % de charge à la mission de référence), une soute qui loge la caméra avec objectif (42,5 + 37 = 79,5 mm de hauteur pour 119 mm disponibles), un essai vendeur avec un appareil plein format plus lourd que le nôtre, et une récupération par parachute prévue par le constructeur.
  - Points ouverts : la masse à vide, le CG, la disponibilité (rupture de stock chez deux revendeurs) et la tenue de l'EPO au soleil.
  - Contrôle indépendant : à 4,5 kg, 20 m/s et au niveau de la mer, le modèle nominal donne 3,29 Wh/km. L'essai vendeur (environ 90 km avec 355 Wh) correspond à 3,2 à 3,9 Wh/km, selon l'énergie réellement consommée. Les deux ordres de grandeur concordent, mais les conditions de l'essai vendeur ne sont pas publiées.
- **Moose : exclu à ce stade (D-03).** Il y a deux raisons :
  - la licence interdit l'usage institutionnel ;
  - la marge de masse est faible : 90 % de la MTOW à 30 minutes d'acquisition, sur une masse sèche hypothétique, et aucune configuration au-delà.

  Il redevient candidat si Flightory accorde une licence. Sa structure imprimée exigerait alors les essais STR-03.
- **Skywalker X8 : non conclu.** Données primaires insuffisantes (MTOW, masse à vide). À réévaluer si une fiche constructeur est obtenue. Sa forme d'aile volante est favorable à l'atterrissage sur le ventre et au lancement par catapulte.
- **Ranger 2000 : éliminé.** C'est un planeur d'environ 1,1 kg sans batterie, prévu pour un pack d'environ 24 Wh (3S 2200 mAh) et un moteur d'environ 150 W. La charge utile de 500 g et la batterie nécessaire (> 250 Wh) le placent hors de son enveloppe d'un facteur supérieur à 2 en masse. Il est possible que vous ayez voulu désigner le **Ranger EX 757-3** (1980 mm), une autre cellule. La PX4 documente sa conversion QuadPlane à environ 4,5 kg au total (R14), mais je n'ai pas de MTOW publiée.

## 2. Architectures VTOL

| Critère | QuadPlane (rotors de sustentation séparés) | Tiltrotor | Tailsitter |
|---|---|---|---|
| Principe | 4 ou 8 rotors verticaux fixes + 1 moteur de croisière | Rotors basculant entre sustentation et propulsion | L'appareil entier pivote de 90° |
| Masse « morte » en croisière | Élevée (rotors, bras, ESC inactifs) | Moyenne (mécanismes de basculement) | Faible |
| Traînée en croisière | Pénalité de bras et d'hélices arrêtées (H13 : ΔCD0 de 0,003 à 0,012) | Moindre | Minimale |
| Commande en transition | La plus simple : sustentation et propulsion découplées | Couplée à l'angle de basculement ; servos de basculement critiques | Grand angle d'attaque en transition, sensible au vent |
| Modes de panne | Perte du moteur de croisière : retour en stationnaire possible si l'énergie le permet. Perte d'un rotor en quad : pas de tolérance. | Panne de basculement possible en configuration intermédiaire, sans issue simple | Atterrissage sur la queue sensible au vent, risque de basculement au sol |
| Caméra au nadir | Orientation fixe, pas d'impact | Pas d'impact | La caméra change d'orientation de 90° entre les phases ; intégration plus difficile |
| Support ArduPilot | Natif (R16, R17) | Natif (paramètres Q_TILT_*, R17) | Mentionné (R16) |
| Maintenance | Plus de moteurs, mais pas de mécanisme | Mécanismes à jeu et à usure | La plus simple mécaniquement |

**ADR-001 : le QuadPlane est retenu comme architecture du prototype B**, pour trois raisons :

1. Les transitions y sont les plus simples à rendre sûres, puisque la sustentation reste indépendante de la vitesse air tant que la transition n'est pas terminée.
2. Ses modes de panne sont les plus découplés.
3. La caméra reste au nadir sans compromis.

Son coût est connu et quantifié dans le Dossier 05 : une masse et une traînée supplémentaires en croisière. Pour une équipe qui construit son premier VTOL, la simplicité de commande et d'essai l'emporte sur le gain énergétique du tiltrotor. Cette décision est réversible si le Dossier 06 montre que l'énergie est le facteur limitant.

**Tolérance à la perte d'un rotor.** En configuration quad à quatre rotors, la perte d'un rotor en stationnaire n'est pas récupérable avec les lois de commande standard. C'est une propriété du multirotor quadri à pas fixe. Une configuration octo-quad (8 rotors, citée en R16) offre une redondance, au prix d'une masse et d'une complexité plus élevées. Cet arbitrage est à chiffrer en Phase 3.

## 3. Cellules VTOL candidates

| Critère | MakeFlyEasy Fighter VTOL | Believer convertie en QuadPlane |
|---|---|---|
| Envergure / surface | 2430 mm / 72,5 dm² (R18) | 1960 mm / 51 dm² |
| MTOW | 11,5 kg (R18) | 5,5 kg (cellule d'origine) |
| Charge utile max | 2,5 kg (R18) | n.d. |
| Soute | 280 × 160 × 110 mm (R18) | 120 × 150 × 119 mm |
| Portée annoncée | Jusqu'à 150 km avec 600 g (R18) | n.d. |
| Résultat du modèle (nominal, 5 m/s, 30 min) | **6S8P, 8,12 kg, marge 13 Wh** | **Aucune configuration faisable, même sans acquisition** |

- **Believer QuadPlane : éliminée.** Avec la masse du système VTOL (H07 adaptée : +1,2 à 1,4 kg), la MTOW de 5,5 kg ne laisse pas assez de batterie pour la mission, quel que soit le scénario d'acquisition en cas nominal.
- **Fighter VTOL : retenue comme base du prototype B**, avec deux réserves :
  - la masse sèche réelle (H07) est inconnue et pèse fortement sur le résultat (amplitude de 132 Wh) ;
  - la portée annoncée de 150 km n'est compatible avec le modèle que sous conditions favorables. Le modèle donne environ 4,7 Wh/km en palier sans vent à 8,1 kg et 1260 m par temps chaud (310 W à 18,3 m/s). 150 km demanderaient donc environ 700 Wh consommés, sans réserve, soit plus que l'énergie utilisable d'un 6S8P (661 Wh). La valeur du constructeur suppose vraisemblablement une batterie plus grosse, le niveau de la mer, pas de vent et pas de réserve. Il faut obtenir la configuration de l'essai.

## 4. Ce qui reste à rechercher

- Fiches constructeur MakeFlyEasy : masses à vide, CG et motorisation recommandée pour la Believer et le Fighter VTOL.
- Données de poussée des moteurs de sustentation de classe 4 à 5 kgf par rotor en 6S. Le modèle exige 4,31 kgf par rotor en équivalent niveau de la mer pour un rapport poussée/poids de 1,8. Le MN4014 consulté (R20) plafonne vers 1,9 à 2,6 kg et est donc insuffisant.
- Autres cellules VTOL commerciales de la même classe, pour élargir la comparaison au-delà de MakeFlyEasy.
