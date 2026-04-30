from app.services.text_normalizer import clean_pdf_text, normalize_text


def test_normalize_text_lowercase_and_removes_punctuation():
    assert normalize_text("Python, FastAPI!") == "python fastapi"


def test_normalize_text_collapses_spaces():
    assert normalize_text("Python     FastAPI") == "python fastapi"


def test_clean_pdf_text_removes_line_breaks():
    assert clean_pdf_text("Python\nFastAPI") == "Python FastAPI"


def test_clean_pdf_text_rebuilds_spaced_words():
    assert clean_pdf_text("C O M P E T E N C E S") == "COMPETENCES"
