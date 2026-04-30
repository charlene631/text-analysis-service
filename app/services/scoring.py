def compute_structure_score(sections_count: int) -> int:
    return min(100, sections_count * 25)


def compute_skills_score(skills_count: int) -> int:
    return min(100, skills_count * 20)


def compute_action_score(action_verbs_count: int) -> int:
    return min(100, action_verbs_count * 20)


def compute_global_score(
    structure_score: int,
    skills_score: int,
    action_score: int,
) -> int:
    global_score = (
        structure_score * 0.3
        + skills_score * 0.4
        + action_score * 0.3
    )

    return round(global_score)
