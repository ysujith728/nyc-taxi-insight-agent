from vector_store import load_vector_store

# Load vector DB
vectorstore = load_vector_store()

# Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


def search_docs(query):

    docs = retriever.invoke(query)

    results = []

    for doc in docs:
        results.append(doc.page_content)

    return results


# Test
if __name__ == "__main__":

    question = "What is VendorID?"

    answer = search_docs(question)

    print("\nRetrieved Chunks:\n")

    for item in answer:
        print(item)
        print("-" * 50)