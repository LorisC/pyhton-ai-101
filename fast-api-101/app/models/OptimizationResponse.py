from typing import List

from pydantic import BaseModel


class OptimizationResponse(BaseModel):
    ats_score: int
    missing_keywords: List[str]
    status: str