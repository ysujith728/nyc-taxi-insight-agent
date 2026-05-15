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
# LLM
# -----------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# -----------------------------
# Register tools
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
# Create Agent
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
        "thread_id": "nyc-session"
    },

    # Assignment requirement
    "recursion_limit": 15
}

# -----------------------------
# Interactive Testing
# -----------------------------

if __name__ == "__main__":

    print("\nNYC Taxi Insight Agent Ready!")

    while True:

        question = input(
            "\nAsk Question (or type exit):\n"
        )

        if question.lower() == "exit":
            break

        try:

            response = agent.invoke(
                {
                    "messages": [
                        ("user", question)
                    ]
                },
                config=config
            )

            print("\nANSWER:\n")

            print(
                response["messages"][-1].content
            )

        except Exception as e:

            print(f"\nERROR: {str(e)}")