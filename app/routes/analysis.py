from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.schemas.analysis_schema import CvAnalysisResponse, LinkedinAnalysisResponse
from app.services.cv_analyzer import analyze_cv
from app.services.linkedin_analyzer import analyze_linkedin
from app.services.pdf_extractor import extract_text_from_pdf

from app.core.config import settings

router = APIRouter(prefix="/analyze", tags=["Analysis"])

async def validate_pdf_upload(file: UploadFile) -> bytes:
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Le fichier doit être un PDF.",
        )
    
    file_bytes = await file.read()
    max_size = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024

    if len(file_bytes) > max_size:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Le fichier dépasse la taille maximale de {settings.MAX_UPLOAD_SIZE_MB} MB.",
        )
    
    return file_bytes

@router.post("/cv/pdf", response_model=CvAnalysisResponse)
async def analyze_cv_route(file: UploadFile = File(...)):
    file_bytes = await validate_pdf_upload(file)
    text = extract_text_from_pdf(file_bytes)

    return analyze_cv(text)


@router.post("/linkedin/pdf", response_model=LinkedinAnalysisResponse)
async def analyze_linkedin_route(file: UploadFile = File(...)):
    file_bytes = await validate_pdf_upload(file)
    text = extract_text_from_pdf(file_bytes)

    return analyze_linkedin(text)
