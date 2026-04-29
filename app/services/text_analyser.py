def analyze_base(text: str):
    words = text.split()
    return {
        "length": len(text),
        "word_count": len(words),
        "keywords": words[:5],
    }


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

def detect_sections(text: str):
    sections = ["experience", "formation", "skills", "compétences", "education"]

    lower = text.lower()

    found = [s for s in sections if s in lower]

    return {
        "sections_found": found,
        "structure_score": min(100, len(found) * 25)
    }

def detect_skills(text: str):
    skills = [
        "python", "fastapi", "sql", "docker",
        "git", "javascript", "react",
        "html", "css", "mysql", "mongodb"
    ]

    lower = text.lower()

    found = [skill for skill in skills if skill in lower]

    return {
        "skills_found": found,
        "skills_count": len(found)
    }

def detect_action_verbs(text: str):
    verbs = [
        "développé", "conçu", "créé", "géré",
        "piloté", "optimisé", "automatisé",
        "réalisé", "implémenté", "coordonné"
    ]

    lower = text.lower()

    found = [verb for verb in verbs if verb in lower]

    return {
        "action_verbs_found": found,
        "action_score": min(100, len(found) * 20)
    }

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

def compute_global_score(structure_score, skills_count, action_score):
    skills_score = min(100, skills_count * 20)

    global_score = (
        structure_score * 0.3 +
        skills_score * 0.4 +
        action_score * 0.3
    )

    return round(global_score)