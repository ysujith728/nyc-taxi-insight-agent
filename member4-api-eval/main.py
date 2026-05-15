from fastapi import FastAPI
from pydantic import BaseModel

from .logger_config import logger

from dotenv import load_dotenv
from pathlib import Path
import sys

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_groq import ChatGroq

# -----------------------------
# Load environment variables
# -----------------------------

load_dotenv()

# -----------------------------
# Setup import paths
# -----------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    str(ROOT_DIR / "member1-data-infra")
)

sys.path.append(
    str(ROOT_DIR / "member2-rag-stats")
)

# -----------------------------
# Import tools
# -----------------------------

from sql_tool import sql_query_tool
from zone_lookup_tool import zone_lookup_tool
from stats_tool import stats_tool
from rag_tool import doc_search_tool

# -----------------------------
# FastAPI App
# -----------------------------

app = FastAPI(
    title="NYC Taxi Insight Agent",
    version="1.0"
)

# -----------------------------
# LLM
# -----------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# -----------------------------
# Tools
# -----------------------------

tools = [
    sql_query_tool,
    zone_lookup_tool,
    stats_tool,
    doc_search_tool
]

# -----------------------------
# Memory
# -----------------------------

memory = MemorySaver()

# -----------------------------
# Agent
# -----------------------------

agent = create_react_agent(
    llm,
    tools,
    checkpointer=memory
)

# -----------------------------
# Config
# -----------------------------

config = {
    "configurable": {
        "thread_id": "api-session"
    },

    # Assignment requires bounded reasoning
    "recursion_limit": 15
}

# -----------------------------
# Request Model
# -----------------------------

class QuestionRequest(BaseModel):
    question: str

# -----------------------------
# Health Endpoint
# -----------------------------

@app.get("/health")
def health():

    logger.info(
        "Health check endpoint called"
    )

    return {
        "status": "healthy"
    }

# -----------------------------
# Ask Endpoint
# -----------------------------

@app.post("/ask")
def ask_question(request: QuestionRequest):

    try:

        logger.info(
            f"Question received: {request.question}"
        )

        response = agent.invoke(
            {
                "messages": [
                    ("user", request.question)
                ]
            },
            config=config
        )

        # DEBUG PRINT
        print("\nFULL RESPONSE:\n")
        print(response)

        answer = response["messages"][-1].content

        logger.info(
            f"Generated answer: {answer}"
        )

        return {
            "question": request.question,
            "answer": str(answer)
        }

    except Exception as e:

        logger.error(str(e))

        return {
            "question": request.question,
            "error": str(e)
        }