# MAIN README.md

# NYC Taxi Insight Agent

## Multi-Tool AI Agent for NYC Taxi Data Analytics

NYC Taxi Insight Agent is a LangChain + LangGraph based AI system capable of answering natural-language questions about New York City taxi trips using structured SQL analytics, semantic document retrieval (RAG), statistical computation, and conversational reasoning.

The system combines:

* SQL analytics using DuckDB
* Retrieval-Augmented Generation (RAG)
* Conversational AI reasoning
* LangGraph orchestration
* FastAPI APIs
* Evaluation harness and logging

The project was developed as part of a LangChain Agentic AI assignment focused on multi-tool reasoning over public open datasets.

---

# Project Objectives

The project demonstrates:

* Multi-tool AI reasoning
* Tool orchestration using LangGraph
* Conversational memory
* SQL querying over Parquet files
* Semantic document retrieval using FAISS
* Statistical analysis tools
* API deployment using FastAPI
* Evaluation and observability

---

# System Architecture

```text
User Question
      ↓
FastAPI API Layer
      ↓
LangGraph ReAct Agent
      ↓
Tool Selection + Reasoning
      ↓
Tool Execution
      ↓
Natural Language Response
```

---

# Project Structure

```text
nyc-taxi-insight-agent/
│
├── data/
│   ├── docs/
│   │   └── NYC_TAXI_DIC.pdf
│   │
│   ├── lookup/
│   │   └── taxi_zone_lookup.csv
│   │
│   └── parquet/
│       ├── yellow_tripdata_2024-01.parquet
│       ├── yellow_tripdata_2024-02.parquet
│       └── yellow_tripdata_2024-03.parquet
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── member1-data-infra/
│   ├── duckdb_setup.py
│   ├── sql_tool.py
│   ├── zone_lookup_tool.py
│   ├── combined_query.py
│   └── README.md
│
├── member2-rag-stats/
│   ├── ingest_docs.py
│   ├── rag_tool.py
│   ├── stats_tool.py
│   ├── test_tools.py
│   ├── vector_store.py
│   ├── main.py
│   └── README.md
│
├── member3-agent-core/
│   ├── agent.py
│   └── README.md
│
├── member4-api-eval/
│   ├── main.py
│   ├── logger_config.py
│   ├── evaluator.py
│   └── README.md
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Technologies Used

| Technology             | Purpose                      |
| ---------------------- | ---------------------------- |
| Python                 | Core programming language    |
| LangChain              | Tool abstraction             |
| LangGraph              | Agent orchestration          |
| DuckDB                 | SQL analytics over parquet   |
| FAISS                  | Vector similarity search     |
| HuggingFace Embeddings | Semantic embeddings          |
| FastAPI                | API framework                |
| Groq LLM               | Large language model backend |
| Uvicorn                | FastAPI server               |
| Pandas                 | Data manipulation            |
| Pydantic               | API request validation       |

---

# Dataset Sources

This project uses publicly available NYC Taxi datasets.

## 1. NYC Yellow Taxi Trip Records

Official Source:

[https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

Download at least 3 consecutive months of Yellow Taxi parquet files.

Example files used:

* yellow_tripdata_2024-01.parquet
* yellow_tripdata_2024-02.parquet
* yellow_tripdata_2024-03.parquet

Place them inside:

```text
data/parquet/
```

---

## 2. Taxi Zone Lookup CSV

Official Source:

[https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv](https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv)

Place file inside:

```text
data/lookup/
```

---

## 3. NYC Taxi Data Dictionary PDF

Official Source:

[https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

Rename file to:

```text
NYC_TAXI_DIC.pdf
```

Place file inside:

```text
data/docs/
```

---

# Features Implemented

## Member 1 — Data Infrastructure

* DuckDB integration
* Secure SQL querying
* Taxi zone lookup system
* Dynamic SQL execution
* SQL safety validation

---

## Member 2 — RAG + Statistics

* PDF ingestion pipeline
* FAISS vector store
* Semantic retrieval system
* Relevance filtering
* Statistical analysis tools

---

## Member 3 — Agent Core

* LangGraph ReAct agent
* Multi-tool reasoning
* Conversational memory
* Bounded execution
* Groq LLM integration

---

## Member 4 — API + Evaluation

* FastAPI APIs
* Swagger documentation
* Logging system
* Evaluation harness
* API observability

---

# Setup Instructions

## Step 1 — Clone Repository

```bash
git clone https://github.com/ysujith728/nyc-taxi-insight-agent.git
```

---

## Step 2 — Navigate into Project

```bash
cd nyc-taxi-insight-agent
```

---

## Step 3 — Create Virtual Environment

```bash
python -m venv .venv
```

---

## Step 4 — Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6 — Create `.env` File

Create a `.env` file in the project root.

Add:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Running the Project

## Step 1 — Generate FAISS Index

Run:

```bash
python member2-rag-stats/ingest_docs.py
```

Expected Output:

```text
FAISS index created successfully!
```

---

## Step 2 — Run the AI Agent

```bash
python member3-agent-core/agent.py
```

---

## Step 3 — Start FastAPI Server

```bash
uvicorn member4-api-eval.main:app --reload
```

---

## Step 4 — Open Swagger Documentation

Open in browser:

```text
http://127.0.0.1:8000/docs
```

---

# Example Questions

## SQL Analytics

```text
What is the average fare amount?
```

---

## RAG Query

```text
What does RateCodeID mean?
```

---

## Zone Lookup

```text
Find the LocationID for JFK Airport
```

---

## Conversational Memory

```text
What is the LocationID for JFK Airport?
```

Follow-up:

```text
What borough is it in?
```

---

# API Endpoints

## GET `/health`

Checks API health.

### Response

```json
{
  "status": "healthy"
}
```

---

## POST `/ask`

Accepts user questions.

### Request

```json
{
  "question": "What does RateCodeID mean?"
}
```

### Response

```json
{
  "question": "What does RateCodeID mean?",
  "answer": "RateCodeID refers to the final rate code in effect at the end of the trip."
}
```

---

# Evaluation Harness

Run:

```bash
python member4-api-eval/evaluator.py
```

---

# Example Evaluation Output

```text
=== FINAL METRICS ===
Total Tests: 6
Successful Responses: 6
Success Rate: 100.0%
```

---

# Key Features

| Feature               | Status   |
| --------------------- | -------- |
| SQL Querying          | Complete |
| RAG Retrieval         | Complete |
| Statistical Analysis  | Complete |
| LangGraph Agent       | Complete |
| Conversational Memory | Complete |
| FastAPI Integration   | Complete |
| Logging System        | Complete |
| Evaluation Harness    | Complete |
| Swagger Documentation | Complete |

---

# Contributors

| Member   | Responsibility      |
| -------- | ------------------- |
| Member 1 | Data Infrastructure |
| Member 2 | RAG + Statistics    |
| Member 3 | Agent Core          |
| Member 4 | API + Evaluation    |

---

# Important Notes

* Ensure parquet files are placed inside `data/parquet/`
* Ensure `.env` contains a valid `GROQ_API_KEY`
* Run `ingest_docs.py` before starting the agent if FAISS index is missing
* Use Python 3.11 or later
* FastAPI Swagger UI is available at `/docs`

---







