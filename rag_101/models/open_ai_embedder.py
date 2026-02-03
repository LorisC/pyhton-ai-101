from pydantic_ai import Embedder
from pydantic_ai.embeddings.openai import OpenAIEmbeddingModel
from pydantic_ai.providers.gateway import gateway_provider

from env_settings import EnvSettings


def create_openai_embedder(api_key: str | None = None):

    if api_key is None:
        env = EnvSettings()
        api_key = env.pydantic_ai_gateway_api_key

    provider = gateway_provider('openai', api_key=api_key)

    model = OpenAIEmbeddingModel(
        'text-embedding-3-small',
        provider=provider,
    )
    embedder = Embedder(model)

    return embedder