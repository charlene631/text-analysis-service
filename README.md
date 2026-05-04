# Text Analysis Service

Microservice FastAPI open source pour analyser des documents textuels.

La première spécialisation du projet est l’analyse de CV au format PDF. Le service extrait le texte, le normalise, détecte des éléments clés, calcule plusieurs scores et retourne une réponse prête à être utilisée par un frontend React.

## Fonctionnalités actuelles

- Upload de CV au format PDF
- Extraction du texte avec `pypdf`
- Nettoyage et normalisation du texte
- Détection des sections clés
- Détection des compétences techniques
- Détection de verbes d’action
- Scoring multi-axes
- Validation du type de fichier PDF
- Limite de taille d’upload
- Gestion des PDF vides ou illisibles
- Réponse API structurée pour dashboard frontend
- Endpoint expérimental pour analyse de contenu LinkedIn

## Stack

### Backend

- Python 3.8
- FastAPI
- Pydantic
- Uvicorn
- pypdf
- python-dotenv
- pytest

### Frontend

- React
- Vite

## Architecture backend

```text
app/
├── core/
│   └── config.py
├── data/
│   ├── action_verbs.py
│   ├── sections.py
│   └── skills.py
├── routes/
│   └── analysis.py
├── schemas/
│   └── analysis_schema.py
├── services/
│   ├── cv_analyzer.py
│   ├── linkedin_analyzer.py
│   ├── pdf_extractor.py
│   ├── scoring.py
│   └── text_normalizer.py
└── main.py
```

## Installation backend

Depuis la racine du projet :

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Créer un fichier `.env` à la racine du projet :

```env
FRONTEND_URL=http://localhost:5173
```

Ne jamais commiter un fichier `.env` contenant des secrets. Pour un projet open source, préférer un fichier `.env.example`.

## Lancer le backend

```bash
source venv/bin/activate
uvicorn main:app --reload
```

Documentation interactive :

```text
http://127.0.0.1:8000/docs
```

## Lancer le frontend

Depuis le dossier `frontend` :

```bash
npm install
npm run dev
```

URL par défaut :

```text
http://localhost:5173
```

## Lancer le projet avec Docker

Le projet peut être lancé avec Docker Compose afin de démarrer le backend FastAPI et le frontend React avec une seule commande.

### Prérequis

- Docker
- Docker Compose

### Démarrage

Depuis la racine du projet :

```bash
docker compose up --build
```

Une fois les containers lancés :

```text
Frontend : http://localhost:5173
Backend  : http://localhost:8000
Swagger  : http://localhost:8000/docs
```

### Arrêter les containers

Dans le terminal où Docker Compose est lancé :

```bash
Ctrl + C
```

Ou depuis la racine du projet :

```bash
docker compose down
```

### Vérifier les containers actifs

```bash
docker compose ps
```

Ou :

```bash
docker ps
```

### Notes de développement

Docker est utilisé ici pour fournir un environnement de développement reproductible.

Le code reste modifiable localement dans VS Code. Les volumes Docker permettent de refléter les changements du code dans les containers pendant le développement.

Les fichiers `.env`, les environnements virtuels Python, les dépendances locales et les dossiers de build ne doivent pas être copiés dans les images Docker. Ils sont exclus via `.dockerignore`.

### Variables d’environnement Docker

Le `docker-compose.yml` configure les variables nécessaires au développement local :

```yaml
FRONTEND_URL=http://localhost:5173
VITE_API_URL=http://localhost:8000
```
## Endpoints

### Health check

```http
GET /
```

Réponse :

```json
{
  "status": "ok",
  "service": "Text Analysis Service",
  "version": "0.1.0"
}
```

### Analyse CV PDF

```http
POST /analyze/cv/pdf
```

Body : fichier PDF via `multipart/form-data`.

Réponse exemple :

```json
{
  "summary": {
    "global_score": 72,
    "structure_score": 75,
    "skills_score": 80,
    "action_score": 60
  },
  "analysis": {
    "sections_found": ["experience", "formation", "competences"],
    "skills_found": ["python", "fastapi", "react"],
    "action_verbs_found": ["developp", "cre", "deploy"]
  },
  "insights": [
    "CV bien structuré et pertinent."
  ],
  "meta": {
    "type": "cv",
    "length": 2450,
    "word_count": 380
  }
}
```

### Analyse LinkedIn PDF

```http
POST /analyze/linkedin/pdf
```

Body : fichier PDF via `multipart/form-data`.

## Tests

Lancer les tests backend depuis la racine du projet :

```bash
source venv/bin/activate
PYTHONPATH=. pytest
```

Statut actuel :

```text
8 passed
```

## Roadmap

### Court terme

- Ajouter un endpoint `/health`
- Ajouter des tests sur les routes FastAPI
- Améliorer la détection des compétences
- Réduire les faux positifs sur les mots-clés
- Ajouter une analyse de texte brut, sans PDF

### Moyen terme

- Ajouter une analyse plus fine des expériences
- Ajouter un score de lisibilité
- Ajouter un score d’adéquation avec une offre d’emploi
- Ajouter une analyse de posts LinkedIn
- Ajouter Docker

### Long terme

- Ajouter authentification utilisateur
- Ajouter historique des analyses
- Ajouter dashboard SaaS
- Ajouter export PDF du rapport
- Ajouter base de données
