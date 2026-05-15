from langchain_core.tools import tool
import duckdb
import pandas as pd
import re
from pathlib import Path

# -----------------------------
# Load parquet dataset
# -----------------------------

PARQUET_PATH = str(
    Path(__file__).resolve().parent.parent
    / "data"
    / "parquet"
    / "*.parquet"
)

# -----------------------------
# DuckDB connection
# -----------------------------

con = duckdb.connect(database=":memory:")

con.execute(f"""
CREATE VIEW trips AS
SELECT *
FROM read_parquet('{PARQUET_PATH}')
""")

# -----------------------------
# SQL safety
# -----------------------------

SAFE_SQL = re.compile(r"^\s*(WITH|SELECT)\b", re.IGNORECASE)

# -----------------------------
# LangChain Tool
# -----------------------------

@tool
def sql_query_tool(sql: str) -> str:
    """
    Use this tool to run SQL analytics queries on the NYC taxi trips database.

    Available table:
    - trips

    Important columns:
    - fare_amount
    - tip_amount
    - total_amount
    - trip_distance
    - passenger_count
    - payment_type
    - PULocationID
    - DOLocationID

    IMPORTANT:
    - Questions about "fare" should use fare_amount
    - Questions about "tip" should use tip_amount
    - Questions about "total amount" should use total_amount

    Rules:
    - Only generate SELECT queries
    - Use table name exactly as: trips
    - Return concise numerical results

    Example queries:

    SELECT AVG(fare_amount) AS avg_fare FROM trips;

    SELECT MAX(fare_amount) AS highest_fare FROM trips;

    SELECT COUNT(*) AS total_trips FROM trips;
    """

    if not SAFE_SQL.match(sql):
        return "ERROR: Only SELECT/WITH queries are allowed."

    try:
        df = con.execute(sql).df().head(50)

        if df.empty:
            return "No results found."

        return df.to_string(index=False)

    except Exception as e:
        return f"ERROR: {str(e)}"


# -----------------------------
# Local testing
# -----------------------------

if __name__ == "__main__":

    print("\nSQL Tool Ready!")

    query = input("\nEnter SQL Query:\n")

    result = sql_query_tool.invoke(query)

    print("\nRESULT:\n")
    print(result)