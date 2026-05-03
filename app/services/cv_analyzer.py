from app.data.action_verbs import ACTION_VERBS
from app.data.sections import CV_SECTIONS
from app.data.skills import SKILLS
from app.services.scoring import (
    compute_action_score,
    compute_global_score,
    compute_skills_score,
    compute_structure_score,
)
from app.services.text_normalizer import normalize_text, remove_accents
from typing import List
import re


def analyze_base(text: str) -> dict:
    words = normalize_text(text).split()

    return {
        "length": len(text),
        "word_count": len(words),
        "keywords": words[:5],
    }


def detect_sections(text: str) -> dict:
    clean = prepare_for_matching(text)

    found = []

    for section in CV_SECTIONS:
        aliases = section["aliases"]

        if any(contains_skill(clean, alias, "compact") for alias in aliases):
            found.append(section["label"])

    return {
        "sections_found": found,
        "structure_score": compute_structure_score(len(found)),
    }

def prepare_for_matching(text: str) -> str:
    text = text.lower()
    text = text.replace("c#", "csharp")
    text = text.replace(".net", "dotnet")
    return remove_accents(normalize_text(text))


def compact_text(text: str) -> str:
    return re.sub(r"\s+", "", text)


def contains_skill(text: str, alias: str, match_strategy: str = "strict") -> bool:
    normalized_alias = prepare_for_matching(alias)

    word_pattern = rf"(?<!\w){re.escape(normalized_alias)}(?!\w)"
    if re.search(word_pattern, text):
        return True

    if match_strategy != "compact":
        return False

    compacted_text = compact_text(text)
    compacted_alias = compact_text(normalized_alias)

    return compacted_alias in compacted_text

def detect_skills(text: str) -> dict:
    clean = prepare_for_matching(text)

    skills_by_category = {}
    skills_found = []

    for category, skills in SKILLS.items():
        detected_skills = []

        for skill in skills:
            aliases = skill["aliases"]
            match_strategy = skill.get("match", "strict")

            if any(contains_skill(clean, alias, match_strategy) for alias in aliases):
                detected_skills.append(skill["label"])

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

    if structure_score < 70:
        suggestions.append(
            "Structurez davantage le CV avec des sections immédiatement identifiables : profil, expériences, formation, compétences et projets."
        )

    if skills_count < 8:
        suggestions.append(
            "Rendez les compétences techniques plus visibles dans une section dédiée ou dans les descriptions de projets."
        )
    elif skills_count < 14:
        suggestions.append(
            "Les compétences sont présentes, mais certaines technologies clés pourraient être mises plus en avant."
        )

    if action_score < 60:
        suggestions.append(
            "Ajoutez davantage de verbes d’action pour mieux valoriser vos réalisations : concevoir, développer, déployer, automatiser, sécuriser, optimiser."
        )
    elif action_score < 80:
        suggestions.append(
            "Les actions sont visibles, mais vous pouvez encore renforcer l’impact avec plus de résultats mesurables."
        )

    if skills_count >= 14 and structure_score >= 80 and action_score >= 70:
        suggestions.append(
            "CV solide : les compétences, la structure et les actions sont globalement bien représentées."
        )

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
