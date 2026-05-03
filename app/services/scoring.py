def compute_structure_score(sections_count: int) -> int:
    if sections_count <= 2:
        return 35
    if sections_count == 3:
        return 55
    if sections_count == 4:
        return 70
    if sections_count == 5:
        return 85

    return 95


def compute_skills_score(skills_count: int) -> int:
    if skills_count <= 3:
        return 35
    if skills_count <= 6:
        return 55
    if skills_count <= 10:
        return 70
    if skills_count <= 15:
        return 82
    if skills_count <= 22:
        return 90

    return 95


def compute_action_score(action_verbs_count: int) -> int:
    if action_verbs_count == 0:
        return 20
    if action_verbs_count <= 2:
        return 40
    if action_verbs_count <= 4:
        return 60
    if action_verbs_count <= 7:
        return 78

    return 90


def compute_global_score(
    structure_score: int,
    skills_score: int,
    action_score: int,
) -> int:
    global_score = (
        structure_score * 0.30
        + skills_score * 0.45
        + action_score * 0.25
    )

    return round(global_score)
