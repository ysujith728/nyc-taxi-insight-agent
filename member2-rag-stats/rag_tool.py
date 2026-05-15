from langchain_core.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path

# -----------------------------
# Load embeddings model
# -----------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Load FAISS vector store
# -----------------------------

FAISS_PATH = (
    Path(__file__).resolve().parent.parent
    / "faiss_index"
)

vectorstore = FAISS.load_local(
    str(FAISS_PATH),
    embedding_model,
    allow_dangerous_deserialization=True
)

# -----------------------------
# LangChain Tool
# -----------------------------

@tool
def doc_search_tool(question: str) -> str:
    """
    Search NYC taxi documentation using semantic retrieval.
    Returns relevant document chunks.
    """

    try:

        docs_with_scores = vectorstore.similarity_search_with_score(
            question,
            k=3
        )

        # -----------------------------
        # Filter low relevance matches
        # -----------------------------

        filtered_docs = []

        for doc, score in docs_with_scores:

            # Lower score = better similarity
            if score < 1.2:
                filtered_docs.append(doc)

        if not filtered_docs:
            return "No relevant documents found."

        results = []

        for i, doc in enumerate(filtered_docs, start=1):

            results.append(
                f"\n--- Chunk {i} ---\n{doc.page_content}"
            )

        return "\n".join(results)

    except Exception as e:
        return f"ERROR: {str(e)}"


# -----------------------------
# Local testing
# -----------------------------

if __name__ == "__main__":

    print("\nRAG Tool Ready!")

    question = input(
        "\nEnter Question:\n"
    )

    result = doc_search_tool.invoke(
        {"question": question}
    )

    print("\nRESULT:\n")
    print(result)