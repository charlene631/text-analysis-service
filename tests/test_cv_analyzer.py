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

    assert "python" in result["analysis"]["skills_found"]
    assert "fastapi" in result["analysis"]["skills_found"]
    assert "react" in result["analysis"]["skills_found"]
    assert "docker" in result["analysis"]["skills_found"]


def test_analyze_cv_has_cv_meta_type():
    result = analyze_cv("Python FastAPI")

    assert result["meta"]["type"] == "cv"


def test_analyze_cv_returns_action_verb_labels():
    result = analyze_cv("J'ai développé une API et déployé une application.")

    assert "développer" in result["analysis"]["action_verbs_found"]
    assert "déployer" in result["analysis"]["action_verbs_found"]


def test_analyze_cv_groups_skills_by_category():
    result = analyze_cv("Python FastAPI React Docker")

    assert "python" in result["analysis"]["skills_by_category"]["backend"]
    assert "react" in result["analysis"]["skills_by_category"]["frontend"]
    assert "docker" in result["analysis"]["skills_by_category"]["devops"]
