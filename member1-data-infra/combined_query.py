import duckdb
import pandas as pd

# -----------------------------
# Load zone lookup CSV
# -----------------------------

zones = pd.read_csv("data/lookup/taxi_zone_lookup.csv")


def get_zone_id(zone_name):

    result = zones[
        zones["Zone"].str.contains(zone_name, case=False, na=False)
    ]

    return result


# -----------------------------
# Setup DuckDB
# -----------------------------

PARQUET_GLOB = "data/parquet/yellow_tripdata_2024-*.parquet"

con = duckdb.connect(database=":memory:")

con.execute(f"""
CREATE VIEW trips AS
SELECT *
FROM read_parquet('{PARQUET_GLOB}')
""")

print("Combined Tool Ready!")


# -----------------------------
# Search Zone
# -----------------------------

user_zone = input("Enter pickup zone: ")

zone_result = get_zone_id(user_zone)
print("\nZONE MATCH:")
print(zone_result)

# Get first matching LocationID
if zone_result.empty:
    print("No matching zone found.")
    exit()

location_id = zone_result.iloc[0]["LocationID"]
print(f"\nUsing LocationID: {location_id}")


# -----------------------------
# SQL Query
# -----------------------------

query = f"""
SELECT AVG(fare_amount) AS avg_fare
FROM trips
WHERE PULocationID = {location_id}
AND fare_amount > 0
AND fare_amount < 500
"""

result = con.execute(query).fetchdf()

print("\nQUERY RESULT:")
print(result)