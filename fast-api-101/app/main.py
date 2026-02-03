from fastapi import FastAPI, HTTPException, Depends

from app.models.OptimizationRequest import OptimizationRequest
from app.models.OptimizationResponse import OptimizationResponse
from app.services.ResumeAnalyzer import ResumeAnalyzer

app = FastAPI(
    title="Resume Rocket API",
    description="API d'optimisation de candidature pour le marché US",
    version="0.1.0"
)


# Dépendance injectable (facilite les tests et l'évolution)
def get_analyzer() -> ResumeAnalyzer:
    return ResumeAnalyzer()


@app.get("/")
async def health_check():
    return {"status": "online", "service": "Resume Rocket API"}


@app.post("/analyze", response_model=OptimizationResponse)
async def analyze_application(
        request: OptimizationRequest,
        analyzer: ResumeAnalyzer = Depends(get_analyzer)
):
    """Analyse un CV vs une offre d'emploi"""

    # Validation métier
    if "internal use only" in request.job_description.lower():
        raise HTTPException(status_code=403, detail="Offre confidentielle")

    # Appel du service
    result = analyzer.analyze(request.resume_text, request.job_description)

    # Mapping vers le modèle public
    return OptimizationResponse(
        ats_score=result['score'],
        missing_keywords=result['missing'],
        status="analysis_complete"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)