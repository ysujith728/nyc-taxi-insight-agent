from rag_tool import search_docs
from stats_tool import compute_stats


while True:

    print("\n=== NYC Taxi Insight Agent ===")
    print("1. Search Taxi Documentation")
    print("2. Compute Statistics")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    # RAG TOOL
    if choice == "1":

        query = input("\nAsk your question: ")

        results = search_docs(query)

        print("\nTop Results:\n")

        for r in results:
            print(r)
            print("-" * 50)

    # STATS TOOL
    elif choice == "2":

        values = input(
            "\nEnter numbers separated by commas: "
        )

        numbers = [float(x.strip()) for x in values.split(",")]

        column_name = "values"

        data = {
            column_name: numbers
        }

        stats = compute_stats(data, column_name)

        print("\nStatistics:\n")

        for key, value in stats.items():
            print(f"{key}: {value}")

    elif choice == "3":

        print("\nExiting...")
        break

    else:
        print("\nInvalid choice.")