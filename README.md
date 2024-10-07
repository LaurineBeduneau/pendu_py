# Jeu du Pendu en Python avec Pygame

Ce projet est une implémentation du **Jeu du Pendu** (Hangman) en Python en utilisant la bibliothèque **Pygame**. Le but du jeu est de deviner un mot secret en sélectionnant des lettres une à une. Si le joueur fait trop d'erreurs, un stickman se fait progressivement dessiner sur l'écran.

## Fonctionnalités

- **Graphismes en Pygame** : Le jeu utilise Pygame pour dessiner le stickman et afficher l'état actuel du mot à deviner.
- **Sélection des lettres par clic** : Le joueur peut cliquer sur les lettres affichées à l'écran pour deviner le mot.
- **Gestion des erreurs** : Le jeu affiche un message en cas de victoire ou de défaite, en fonction du nombre d'erreurs commises.
- **Fond d'écran personnalisé** : Le jeu utilise une image de fond pour rendre l'interface plus attrayante.

## Prérequis

- Python 3.x
- Bibliothèque **Pygame**

## Installation

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/LaurineBeudneau/pendu_py.git

2. **Installer Pygame** : Si vous n'avez pas encore installé Pygame, vous pouvez le faire avec pip :

bash
```
pip install pygame
```

3. **Préparer les fichiers de ressources** :

Assurez-vous que l'image de fond (fond-vectoriel.jpg) et les fichiers Python nécessaires (comme task9.py) sont dans le répertoire du projet.

## Lancement du jeu

Pour lancer le jeu, exécutez simplement le script Python :

bash
```
python3 main.py
```
## Fichiers importants

- **main.py** : Le script principal qui initialise Pygame, gère les événements du jeu et dessine le stickman.
- **task9.py** : Le fichier contenant la logique du jeu (gestion des erreurs, vérification des victoires, etc.).
- **fond-vectoriel.jpg** : L'image de fond utilisée pour l'interface graphique du jeu (nommez l'image comme vous le souhaitez).

## Structure du projet

Voici la structure de base du projet :

bash
```
hangman-pygame/
│
├── main.py           # Script principal du jeu
├── task9.py             # Logique du jeu (gestion des erreurs, victoire/défaite, etc.)
├── fond-vectoriel.jpg    # Image de fond pour l'interface graphique
├── my_wordlist.txt       # Fichier contenant une liste de mots à deviner
└── README.md            
         
```

## Fonctionnement du jeu

Le joueur doit deviner un mot secret en cliquant sur les lettres de l'alphabet affichées à l'écran.
Chaque mauvaise réponse fait progresser le dessin du stickman.
Si le joueur devine correctement toutes les lettres avant que le stickman soit entièrement dessiné, il gagne.
Si le stickman est complètement dessiné avant que le mot soit découvert, le joueur perd.

## Améliorations possibles

- Ajout de niveaux : Vous pouvez ajouter des niveaux de difficulté avec des mots plus ou moins longs.
- Multijoueur : Implémenter une version multijoueur où les joueurs peuvent s'affronter pour deviner le mot plus rapidement.
- Utilisation de my_wordlist.txt : Modifier le code pour permettre au joueur de choisir un fichier de mots personnalisé pour améliorer l'expérience de jeu.
