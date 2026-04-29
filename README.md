# Text Analysis Service

## Objectif

Créer un microservice backend capable de recevoir un texte et de renvoyer une analyse simple.

La première version de l’API renvoie :

* le nombre de mots,
* les mots détectés.

Ce service servira ensuite de base pour analyser des CV ou d’autres contenus textuels.

---

## Stack utilisée

* Python
* FastAPI
* Uvicorn

---

## Lancer le projet

Activer l’environnement virtuel :

```bash id="m1q7vn"
source venv/bin/activate
```

Lancer le serveur :

```bash id="f8r2kt"
uvicorn main:app --reload
```

Documentation interactive :

```text id="v6n3px"
http://127.0.0.1:8000/docs
```

---

## Endpoint actuel

### POST `/analyze`

Exemple :

```json id="u9k4zr"
{
  "text": "Python Docker API"
}
```

Réponse :

```json id="x2m8lc"
{
  "word_count": 3,
  "keywords": ["python", "docker", "api"]
}
```

---

## Prochaines étapes

* filtrer les mots inutiles,
* calculer un score,
* séparer le code en modules,
* ajouter Docker,
* versionner avec Git.

## Actions du système

analyse brute du texte ✔️
détection de structure CV ✔️
détection de compétences ✔️
détection de verbes d’action ✔️
génération de recommandations conditionnelles ✔️
API stable ✔️

ingestion PDF ✔️
nettoyage ✔️
extraction features ✔️
scoring ✔️
suggestion engine ✔️

