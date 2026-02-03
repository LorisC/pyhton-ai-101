from pydantic import BaseModel, Field


class OptimizationRequest(BaseModel):
    resume_text: str = Field(..., min_length=50, description="Le texte brut extrait du CV")
    job_description: str = Field(..., min_length=50, description="Le texte de l'offre d'emploi")
    target_role: str = Field(..., description="Le poste visé")