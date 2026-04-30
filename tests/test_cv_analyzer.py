from app.services.cv_analyzer import analyze_cv


def test_analyze_cv_returns_expected_structure():
    result = analyze_cv(
        "Profil Python FastAPI React. Experience developpement. Formation informatique."
    )

    assert "summary" in result
    assert "analysis" in result
    assert "insights" in result
    assert "meta" in result


def test_analyze_cv_detects_skills():
    result = analyze_cv("Python FastAPI React Docker")

    assert "Python" in result["analysis"]["skills_found"]
    assert "FastAPI" in result["analysis"]["skills_found"]
    assert "React" in result["analysis"]["skills_found"]
    assert "Docker" in result["analysis"]["skills_found"]


def test_analyze_cv_has_cv_meta_type():
    result = analyze_cv("Python FastAPI")

    assert result["meta"]["type"] == "cv"


def test_analyze_cv_returns_action_verb_labels():
    result = analyze_cv("J'ai développé une API et déployé une application.")

    assert "développer" in result["analysis"]["action_verbs_found"]
    assert "déployer" in result["analysis"]["action_verbs_found"]


def test_analyze_cv_groups_skills_by_category():
    result = analyze_cv("Python FastAPI React Docker")

    assert "Python" in result["analysis"]["skills_by_category"]["backend"]
    assert "React" in result["analysis"]["skills_by_category"]["frontend"]
    assert "Docker" in result["analysis"]["skills_by_category"]["devops"]


def test_analyze_cv_detects_soft_skills():
    result = analyze_cv("Autonomie, rigueur et communication avec l'équipe.")

    assert "Autonomie" in result["analysis"]["skills_by_category"]["soft_skills"]
    assert "Rigueur" in result["analysis"]["skills_by_category"]["soft_skills"]
    assert "Communication" in result["analysis"]["skills_by_category"]["soft_skills"]


def test_analyze_cv_avoids_partial_skill_matches():
    result = analyze_cv("Je travaille sur une application.")

    assert "API REST" not in result["analysis"]["skills_found"]


def test_analyze_cv_detects_skill_aliases():
    result = analyze_cv("Création d'une REST API avec Node.js et Express.")

    assert "API REST" in result["analysis"]["skills_by_category"]["backend"]
    assert "Node.js" in result["analysis"]["skills_by_category"]["backend"]
    assert "Express.js" in result["analysis"]["skills_by_category"]["backend"]


def test_analyze_cv_detects_accented_soft_skills():
    result = analyze_cv("Autonome, rigoureuse et bon esprit d'équipe.")

    assert "Autonomie" in result["analysis"]["skills_by_category"]["soft_skills"]
    assert "Rigueur" in result["analysis"]["skills_by_category"]["soft_skills"]
    assert "Travail en équipe" in result["analysis"]["skills_by_category"]["soft_skills"]

def test_analyze_cv_does_not_detect_java_inside_javascript():
    result = analyze_cv("JavaScript React TypeScript")

    assert "JavaScript" in result["analysis"]["skills_found"]
    assert "Java" not in result["analysis"]["skills_found"]


def test_analyze_cv_detects_compacted_pdf_skills():
    result = analyze_cv("apirest supportutilisateur travailenequipe")

    assert "API REST" in result["analysis"]["skills_found"]
    assert "Support utilisateur" in result["analysis"]["skills_found"]
    assert "Travail en équipe" in result["analysis"]["skills_found"]


def test_analyze_cv_does_not_detect_csharp_without_explicit_csharp():
    result = analyze_cv("Contact profil competences")

    assert "C#" not in result["analysis"]["skills_found"]

