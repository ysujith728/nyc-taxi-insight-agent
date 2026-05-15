from rag_tool import doc_search_tool
from stats_tool import stats_tool

print("\n=== RAG TEST ===\n")

print(
    doc_search_tool.invoke(
        {"question": "What is RateCodeID?"}
    )
)

print("\n=== STATS TEST ===\n")

print(
    stats_tool.invoke(
        {"values": [12, 25, 37, 100, 21]}
    )
)