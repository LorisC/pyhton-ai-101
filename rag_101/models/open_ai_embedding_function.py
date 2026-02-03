from chromadb import EmbeddingFunction, Documents

from models.open_ai_embedder import create_openai_embedder


class OpenAiEmbeddingFunction(EmbeddingFunction):
    """Adapter to use pydantic-ai embeddings with ChromaDB."""

    def __init__(self):
        self._embedder = create_openai_embedder()

    def __call__(self, input: Documents) -> list[list[float]]:
        """ChromaDB calls this method to generate embeddings."""
        # Get embeddings from pydantic-ai
        embeddings =  self._embedder.embed_sync(input, input_type="text")

        # Convert to list format ChromaDB expects
        return [emb for emb in embeddings]
