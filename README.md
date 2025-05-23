# 🎯 Arctal

**Arctal** est un jeu de plateforme en 2D développé dans le cadre du module projet Transverse à l'EFREI. Le joueur incarne **Kherrow**, un aventurier capable de tirer des portails pour avancer dans sa quête à travers un monde sombre et mystérieux : l'Arctal.

---

## 🎮 À propos du projet

L'objectif principal était de :
- Développer un **jeu 2D en Python avec Pygame**
- Travailler en **équipe** avec Git et des sessions de codage collaboratif (Code With Me)
- Intégrer des notions de **trajectoires physiques** et une **interface graphique**

### 👥 Équipe

- Ethan Bourdais–Goupil  
- Arthur Morineaux  
- Melvin Chaigneau  
- Julie Sieux  
- Rémi Bouerie (a quitté le projet en début de semestre)

---

## 🕹️ Fonctionnalités du jeu

### Menu principal :
- **Jouer** : Choisissez parmi 3 chapitres en mode Histoire (avec dialogues) ou activez le **mode chronométré**
- **Tutoriel** : Un niveau d'entraînement pour apprendre les touches et mécanismes
- **Paramètres** : Activer/désactiver la musique, l'aide à la visée, ou le mode chronométré
- **Skin** : Personnalisez votre personnage avec 4 tenues différentes
- **Classé** : Affiche le **leaderboard** des 5 meilleurs temps
- **Aide** : Rappel des fonctionnalités principales
- **Quitter** : Ferme le jeu (bouton visible sur toutes les pages sauf en jeu)

---

## 🧭 Comment jouer

- **Déplacement** : `Q` (gauche), `D` (droite)  
- **Sauter** : `ESPACE`  
- **Tirer une flèche** : clic souris  
- **Changer de portail (bleu/rose)** : `E`

⚠️ Pour vous téléporter, les deux portails doivent être placés, et la sortie doit être sécurisée (hors laser et hors murs).

### Mode Histoire :
- 3 chapitres à explorer, avec une **ambiance de plus en plus sombre**
- Dialogue automatique au début de chaque niveau (hors mode chronométré)
- Appuyez sur **n'importe quelle touche** pour passer au dialogue suivant

### Mode Chronométré :
- Entrez votre **prénom**
- Jouez tous les niveaux à la suite
- Votre **temps est enregistré** et peut apparaître dans le leaderboard

---

## 📖 Scénario

Vous incarnez **Kherrow**, un jeune aventurier dont le père a été capturé par **Necros**, un être maléfique avide de pouvoir. À travers les portails, vous devrez résoudre des énigmes, éviter des pièges et **vaincre l'obscurité de l'Arctal** pour retrouver votre père.

---

## 🧩 Structure du code

Le projet est divisé en **16 modules**, ainsi que de nombreux **assets** :

| Module              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `main`              | Gère le lancement du jeu et la navigation entre les fenêtres                |
| `skin_manager`      | Gère l'apparence du joueur                                                  |
| `level_selection`   | Permet de choisir le chapitre/niveau                                        |
| `leader_menu`       | Affiche le classement des meilleurs temps                                   |
| `bow`               | Gère l'arc et la trajectoire des flèches                                    |
| `chrono`            | Chronomètre et enregistrement des scores                                    |
| `equation_trajectory` | Contient les équations physiques utilisées pour les trajectoires           |
| `game`              | Mécaniques de jeu : déplacement, tir, téléportation                         |
| `map`               | Gestion et affichage des niveaux via des tuiles                             |
| `menu`              | Menu principal et boutons                                                   |
| `movie_manager`     | Gestion des cinématiques en images                                          |
| `player`            | Déplacement, collision et animation du joueur                               |
| `portal`            | Création et fonctionnement des portails                                     |
| `settings`          | Affichage et modification des paramètres                                    |
| `story_functions`   | Affichage des dialogues et transitions de l'histoire                        |
| `sound_manager`     | Sons de fond, musiques, bruitages                                           |

---

## 💻 Technologies utilisées

- **Python 3**
- **Pygame**
- **PyCharm** (environnement de développement)
- **Git** / **GitHub**
- **Code With Me** pour la collaboration

---

## 📂 Lancer le jeu

```bash
# Cloner le repository
git clone https://github.com/Didros75/ProjetTransverse

# Lancer le jeu
Ecrire la commande pip install pygame dans la console.
Lancer le jeu en appuyant sur la flèche verte en haut de l'écran.