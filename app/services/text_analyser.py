def analyze_base(text: str):
    words = text.split()
    return {
        "length": len(text),
        "word_count": len(words),
        "keywords": list(set(words))[:5],
    }


def analyze_cv(text: str):
    base = analyze_base(text)

    return {
        **base,
        "type": "cv",
        "clarity_score": min(100, len(text.split()) * 2),
        "suggestions": [
            "Ajoutez des verbes d’action",
            "Structurez en sections claires",
            "Ajoutez des compétences techniques visibles"
        ]
    }


def analyze_linkedin(text: str):
    base = analyze_base(text)

    return {
        **base,
        "type": "linkedin",
        "tone_score": min(100, len(text.split()) * 1.5),
        "suggestions": [
            "Rendez votre pitch plus direct",
            "Ajoutez une phrase d’impact",
            "Mettez en avant vos résultats"
        ]
    }
