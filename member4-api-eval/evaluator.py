import requests
import time

# -----------------------------
# Test Questions
# -----------------------------

questions = [

    "What does RateCodeID mean?",

    "What is the average fare amount?",

    "Find the LocationID for JFK Airport",

    "What borough is JFK Airport in?",

    "Explain payment_type",

    "randomunknownfield"
]

# -----------------------------
# API Endpoint
# -----------------------------

API_URL = "http://127.0.0.1:8000/ask"

# -----------------------------
# Evaluation
# -----------------------------

success_count = 0

print("\n=== NYC TAXI AGENT EVALUATION ===\n")

for i, question in enumerate(questions, start=1):

    print(f"\nTest {i}")
    print(f"Question: {question}")

    payload = {
        "question": question
    }

    try:

        start_time = time.time()

        response = requests.post(
            API_URL,
            json=payload
        )

        end_time = time.time()

        latency = round(
            end_time - start_time,
            2
        )

        data = response.json()

        answer = data.get(
            "answer",
            "No answer returned"
        )

        print(f"Answer: {answer}")

        print(f"Latency: {latency} sec")

        if response.status_code == 200:
            success_count += 1

    except Exception as e:

        print(f"ERROR: {e}")

# -----------------------------
# Final Metrics
# -----------------------------

total = len(questions)

accuracy = round(
    (success_count / total) * 100,
    2
)

print("\n=== FINAL METRICS ===")

print(f"Total Tests: {total}")

print(f"Successful Responses: {success_count}")

print(f"Success Rate: {accuracy}%")