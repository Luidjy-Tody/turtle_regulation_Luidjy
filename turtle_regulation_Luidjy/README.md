# turtle_regulation_Luidjy

## Test de Kp

- Kp = 1 :
  la tortue tourne lentement et s’arrête avec un angle d’environ 30°.

- Kp = 2 :
  la tortue tourne plus vite que pour Kp = 1.
  Le mouvement est plus stable.
  L’angle observé est entre 30° et 40°.

- Kp = 20 :
  la tortue tourne très vite.
  Elle peut faire 360°.
  La vitesse diminue avec le temps, mais le mouvement n’est pas stable.

- Kp = 100 :
  la tortue tourne très vite et fait des rotations continues (360° puis -360° et ainsi de suite)
  Elle ne s’arrête plus.

- Kp choisi :

  Kp choisi : Kp entre 2 et 5, car cette plage permet d’obtenir un bon équilibre entre vitesse de réaction et stabilité du mouvement.

  Kp = 2, car il donne le meilleur compromis entre rapidité et stabilité.


## Test de différentes valeurs de Kpl

Nous avons testé plusieurs valeurs de Kpl pour observer le déplacement de la tortue vers le waypoint.

### Kpl = 0.5
Avec Kpl = 0.5, la tortue avance lentement.  
Le mouvement est plus doux, mais l’arrivée au waypoint prend plus de temps.

### Kpl = 1.0
Avec Kpl = 1.0, la tortue avance de manière correcte vers le waypoint.  
Le mouvement reste assez stable.

### Kpl = 3.0
Avec Kpl = 3.0, la tortue avance plus rapidement.  
Le déplacement est plus rapide qu’avec Kpl = 1.0, mais il faut vérifier la stabilité du mouvement.

### Kpl = 5.0
Avec Kpl = 5.0, la tortue avance très vite.  
Le mouvement devient plus difficile à contrôler et peut devenir moins stable.

### Kpl = 10.0
Avec Kpl = 10.0, le départ se fait normalement, mais ensuite la tortue continue son déplacement en contournant largement la zone et devient difficile à arrêter.  
Cette valeur est donc trop grande pour une bonne régulation en distance.

### Valeur choisie
La valeur choisie pour Kpl est comprise entre 1.0 et 3.0, car cette plage permet d’avoir un déplacement assez rapide tout en gardant un comportement plus stable.
