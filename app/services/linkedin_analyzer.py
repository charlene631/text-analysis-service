from app.services.cv_analyzer import analyze_base, detect_sections, detect_skills
from app.services.scoring import compute_global_score


def analyze_linkedin(text: str) -> dict:
    base = analyze_base(text)
    structure = detect_sections(text)
    skills = detect_skills(text)

    action_score = 0

    global_score = compute_global_score(
        structure_score=structure["structure_score"],
        skills_score=skills["skills_score"],
        action_score=action_score,
    )

    return {
        "summary": {
            "global_score": global_score,
            "structure_score": structure["structure_score"],
            "skills_score": skills["skills_score"],
            "action_score": action_score,
        },
        "analysis": {
            "sections_found": structure["sections_found"],
            "skills_found": skills["skills_found"],
            "action_verbs_found": [],
        },
        "insights": [
            "Rendez votre pitch plus direct.",
            "Ajoutez une phrase d’impact.",
            "Mettez en avant vos résultats.",
        ],
        "meta": {
            "type": "linkedin",
            "length": base["length"],
            "word_count": base["word_count"],
        },
    }
