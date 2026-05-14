# NYC Taxi Insight Agent

A LangChain agentic AI system that answers natural-language questions about NYC Yellow Taxi trip data using multi-tool reasoning, RAG retrieval, and a FastAPI backend.

---

## Project Overview

This system uses LangChain/LangGraph to autonomously decide which tools to call, combine information from multiple sources, perform calculations on real public data, and produce grounded answers with reasoning traces.

---

## Team Structure

| Member | Folder | Responsibility |
|--------|--------|---------------|
| Member 1 | `member1-data-infra/` | Data Infrastructure, SQL Tool, Zone Lookup Tool |
| Member 2 | `member2-rag-stats/` | RAG Tool, Stats Tool, Vector Store |
| Member 3 | `member3-agent-core/` | LangChain Agent, Prompts, Memory |
| Member 4 | `member4-api-eval/` | FastAPI, Evaluation, Docker, Observability |

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/ysujith728/nyc-taxi-insight-agent.git
cd nyc-taxi-insight-agent
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
# Open .env and fill in your API keys
```

### 5. Start the system
```bash
docker compose up
```

---

## Team Rules

- Each member only works inside their assigned folder
- Never push directly to `main`
- Always create a branch and open a Pull Request
- Update `requirements.txt` if you install a new package
- Only the repo owner merges Pull Requests

---

## Architecture

- **LLM Orchestration:** LangChain / LangGraph
- **Structured Data:** DuckDB over Parquet files
- **Vector Store:** FAISS / Chroma
- **API:** FastAPI
- **Packaging:** Docker + docker-compose

---

## Dataset

NYC TLC Yellow Taxi Trip Records — 3 consecutive months from 2023/2024 (~9–12 million rows)

Source: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page