import duckdb

PARQUET_GLOB = "data/parquet/yellow_tripdata_2024-*.parquet"

# Create DuckDB connection
con = duckdb.connect(database=":memory:")

# Create trips view
con.execute(f"""
CREATE VIEW trips AS
SELECT *
FROM read_parquet('{PARQUET_GLOB}')
""")

print("SQL Tool Ready!")


def run_sql_query(query):
    """
    Executes a SQL query on NYC taxi data
    and returns the result as a dataframe.
    """

    try:
        result = con.execute(query).fetchdf()
        return result

    except Exception as e:
        return f"Error: {e}"


# Example query
query = """
SELECT payment_type,
       AVG(fare_amount) AS avg_fare
FROM trips
WHERE fare_amount > 0
AND fare_amount < 500
GROUP BY payment_type
ORDER BY avg_fare DESC
"""

result = run_sql_query(query)

print("\nQUERY RESULT:")
print(result)