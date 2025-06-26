*last update: 01/17/2025*

# Workshop 

Initiation à GamePy en plusieurs étapes

# 1. On cré un programme qui affiche un ecran blanc.

* Définition des paramètres de la fenètre d'affichage
* boucle principale: events et rendering

# 2. On implémente un personnage que nous pourrons déplacer.
* paramètres du personage
* gestion de input clavier
* gestion des events

+ paramètre du jeux: rafraichissment
+ gestion des collisions avec les bords de l'écran

* déportation du system de mouvement dans un module player.py

# 3. On ajoute un fond et un sprite à notre personnage

# 4 on ajoute l'animation du personnage, et un système de saut

* modification de player_system.py

# 5. Ajout d'un scrolling horizontal avec une caméra dynamique, et refactorisation des nouveaux systems.

* ajout de BGM: Main theme
* ajout de SFX: Jump fx

* modifications de main.py
* création de camera_system.py
* création de level_system.py
* création de render_system.py
* création de audio_system.py
* ajustement de player_system.py