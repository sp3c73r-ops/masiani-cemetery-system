# Système de Cartographie et d'Identification des Sépultures du Cimetière de Masiani

## Installation

1. Créer le dossier du projet et se placer dedans.
2. Créer un environnement virtuel Python.
3. Installer les dépendances.
4. Lancer le serveur.

## Création de l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

## Installation des dépendances

```bash
pip install -r requirements.txt
```

## Lancement du serveur

```bash
uvicorn app.main:app --reload
```
