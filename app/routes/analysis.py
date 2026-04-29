from fastapi import APIRouter, UploadFile, File
from app.services.text_analyser import extract_text_from_pdf, analyze_cv, analyze_linkedin

router = APIRouter()

@router.post("/analyze/cv/pdf")
async def analyze_cv_route(file: UploadFile = File(...)):
    file_bytes = await file.read()
    text = extract_text_from_pdf(file_bytes)
    return analyze_cv(text)

@router.post("/analyze/linkedin/pdf")
async def analyze_linkedin_route(file: UploadFile = File(...)):
    file_bytes = await file.read()
    text = extract_text_from_pdf(file_bytes)
    return analyze_linkedin(text)
