# Dossier 03b : Faisabilité d'une endurance de 2 h avec 30 % de réserve

Version 0.2, 19 octobre 2026. Exigence révisée par l'utilisateur : **2 h de vol en conservant 30 % de réserve** (MIS-02, entrée REQ-2026-10-19 du registre des décisions). Les résultats proviennent de `calc/out/endurance_2h.csv`, régénéré par `make calc`. Ce sont des estimations ; aucune n'est une mesure.

## 1. Ce que l'exigence implique physiquement

L'énergie utilisable doit couvrir 120 minutes de vol, puis rester à 70 % consommée seulement. L'énergie embarquée utile doit donc correspondre à **120 / 0,7 ≈ 171 minutes** de vol à la puissance de croisière.

Pour un avion électrique, l'endurance en palier suit au premier ordre une forme de Breguet électrique, sans auxiliaires :

$$t \approx \frac{e_{pack}\; f_b\; \eta\; (L/D)}{g\, V}$$

| Symbole | Signification | Valeur pour A (Believer, cas nominal) |
|---|---|---|
| $e_{pack}$ | Énergie massique du pack | 210 Wh/kg, soit 756 kJ/kg (P45B avec 10 % de surcoût pack) |
| $f_b$ | Fraction massique de batterie | 0,41 (1,85 kg sur 4,47 kg) |
| $\eta$ | Rendement propulsif global | 0,51 |
| $L/D$ | Finesse | 10,3 |
| $V$ | Vitesse air | 16,2 m/s |

Avec ces valeurs, t ≈ 171 min d'énergie brute. Après le coefficient d'utilisation de 0,85, la réserve de 30 % et environ 16 W d'auxiliaires, il reste environ 93 minutes de vol utilisable, ce que confirme le modèle complet. **Il manque un facteur d'environ 1,3** sur le produit $e_{pack} \cdot f_b \cdot \eta \cdot (L/D) / V$.

La formule montre les leviers, chacun agissant proportionnellement :

| Levier | Gain plausible | Coût ou risque |
|---|---|---|
| Finesse (CD0 de 0,040 à 0,030, allongement plus élevé) | +10 à 20 % | Cellule plus propre ou plus grande ; à mesurer en vol |
| Rendement propulsif (0,51 à 0,57) | environ +12 % | Hélice de grand diamètre adaptée au point de croisière, et non au décollage |
| Énergie massique (P45B 210 → P50B environ 237 → classe semi-solide environ 313 Wh/kg pack) | +13 % à +49 % | Coût, cycles (250 à 800, R30), courant admissible, disponibilité |
| Fraction de batterie | Limitée par la MTOW et la spirale de masse | Au-delà d'environ 0,5, la vitesse minimale et la puissance augmentent avec la masse |

## 2. Résultats (vent de 5 m/s, croisière à 1260 m AMSL et ISA+21 °C)

Batterie minimale satisfaisant 2 h et 30 % de réserve sous la MTOW. L'acquisition remplit le temps restant après la montée, le transit de 2 × 20 km et l'approche, soit **57 à 82 minutes d'acquisition par vol** selon la configuration.

| Cellule | Aérodynamique et propulsion | P45B (210 Wh/kg pack) | P50B (237 Wh/kg pack) | Semi-solide (≈313 Wh/kg pack, HYP) |
|---|---|---|---|---|
| **A : Believer 1960** (MTOW 5,5 kg) | Nominal (CD0 0,040, η 0,51) | Non faisable | Non faisable | 4,92 kg, 720 Wh |
| | Cellule propre (CD0 0,030) | 5,39 kg (98 % MTOW) | 4,90 kg | 4,15 kg |
| | Cellule propre + hélice optimisée (η 0,57) | 4,93 kg (90 % MTOW) | 4,90 kg | 4,15 kg |
| **Classe FW 2,6 m**, 80 dm² (HYP) | Nominal | 7,84 kg, 972 Wh | 6,86 kg | 5,52 kg |
| | Cellule propre + hélice optimisée | 5,99 kg, 583 Wh | 5,50 kg, 540 Wh | 4,75 kg, 480 Wh |
| **Classe FW 3,0 m**, 85 dm² (HYP) | Cellule propre + hélice optimisée | 6,39 kg | 5,90 kg | 5,15 kg |
| **B : Fighter VTOL** (MTOW 11,5 kg) | Nominal | Non faisable | Non faisable | 8,25 kg, 1200 Wh |
| | Cellule propre + hélice optimisée | Non faisable | 8,97 kg, 1080 Wh | **7,48 kg, 960 Wh** |
| **Classe VTOL 2,7 m**, géométrie DeltaQuad Evo | Cellule propre + hélice optimisée | Non faisable | Non faisable | 8,38 kg, 960 Wh |

**À 8 m/s de vent**, la Believer « propre » en P45B n'est plus faisable. Les solutions semi-solides et la classe 2,6 m tiennent, avec un échelon de batterie de plus dans certains cas. Le détail est dans le CSV.

## 3. Contrôle indépendant : le DeltaQuad Evo

Le DeltaQuad Evo (R28) donne un point de comparaison commercial pour le VTOL.

- **Données constructeur.** 2,69 m d'envergure, 84 dm², 4,8 kg à vide, MTOW de 10 kg. Le constructeur annonce **272 minutes** avec deux batteries Li-ion semi-solides 6S de 22 Ah (environ 2,0 kg chacune), pour une utilisation de 90 % de la batterie, un vent faible, au niveau de la mer, et une charge utile non précisée.
- **Puissance moyenne implicite.** En supposant 3,6 V par cellule (valeur non publiée), on obtient environ 2 × 475 Wh × 0,9 / 4,53 h ≈ **189 W**, soit environ 21 W/kg à environ 9 kg.
- **Modèle de ce dossier.** Pour la classe 2,7 m « propre + hélice optimisée », le modèle donne 230 W à 8,38 kg, à 1260 m et ISA+21 °C. Ramenés au niveau de la mer à coefficient de portance constant (P ∝ 1/√ρ), cela fait environ **209 W**. L'écart est de l'ordre de 10 %, cohérent avec un constructeur qui annonce des conditions favorables.
- **Enseignement principal.** Le pack DeltaQuad implicite représente environ 240 Wh/kg, et non 313 Wh/kg. Son endurance vient d'abord de **l'efficacité aérodynamique et propulsive** (aile volante VTOL optimisée), puis de la densité d'énergie. Avec une cellule commerciale dont la traînée et l'hélice ne sont pas optimisées, nos chiffres « nominaux » montrent que 2 h ne sont pas atteignables en VTOL.

Le Trinity Pro (R29) annonce 90 minutes pour une MTOW de 5,75 kg et 1 kg de charge utile, soit 1,5 h à 5,75 kg. Il confirme que **2 h et 30 % de réserve dépassent ce que font les VTOL commerciaux de la classe 5 à 6 kg**. La classe 8 à 10 kg (DeltaQuad Evo) y parvient.

Le mémoire Chalmers (R31) illustre le risque inverse : un FW de 2,8 m conçu en interne est arrivé à une finesse de 6,9 et 54 minutes calculées, à cause de la traînée du fuselage. **La finesse réelle d'une cellule non optimisée est la principale cause d'échec documentée.**

## 4. Conclusions

1. **L'objectif de 2 h avec 30 % de réserve est atteignable en Fixed Wing**, à condition d'obtenir une cellule propre (CD0 ≤ 0,030) et un groupe propulseur optimisé pour la croisière. La masse au décollage est alors de 5 à 6 kg en Li-ion P45B ou P50B, ou d'environ 4,2 à 4,8 kg avec des cellules haute énergie.
2. **La Believer devient limite.** Elle n'atteint l'objectif que si sa traînée réelle est basse, et alors à 90 % ou plus de sa MTOW en Li-ion standard. Une cellule plus grande (2,4 à 3 m, allongement 8 à 10) est plus robuste vis-à-vis de l'incertitude (D-07).
3. **Le VTOL n'atteint 2 h qu'avec des cellules haute énergie ou une cellule optimisée.** La masse est alors de 7,5 à 9 kg, avec environ 1 kWh de batterie. Il faut vérifier le courant en stationnaire : avec un 6S4P semi-solide d'environ 44 Ah, environ 62 A en transition donnent environ 1,4 C par cellule, compatible avec les cellules « équilibrées » (4 à 6 C), mais pas avec certaines cellules « énergie » limitées à 1 à 2 C (R30).
4. **L'écart A/B se creuse** : environ 0,5 kWh de batterie pour A contre environ 1 kWh pour B. Cela pèse sur le coût des batteries, la charge sur le terrain et le transport.
5. **Les deux paramètres à mesurer en priorité restent le CD0 et le rendement propulsif** (H23, H24). Ce sont eux qui font passer la Believer de « non faisable » à « faisable ».

## 5. Décisions et actions

- **D-06** : accepter ou non des cellules haute énergie, avec leur coût, leur nombre de cycles, leur disponibilité en RDC et les contraintes de transport aérien des batteries Li-ion à vérifier.
- **D-07** : rechercher une cellule FW de 2,4 à 3 m optimisée pour l'endurance, et une cellule VTOL efficace en concurrence avec le Fighter.
- **Action P3-10, avancée en priorité** : une campagne d'identification de la polaire et du rendement propulsif sur une cellule disponible (Believer ou équivalent). Elle tranche le point 2 avant tout achat lourd.
