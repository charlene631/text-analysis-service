from io import BytesIO

from fastapi import HTTPException, status
from pypdf import PdfReader
from pypdf.errors import PdfReadError

from app.services.text_normalizer import clean_pdf_text


def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        reader = PdfReader(BytesIO(file_bytes))

        text = ""
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text += page_text.replace("\n", " ")

        cleaned_text = clean_pdf_text(text)

        if not cleaned_text:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Aucun texte exploitable n'a été trouvé dans ce PDF.",
            )

        return cleaned_text

    except PdfReadError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Le PDF est corrompu ou illisible.",
        )
