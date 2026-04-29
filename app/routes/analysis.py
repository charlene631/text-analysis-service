from fastapi import APIRouter
from app.services.text_analyser import analyze_cv, analyze_linkedin

router = APIRouter()

@router.post("/analyze/cv")
def analyze_cv_route(payload: dict):
    return analyze_cv(payload.get("text", ""))

@router.post("/analyze/linkedin")
def analyze_linkedin_route(payload: dict):
    return analyze_linkedin(payload.get("text", ""))
