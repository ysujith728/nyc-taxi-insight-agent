import duckdb

PARQUET_GLOB = "data/parquet/yellow_tripdata_2024-*.parquet"

# Create DuckDB connection
con = duckdb.connect(database=":memory:")

# Create SQL view over parquet files
con.execute(f"""
CREATE VIEW trips AS
SELECT *
FROM read_parquet('{PARQUET_GLOB}')
""")

print("DuckDB connected successfully!")

# Run first SQL query
# Total trips
total_trips = con.execute("""
SELECT COUNT(*) AS total_trips
FROM trips
""").fetchdf()

print("\nTOTAL TRIPS:")
print(total_trips)

# Average fare
average_fare = con.execute("""
SELECT AVG(fare_amount) AS average_fare
FROM trips
WHERE fare_amount > 0
AND fare_amount < 500
""").fetchdf()

print("\nAVERAGE FARE:")
print(average_fare)

# Highest fare
highest_fare = con.execute("""
SELECT MAX(fare_amount) AS highest_fare
FROM trips
WHERE fare_amount > 0
AND fare_amount < 500
""").fetchdf()

print("\nHIGHEST FARE:")
print(highest_fare)

# Average tip
average_tip = con.execute("""
SELECT AVG(tip_amount) AS average_tip
FROM trips
WHERE tip_amount > 0
AND tip_amount < 200
""").fetchdf()

print("\nAVERAGE TIP:")
print(average_tip)

# Payment type statistics
payment_stats = con.execute("""
SELECT payment_type,
       COUNT(*) AS total_trips,
       AVG(fare_amount) AS avg_fare
FROM trips
GROUP BY payment_type
ORDER BY total_trips DESC
""").fetchdf()

print("\nPAYMENT TYPE STATS:")
print(payment_stats)