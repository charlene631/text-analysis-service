from pypdf import PdfReader
from io import BytesIO
import re


# -------------------------
# CORE NORMALISATION
# -------------------------
def normalize(text: str):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    return text


# -------------------------
# BASE ANALYSIS
# -------------------------
def analyze_base(text: str):
    words = normalize(text).split()
    return {
        "length": len(text),
        "word_count": len(words),
        "keywords": words[:5],
    }


# -------------------------
# CV ANALYSIS
# -------------------------
def analyze_cv(text: str):
    base = analyze_base(text)
    structure = detect_sections(text)
    skills = detect_skills(text)
    actions = detect_action_verbs(text)

    suggestions = generate_cv_suggestions(
        structure["structure_score"],
        skills["skills_count"],
        actions["action_score"]
    )

    global_score = compute_global_score(
        structure["structure_score"],
        skills["skills_count"],
        actions["action_score"]
    )

    return {
        **base,
        **structure,
        **skills,
        **actions,
        "type": "cv",
        "clarity_score": min(100, len(text.split()) * 2),
        "suggestions": suggestions,
        "global_score": global_score
    }


# -------------------------
# LINKEDIN ANALYSIS
# -------------------------
def analyze_linkedin(text: str):
    base = analyze_base(text)
    structure = detect_sections(text)
    skills = detect_skills(text)

    return {
        **base,
        **structure,
        **skills,
        "type": "linkedin",
        "tone_score": min(100, len(text.split()) * 1.5),
        "suggestions": [
            "Rendez votre pitch plus direct",
            "Ajoutez une phrase d’impact",
            "Mettez en avant vos résultats"
        ]
    }


# -------------------------
# SECTIONS DETECTION
# -------------------------
def detect_sections(text: str):
    sections = [
        "experience", "experiences", "parcours",
        "formation", "formations",
        "competences", "compétences",
        "skills", "education", "profil"
    ]

    clean = normalize(text)

    found = [s for s in sections if s in clean]

    return {
        "sections_found": found,
        "structure_score": min(100, len(found) * 25)
    }


# -------------------------
# SKILLS DETECTION (élargie)
# -------------------------
def detect_skills(text: str):
    skills = [
        "python", "fastapi", "sql", "docker",
        "git", "javascript", "react",
        "html", "css", "mysql", "mongodb",
        "informatique", "reseau", "systeme",
        "support", "maintenance", "developpement",
        "linux", "api"
    ]

    clean = normalize(text)

    found = [skill for skill in skills if skill in clean]

    return {
        "skills_found": found,
        "skills_count": len(found)
    }


# -------------------------
# ACTION VERBS
# -------------------------
def detect_action_verbs(text: str):
    verbs = [
    "developp",   # capture développé / développement / developper
    "concep",     # conçu / conception
    "cre",        # créé / creation
    "ger",        # géré / gestion
    "pilot",      # pilotage
    "optimis",    # optimisation
    "realis",     # réalisé
    "implement",  # implémenté
    "deploy",     # déployé
    "adminis"
]

    clean = normalize(text)

    found = [verb for verb in verbs if verb in clean]

    return {
        "action_verbs_found": found,
        "action_score": min(100, len(found) * 20)
    }


# -------------------------
# SUGGESTIONS
# -------------------------
def generate_cv_suggestions(structure_score, skills_count, action_score):
    suggestions = []

    if structure_score < 50:
        suggestions.append("Ajoutez des sections claires (expérience, compétences, formation)")

    if skills_count < 3:
        suggestions.append("Ajoutez davantage de compétences techniques visibles")

    if action_score < 40:
        suggestions.append("Utilisez plus de verbes d’action pour valoriser vos expériences")

    if not suggestions:
        suggestions.append("CV bien structuré et pertinent")

    return suggestions


# -------------------------
# SCORE GLOBAL
# -------------------------
def compute_global_score(structure_score, skills_count, action_score):
    skills_score = min(100, skills_count * 20)

    global_score = (
        structure_score * 0.3 +
        skills_score * 0.4 +
        action_score * 0.3
    )

    return round(global_score)


# -------------------------
# PDF CLEANING
# -------------------------
def clean_pdf_text(text: str):
    # 1. enlève sauts de ligne
    text = text.replace("\n", " ")

    # 2. reconstruit mots espacés type "C O M P É T E N C E S"
    text = re.sub(r"(?:(?:\b\w\b\s+){3,})", lambda m: m.group(0).replace(" ", ""), text)

    # 3. normalise espaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# -------------------------
# PDF EXTRACTION
# -------------------------
def extract_text_from_pdf(file_bytes: bytes):
    reader = PdfReader(BytesIO(file_bytes))

    text = ""
    for page in reader.pages:
        page_text = page.extract_text() or ""
        text += page_text.replace("\n", " ")

    # IMPORTANT : on nettoie ici UNE SEULE FOIS
    return clean_pdf_text(text)