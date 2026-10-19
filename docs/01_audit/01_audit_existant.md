# Dossier 01 : Audit de l'existant

Version 0.1, 19 octobre 2026. Objet audité : sortie Blueprint.io « Fixed-Wing Mapping Drone » (5 fichiers, référence R27), ainsi que mes propres affirmations de la revue précédente.

La matrice complète, avec 26 lignes, se trouve dans `matrice_audit.csv`. Ce document en donne la lecture technique et la synthèse.

## 1. Méthode

Chaque élément a été confronté à une source primaire lorsqu'elle existe (constructeur, documentation ArduPilot) et classé selon cinq niveaux de gravité :

- **Bloquant** : empêche le vol, la mission ou l'usage institutionnel.
- **Majeur** : faux ou non justifié, et doit être refait.
- **Modéré** : à justifier.
- **Mineur** : défaut de traçabilité.
- **Conforme.**

Les références (R01 à R27) sont dans `registres/references.csv`.

## 2. Verdict

La proposition Blueprint n'est pas une conception. Elle juxtapose des composants plausibles, sans bilan de masse, d'énergie, de centrage ni de charges, et contient quatre incohérences bloquantes vérifiées.

| Gravité | Nombre | Lignes |
|---|---|---|
| Bloquant | 6 | A01 cellule, A02 licence, A03 moteur, A10 LTE, A16 déclenchement, A23 documentation |
| Majeur | 13 | A05 à A09, A11 à A15, A17, A25, A26 |
| Modéré | 1 | A19 |
| Mineur | 6 | A04, A18, A20, A21, A22, A24 |

Rien de la nomenclature Blueprint n'est repris par défaut. Trois éléments sont conservés sur le principe, après vérification indépendante :

- la cellule Li-ion 21700 (R04) ;
- le régulateur 12 V de la caméra : il est nécessaire, car un pack 6S chargé atteint 25,2 V alors que l'ILX-LR1 accepte 10 à 18 V (R08) ;
- la présence d'un capteur de vitesse air et d'un capteur de courant.

## 3. Constats bloquants démontrés

**A01 Cellule.** Le manuel du Moose (R01) décrit deux moteurs 28XX tractifs sur l'aile, un empennage en V et quatre servos. Blueprint a modélisé un monomoteur dans le nez, avec empennage classique et tube de queue. Ses pièces imprimées ne correspondent à aucun fichier existant.

**A02 Licence.** La licence Flightory (R02, section 1) interdit explicitement l'usage institutionnel sans licence séparée. Un parc national opéré par une organisation relève de ce cas. Cela vaut pour toutes les cellules Flightory, et pas seulement pour le Moose.

**A03 Moteur.** T-Motor spécifie l'AT3520 KV850 pour 3 à 4S (R03). En 6S, le régime à vide atteint environ 850 × 25,2 V ≈ 21 400 tr/min sur pack chargé, contre environ 12 600 tr/min en 4S nominal. À hélice constante, la puissance absorbée croît approximativement comme le cube du régime, donc le moteur sortirait de son enveloppe de 1100 W sur 180 s.

**A10 LTE.** La documentation ArduPilot (R06) place le modem LTE sur un ordinateur compagnon de type Raspberry Pi CM4, pas sur l'autopilote. La clé USB branchée sur le Cube n'aurait aucune fonction.

**A16 Déclenchement.** Le connecteur Sony (R08) impose plusieurs conditions que l'interface Blueprint ne respecte pas :

- des entrées actives à l'état bas, pilotées en collecteur ou drain ouvert ;
- l'activation de FOCUS avant TRIGGER ;
- un 0 V commun entre l'appareil de commande et la broche 2 ;
- une sortie EXPOSURE en drain ouvert, qui demande un pull-up.

Sortir AUX1 directement vers la caméra ne satisfait aucune de ces conditions, et le retour d'exposition est absent. Sans ce retour, l'horodatage des images repose sur l'instant de commande et non sur l'instant d'exposition.

**A23 Documentation.** Les 18 étapes du guide sont marquées « not yet generated ». Il n'existe aucune note de calcul.

## 4. Points majeurs, avec le chiffrage du modèle v0.1

Les chiffres suivants sortent de `calc/model.py`, avec ses hypothèses (registre H01 à H20). Ce sont des estimations, pas des mesures.

**A06 Batterie.** Le pack 6S4P P45B (389 Wh nominaux, environ 330 Wh utilisables, environ 1,85 kg) n'est pas absurde. Pour la mission de référence, un transit de 2 × 20 km avec 30 minutes d'acquisition, sur Believer avec parachute, en cas nominal et avec un vent de 5 m/s, le besoin réserve comprise est de 320 Wh, soit une marge de 11 Wh. Mais ce pack n'est justifié par rien, et il devient insuffisant dès 8 m/s de vent (marge de −22 Wh).

**A09 Lancement.** Pour une Believer de 4,47 kg, à 960 m par 30 °C avec un CLmax de 1,1, la vitesse de décrochage vaut 12,3 m/s et la vitesse de lancement visée (1,25 Vs) 15,3 m/s. Une catapulte de 3 m impose alors 4,0 g en moyenne et environ 6,4 g en crête, avec l'hypothèse H20. Ces accélérations dimensionnent les fixations de la batterie (1,85 kg) et de la caméra.

**A09 Récupération.** L'énergie cinétique vaut environ 406 J en atterrissage sur le ventre à 1,1 Vs, contre environ 56 J sous parachute à 5 m/s.

**A11 et A12 Alimentation.** La documentation ArduPilot (R05) confirme que l'alimentation de 5,35 V sous 3 A vient d'un BEC Mauch attaché au capteur, et non du capteur lui-même. Le BEC Castle a une double fonction contradictoire.

**A13 et A14 Radio.** La variante RFD868x consomme environ 800 mA en crête sous 5 V à 500 mW (R23), ce qui justifie une alimentation dédiée. La bande 902 à 928 MHz n'a pas été vérifiée pour la RDC, et je n'ai trouvé aucune source primaire ARPTC en ligne. Il faut une demande écrite.

## 5. Auto-audit de ma revue précédente

| Affirmation précédente | Statut après vérification |
|---|---|
| « Chez Mauch, le 5,3 V vient d'un BEC séparé (à vérifier) » | **Confirmé** par R05 (5,35 V / 3 A via BEC LV ou HV attaché) |
| « Il existe une variante RFD 868 MHz (à confirmer) » | **Confirmé** : RFD868x-EU, 868 à 869 MHz, 500 mW (R23) |
| « Objectif de longueur ≤ 45 mm pour la soute du Moose » | **Confirmé** par le calcul : 90 mm (R01) − 42,5 mm (R07) = 47,5 mm, donc ≤ 45 mm laisse 2,5 mm de jeu. Ce point n'a plus d'objet si le Moose est exclu (A02). |
| « Masse d'environ 4,4 kg pour le Moose avec un 6S4P » | **Cohérent** : le modèle v0.1 donne 4,07 kg en nominal avec parachute, pour une masse sèche supposée de 1,2 kg. Mon estimation précédente supposait une cellule de 1,2 kg plus des composants Blueprint plus lourds (Cube avec carrier ADS-B, LTE, AT3520). |
| « Lancement à la main irréaliste à 4,4 kg » | **Nuancé** : le vendeur Believer annonce un lancement à la main (R12), sans préciser la masse. À 4,5 kg et 15 m/s de vitesse de lancement visée, je le considère comme non démontré, pas comme impossible. À tester à masse croissante. |

## 6. Informations manquantes

- Masses à vide documentées : Believer, Fighter VTOL et Moose.
- Polaires mesurées : aucune cellule candidate n'en publie.
- Données moteur-hélice au point de croisière : seules des données statiques sont publiées.
- Réglementation radio et aéronautique primaire de la RDC. Seule une source de presse secondaire a été consultée (R26).
- Spécification de la sortie EXPOSURE en délai par rapport à l'ouverture réelle : le chronogramme est publié en image, non extrait.
- Prix courants et disponibilités. Plusieurs articles sont en rupture : Believer, RFD868x.
