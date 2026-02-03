import chromadb
from chromadb.utils import embedding_functions
import os

from models.open_ai_embedding_function import OpenAiEmbeddingFunction

# 1. INITIALISATION DE LA DB (VOLATILE)
# On n'écrit pas sur le disque, tout reste en RAM pour la privacy
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="user_cv_session", embedding_function=OpenAiEmbeddingFunction())

# 2. DONNÉES SIMULÉES (Ton "Master CV" découpé en morceaux)
# Dans le projet final, ceci viendra du parsing PDF
cv_chunks = [
    "2015-2016: Barista at Starbucks. Learned customer service and speed.",
    "2017-2019: Junior Web Dev. Built WordPress sites using PHP and CSS.",
    "2020-2022: Backend Engineer at Fintech Corp. Built high-traffic APIs using Python and FastAPI. Optimized SQL queries reducing latency by 40%.",
    "2023-Present: Team Lead. Managed 5 developers, implemented Agile methodology and Docker containers."
]

# 3. INDEXATION (Embedding)
print("--- Indexation du CV en cours ---")
collection.add(
    documents=cv_chunks,
    ids=[f"chunk_{i}" for i in range(len(cv_chunks))],
    metadatas=[{"year": "2015"}, {"year": "2017"}, {"year": "2020"}, {"year": "2023"}]
)
print(f"{len(cv_chunks)} blocs indexés en mémoire vectorielle.\n")


# 4. LA FONCTION DE RECHERCHE (Retrieval)
def find_relevant_experience(query_skill: str):
    print(f"🔎 Recherche de preuves pour : '{query_skill}'")

    results = collection.query(
        query_texts=[query_skill],
        n_results=1  # On veut juste le TOP 1 résultat le plus pertinent
    )

    # Extraction propre
    best_match = results['documents'][0][0]
    distance = results['distances'][0][0]  # Plus c'est proche de 0, mieux c'est

    return best_match, distance


# 5. TEST DE SCÉNARIOS
scenarios = [
    "Expertise in API development",  # Doit matcher le bloc 2020
    "Experience managing teams",  # Doit matcher le bloc 2023
    "Customer handling skills"  # Doit matcher le bloc 2015 (Starbucks)
]

for skill in scenarios:
    evidence, score = find_relevant_experience(skill)
    print(f"   ✅ Preuve trouvée : \"{evidence}\" (Distance: {score:.4f})\n")
