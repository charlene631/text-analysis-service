import re


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_pdf_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(
        r"(?:(?:\b\w\b\s+){3,})",
        lambda match: match.group(0).replace(" ", ""),
        text,
    )
    text = re.sub(r"\s+", " ", text)
    return text.strip()
