import os
import nest_asyncio
from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel

from src.agents.us_based_recruter import create_job_analyzer_agent

# Patch pour les notebooks/scripts simples asyncio
nest_asyncio.apply()

agent = create_job_analyzer_agent()



# --- 3. EXECUTION ---

async def analyze_job_posting(raw_text: str):
    print(f"Analyzing job description... ({len(raw_text)} chars)")

    # L'agent va faire l'aller-retour avec Anthropic et valider le JSON
    result = await agent.run(raw_text)


    return result.output


# --- 4. TEST DE L'APP ---

if __name__ == "__main__":
    import asyncio

    # Exemple d'offre "Toxique" typique de la Silicon Valley
    bad_job_offer = """
    WE ARE HIRING A 10x ENGINEER!!
    Startup based in San Francisco looking for a Rockstar Developer.
    Must know Python, Rust, React, Kubernetes, and Assembly.
    Salary: Competitive (Equity only for first 6 months).
    We work hard and play hard. No 9-5 mentality here!
    """

    try:
        data = asyncio.run(analyze_job_posting(bad_job_offer))

        print("\n--- RÉSULTAT STRUCTURÉ ---")
        print(f"Poste: {data.job_title}")
        print(f"Compétences: {data.required_skills}")
        print(f"Remote: {data.is_remote}")
        print(f"Score de Toxicité: {data.risk_score}/100")

        if data.salary and data.salary.min_salary:
            print(f"Salaire: {data.salary.min_salary}$")
        else:
            print("Salaire: Non spécifié (Attention: Illégal en Californie depuis 2023 pour les boites >15 employés)")

    except Exception as e:
        print(f"Erreur: {e}")