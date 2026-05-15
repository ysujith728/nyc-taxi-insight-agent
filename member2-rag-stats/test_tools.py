from rag_tool import search_docs
from stats_tool import compute_stats


print("\n=== RAG TEST ===\n")

results = search_docs("What is passenger_count?")

for r in results:
    print(r)
    print("-" * 50)


print("\n=== STATS TEST ===\n")

data = {
    "fare_amount": [12, 25, 18, 40, 100]
}

stats = compute_stats(data, "fare_amount")

print(stats)