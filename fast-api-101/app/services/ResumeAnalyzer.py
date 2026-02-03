class ResumeAnalyzer:

    def analyze(self, resume: str, job: str) -> dict:
        # Simulation d'un ATS basique
        resume_words = set(resume.lower().split())
        job_words = set(job.lower().split())

        # On cherche les mots de l'offre qui NE SONT PAS dans le CV
        missing = list(job_words - resume_words)

        # Calcul de score arbitraire pour l'exercice
        # Plus il manque de mots, plus le score baisse
        match_count = len(job_words) - len(missing)
        total_words = len(job_words)
        score = int((match_count / total_words) * 100) if total_words > 0 else 0

        return {
            "score": score,
            "missing": missing[:5]  # On en retourne juste 5 pour l'exemple
        }
