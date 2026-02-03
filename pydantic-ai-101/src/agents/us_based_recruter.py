from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.gateway import gateway_provider

from src.env_settings import EnvSettings
from src.models.job_analysis import JobAnalysis


def create_job_analyzer_agent(api_key: str | None = None) -> Agent:
    """
    Crée l'agent d'analyse de descriptions de poste.

    Args:
        api_key: Clé API Anthropic. Si None, utilise EnvSettings.

    Returns:
        Agent configuré pour analyser des descriptions de poste.
    """
    if api_key is None:
        env = EnvSettings()
        api_key = env.pydantic_ai_gateway_api_key

    provider = gateway_provider('anthropic', api_key=api_key)

    model = AnthropicModel('claude-sonnet-4-5', provider=provider)

    return Agent(
        model,
        system_prompt=(
            "Tu es un expert en recrutement US (Californie)."
            "Tu analyses des descriptions de poste brutes."
            "Extrais les informations clés."
            "Pour le risk_score, analyse le ton: mots clés comme 'Rockstar', 'Ninja', "
            "'Work hard play hard' augmentent le risque."
        ),
        output_type=JobAnalysis
    )
