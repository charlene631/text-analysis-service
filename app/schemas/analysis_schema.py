from pydantic import BaseModel
from typing import List, Literal


class AnalysisSummary(BaseModel):
    global_score: int
    structure_score: int
    skills_score: int
    action_score: int


class AnalysisDetails(BaseModel):
    sections_found: List[str]
    skills_found: List[str]
    action_verbs_found: List[str]


class AnalysisMeta(BaseModel):
    type: Literal["cv", "linkedin"]
    length: int
    word_count: int


class CvAnalysisResponse(BaseModel):
    summary: AnalysisSummary
    analysis: AnalysisDetails
    insights: List[str]
    meta: AnalysisMeta


class LinkedinAnalysisResponse(BaseModel):
    summary: AnalysisSummary
    analysis: AnalysisDetails
    insights: List[str]
    meta: AnalysisMeta
