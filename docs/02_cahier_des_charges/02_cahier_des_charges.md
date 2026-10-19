# Dossier 02 : Cahier des charges

Version 0.2, 19 octobre 2026. Statut : provisoire. Révision v0.2 : MIS-02 porté à 2 h de vol avec 30 % de réserve (voir le Dossier 03b). Les exigences notées **P** dépendent des décisions D-01 à D-05 (`registres/decisions.csv`).

Méthodes de vérification : **A** Analyse, **E** Essai, **I** Inspection, **D** Démonstration en vol.

## 1. Paramètres qui conditionnent réellement la conception

Le modèle v0.1 classe les paramètres par leur effet sur la marge énergétique de la mission de référence (`calc/out/sensibilite.csv`). Pour le prototype A (Believer, 6S4P), l'amplitude est l'écart de marge entre les bornes basse et haute de chaque paramètre :

1. Durée d'acquisition (15 à 60 min) : 190 Wh d'amplitude.
2. Rendement propulsif global (0,57 à 0,40) : 111 Wh.
3. CD0 (0,030 à 0,050) : 94 Wh.
4. Vent moyen (0 à 10 m/s) : 83 Wh.
5. Énergie utilisable de la batterie (0,90 à 0,75) : 58 Wh.

La masse sèche (25 Wh) et le coefficient d'Oswald (18 Wh) pèsent beaucoup moins.

Conséquence : **la décision D-01, durée ou surface d'acquisition par sortie, est la donnée de conception la plus importante**, devant tout choix de composant. Viennent ensuite deux mesures à obtenir tôt par essai : le rendement propulsif et la traînée de la cellule.

## 2. Définitions

- **Altitude du terrain** : 960 m AMSL au site de décollage de référence (donnée utilisateur).
- **Hauteur AGL** : hauteur au-dessus du sol survolé. Sur relief, elle varie le long de la ligne de vol si l'altitude AMSL est constante (voir PL-06).
- **Mission de référence** : transit de 20 km aller, acquisition, transit de 20 km retour (hypothèse D-01), vent moyen de 5 m/s de face à l'aller et arrière au retour, ISA+21 °C, croisière à 1260 m AMSL.

## 3. Exigences

| ID | Exigence | Valeur | Statut | Vérif. |
|---|---|---|---|---|
| MIS-01 | Rayon d'action en transit | 20 km aller + 20 km retour | P (D-01) | A, D |
| MIS-02 | Endurance | **2 h de vol avec 30 % de réserve** (révision du 2026-10-19) ; l'acquisition remplit le temps restant, soit environ 57 à 82 min | Confirmée (utilisateur) | A, D |
| MIS-03 | Réserve d'énergie à l'atterrissage | ≥ 30 % de l'énergie utilisable | Confirmée | A, E (journaux) |
| MIS-04 | Hauteur maximale | 1000 m AGL ; altitude de site 960 m AMSL | Confirmée | A, D |
| MIS-05 | Conditions atmosphériques de dimensionnement | Jusqu'à ISA+21 °C (30 °C au sol) | P | A |
| MIS-06 | Vent moyen admissible pour la mission de référence | 8 m/s (cible), à arbitrer avec MIS-02 | P | A, D |
| MIS-07 | Vitesse de décrochage en configuration d'acquisition | V_acq ≥ 1,3 Vs à la masse et la densité du vol | Confirmée | A, E |
| PL-01 | Charge utile | ILX-LR1 + objectif + support + câblage ≤ 500 g | Confirmée | I (pesée) |
| PL-02 | Résolution au sol | 3 cm/px (hypothèse D-02) | P | A, D |
| PL-03 | Flou de bougé | ≤ 0,5 px à la vitesse d'acquisition | Proposée | A, D |
| PL-04 | Déclenchement | Via le terminal Power and Control : FOCUS puis TRIGGER, en collecteur ouvert | Confirmée (R08) | E (banc) |
| PL-05 | Retour d'exposition | Signal EXPOSURE horodaté par l'autopilote pour chaque image | Confirmée | E, D |
| PL-06 | Recouvrements | Ortho 80/70 % ; 3D 80/80 %, à garantir au point le plus haut du terrain | P (D-02) | A |
| PL-07 | Alimentation caméra | 12 V régulés (plage 10 à 18 V), protégée | Confirmée | E |
| PL-08 | Température caméra | Habitacle ≤ 50 °C en fonctionnement (spécification 0 à 50 °C, R09) | Confirmée | E (thermocouple) |
| NAV-01 | Autopilote | ArduPilot Plane, CUAV X7+ Pro existant | Proposée (ADR-003) | I |
| NAV-02 | Capteur de vitesse air | Obligatoire (transitions VTOL, protection décrochage) | Confirmée | E |
| NAV-03 | Géoréférencement | Points de contrôle au sol obligatoires en validation ; PPK en phase 2 | P (D-02) | D |
| COM-01 | Liaison C2 et télémétrie | Couverture à 20 km avec marge de bilan de liaison ≥ 10 dB en visibilité directe | Proposée | A, E |
| COM-02 | Conformité radio | Bande et puissance autorisées par l'ARPTC | Confirmée | I (autorisation écrite) |
| COM-03 | Perte de liaison | Retour automatique, puis atterrissage ou parachute selon la configuration | Confirmée | E (SITL), D |
| PWR-01 | Alimentation de l'autopilote | Deux sources de modes de panne indépendants | Proposée | A, E |
| PWR-02 | Servos et radio | Rails d'alimentation dédiés, distincts de l'autopilote | Confirmée (A12, A13) | E |
| STR-01 | Charges de calcul en vol | +3,8 g limite, coefficient 1,5 pour la charge extrême | Proposée | A, E |
| STR-02 | Charges de lancement (A) | Fixations batterie et caméra dimensionnées pour l'accélération de crête de la catapulte retenue | Confirmée | A, E (accéléromètre) |
| STR-03 | Matériaux | Toute pièce structurelle imprimée doit avoir des données matériau et un essai à 55 °C | Proposée | E |
| OPS-01 | Lancement et récupération | Sans piste ; surface disponible à définir | P (D-04) | D |
| OPS-02 | Mise en œuvre | De l'arrivée au décollage en ≤ 20 min par 2 personnes | Proposée | D |
| MNT-01 | Réparabilité terrain | Pièces de rechange critiques en stock ; réparation d'une aile ou d'un rotor en < 1 h | Proposée | D |
| REG-01 | Autorisation aéronautique | Autorisation préalable de l'AAC RDC avant tout vol | Confirmée (R26, source secondaire) | I |
| REG-02 | Aire protégée | Accord du gestionnaire du parc, sans valeur d'autorisation aéronautique | Confirmée | I |
| SAF-01 | Limites d'exploitation | Refus de vol au-delà des limites vent, température ou batterie définies en Phase 3 | Proposée | I |
| ECO-01 | Budget | Plafond à définir | P (D-05) | A |

## 4. Remarques de conception sur les exigences

**MIS-06 contre MIS-02.** Avec le prototype A et un pack 6S4P, la mission de référence passe à 5 m/s de vent (+11 Wh) et échoue à 8 m/s (−22 Wh). Tenir 8 m/s avec 30 minutes d'acquisition demande un 6S5P, soit 4,93 kg (90 % de la MTOW vendeur, marge de 39 Wh), ou une réduction de l'acquisition. C'est un arbitrage à faire, pas une évidence.

**STR-01.** Le facteur +3,8 g correspond à la catégorie normale de l'aviation légère et sert ici de référence prudente pour un petit UAV. Ce n'est pas une exigence réglementaire RDC.

**STR-02.** Les accélérations de crête du lancement (environ 5 à 10 g selon la course de 4 à 2 m, voir le Dossier 04) dépassent les charges de vol. Pour le prototype A, ce sont elles qui dimensionnent les fixations.

**PL-08.** La limite de 50 °C de la caméra est plus contraignante qu'il n'y paraît dans une soute fermée en mousse exposée au soleil en zone tropicale. À mesurer au sol avant tout vol.
