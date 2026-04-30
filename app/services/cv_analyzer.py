from app.data.action_verbs import ACTION_VERBS
from app.data.sections import CV_SECTIONS
from app.data.skills import SKILLS
from app.services.scoring import (
    compute_action_score,
    compute_global_score,
    compute_skills_score,
    compute_structure_score,
)
from app.services.text_normalizer import normalize_text
from typing import List


def analyze_base(text: str) -> dict:
    words = normalize_text(text).split()

    return {
        "length": len(text),
        "word_count": len(words),
        "keywords": words[:5],
    }


def detect_sections(text: str) -> dict:
    clean = normalize_text(text)
    found = [section for section in CV_SECTIONS if section in clean]

    return {
        "sections_found": found,
        "structure_score": compute_structure_score(len(found)),
    }


def detect_skills(text: str) -> dict:
    clean = normalize_text(text)

    skills_by_category = {}
    skills_found = []

    for category, skills in SKILLS.items():
        detected_skills = [skill for skill in skills if skill in clean]
        skills_by_category[category] = detected_skills
        skills_found.extend(detected_skills)

    return {
        "skills_found": skills_found,
        "skills_by_category": skills_by_category,
        "skills_count": len(skills_found),
        "skills_score": compute_skills_score(len(skills_found)),
    }


def detect_action_verbs(text: str) -> dict:
    clean = normalize_text(text)

    found = []

    for verb in ACTION_VERBS:
        if any(pattern in clean for pattern in verb["patterns"]):
            found.append(verb["label"])

    return {
        "action_verbs_found": found,
        "action_score": compute_action_score(len(found)),
    }


def generate_cv_suggestions(
    structure_score: int,
    skills_count: int,
    action_score: int,
) -> List[str]:
    suggestions = []

    if structure_score < 50:
        suggestions.append("Ajoutez des sections claires : expérience, compétences, formation.")

    if skills_count < 3:
        suggestions.append("Ajoutez davantage de compétences techniques visibles.")

    if action_score < 40:
        suggestions.append("Utilisez plus de verbes d’action pour valoriser vos expériences.")

    if not suggestions:
        suggestions.append("CV bien structuré et pertinent.")

    return suggestions


def analyze_cv(text: str) -> dict:
    base = analyze_base(text)
    structure = detect_sections(text)
    skills = detect_skills(text)
    actions = detect_action_verbs(text)

    global_score = compute_global_score(
        structure_score=structure["structure_score"],
        skills_score=skills["skills_score"],
        action_score=actions["action_score"],
    )

    suggestions = generate_cv_suggestions(
        structure_score=structure["structure_score"],
        skills_count=skills["skills_count"],
        action_score=actions["action_score"],
    )

    return {
        "summary": {
            "global_score": global_score,
            "structure_score": structure["structure_score"],
            "skills_score": skills["skills_score"],
            "action_score": actions["action_score"],
        },
        "analysis": {
            "sections_found": structure["sections_found"],
            "skills_found": skills["skills_found"],
            "skills_by_category": skills["skills_by_category"],
            "action_verbs_found": actions["action_verbs_found"],
        },
        "insights": suggestions,
        "meta": {
            "type": "cv",
            "length": base["length"],
            "word_count": base["word_count"],
        },
    }
