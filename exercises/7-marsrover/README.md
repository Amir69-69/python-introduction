 ## 🎳 Description du problème
Le programme doit recevoir en entrée :
- Le point de départ du rover : coordonnées (x, y) et direction initiale (N, S, E, W)
- Une carte décrivant les obstacles présents
- Une liste de commandes pour déplacer et orienter le rover :
- ⬆️ : avancer d’une case
- ➡️ : tourner à droite de 90°
- ⬅️ : tourner à gauche de 90

---
## 🧱 Comportement en cas d'obstacle :
Si le rover rencontre un obstacle, il ne fait rien et ignore cette commande.

## 🗺️ Exemple de carte

```
🟩🟩🌳🟩🟩
🟩🟩🟩🟩🟩
🟩🟩🟩🌳🟩
🟩🌳🟩🟩🟩
➡️🟩🟩🟩🟩
```

## 🖨️ Instruction supplémentaire
Avant d’implémenter le déplacement du Rover, implementer  un affichage (print) de la carte pour visualiser l’environnement.

## 💧 Bonus : capteur d’eau
Le Rover est équipé d’un capteur d’eau qui vérifie s’il y a de l’eau sur la case cible à chaque déplacement.
⚠️ Ce capteur n’est pas accessible depuis notre machine lors des tests unitaires ou d’intégration.


