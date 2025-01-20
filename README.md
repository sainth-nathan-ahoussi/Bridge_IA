# Outil de Détection et Reconnaissance de Cartes de Bridge

## Introduction
Ce projet utilise un modèle d'apprentissage profond basé sur YOLOv8 pour détecter et reconnaître les cartes de bridge en temps réel à partir d'un flux vidéo. L'application est conçue pour analyser des séquences vidéo en direct, identifier les cartes présentes et enregistrer les résultats dans un fichier texte.

---

## Table des Matières
- [Introduction](#introduction)
- [Caractéristiques](#caractéristiques)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Configuration](#configuration)
- [Dépendances](#dépendances)
- [Exemples](#exemples)
- [Contributeurs](#contributeurs)
- [Licence](#licence)

---

## Caractéristiques
- **Détection en temps réel** : Utilise une caméra pour capturer et analyser les cartes.
- **Haute précision** : Filtrage des résultats en fonction de seuils de confiance configurables.
- **Validation par fréquence** : Seules les cartes détectées fréquemment (selon un seuil défini) sont enregistrées.
- **Compatibilité YOLOv8** : Basé sur un modèle YOLOv8 pour une performance optimale.

---

## Installation
### Prérequis
- Python 3.8 ou plus
- Une caméra connectée à votre machine

### Étapes d'installation
1. Clonez ce dépôt :
   ```bash
   git clone <URL_DU_DÉPÔT>
   cd <NOM_DU_DÉPÔT>
   ```
2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```
3. Téléchargez et placez le fichier de modèle `Bridge_IA.pt` dans le répertoire principal.

---

## Utilisation
1. Exécutez le script de détection :
   ```bash
   python detection.py
   ```
2. Les cartes détectées apparaîtront dans une fenêtre avec des annotations.
3. Les résultats validés seront sauvegardés dans le fichier `Sortie.txt`.

### Raccourcis :
- Appuyez sur `q` pour quitter le programme.

---

## Configuration
Le fichier `data.yaml` configure les classes des cartes et les chemins vers les ensembles de données :
- **Classes disponibles** : 77 classes de cartes et enchères spécifiques.
- **Seuils** :
  - Confiance minimale : 0.9
  - Fréquence minimale : 30 détections consécutives

Pour modifier ces paramètres, éditez les lignes correspondantes dans `detection.py`.

---

## Dépendances
- [YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV
- Python Libraries : `collections`, `time`

---

## Exemples
Exemple de sortie dans `Sortie.txt` :
```
Carte détectée : Roi_Coeur, Fréquence : 32, Confiance moyenne : 0.95
Carte détectée : As_Pique, Fréquence : 31, Confiance moyenne : 0.93
```

---

## Contributeurs
- **Nom du développeur** : AHOUSSI Sainth-Nathan
- **Contact** : https://www.linkedin.com/in/sainth-nathan-ahoussi-526412279/

---

## Licence
Ce projet est sous licence [CC BY 4.0](LICENSE).

---

## Remerciements
Merci aux ressources de [Roboflow](https://universe.roboflow.com/bridge-fr7ig/yolo_bridge) pour les ensembles de données utilisés dans ce projet.

### Points principaux :
1. Ce fichier est organisé pour fournir des informations complètes à l'utilisateur ou au contributeur.
2. Il décrit les étapes nécessaires pour utiliser l'outil, configure les seuils, et cite les dépendances.
3. Si vous avez d'autres éléments à inclure, comme des captures d'écran ou des détails spécifiques sur le modèle, faites-le-moi savoir !