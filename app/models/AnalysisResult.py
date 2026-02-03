from typing import List

from pydantic import BaseModel


class AnalysisResult(BaseModel):
    """Résultat interne de l'analyse (domaine)"""
    score: int
    missing_keywords: List[str]