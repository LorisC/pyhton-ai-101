from typing import Optional, List
from pydantic import BaseModel, Field
from src.models.salary_range import SalaryRange


class JobAnalysis(BaseModel):
    job_title: str = Field(..., description="Le titre normalisé du poste")
    company_name: Optional[str] = Field(None, description="Nom de l'entreprise si mentionné")
    required_skills: List[str] = Field(..., description="Liste des compétences techniques exigées (Hard Skills)")
    years_experience: Optional[int] = Field(None, description="Années d'expérience minimum requises")
    is_remote: bool = Field(False, description="True si le poste mentionne 'Remote' ou 'Télétravail'")
    salary: Optional[SalaryRange] = Field(None, description="Fourchette de salaire si mentionnée")
    risk_score: int = Field(..., description="Score de 0 à 100. 100 = Offre suspecte ou toxique.")
