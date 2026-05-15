
# Member 1 — Data Infrastructure

## Overview

This module handles all structured data operations for the NYC Taxi Insight Agent.

Responsibilities include:

* DuckDB integration
* SQL query execution
* Taxi zone lookup
* Dynamic query handling
* SQL safety validation

---

# Files

| File                  | Purpose                                   |
| --------------------- | ----------------------------------------- |
| `duckdb_setup.py`     | Initializes DuckDB and validates datasets |
| `sql_tool.py`         | Executes validated SQL queries            |
| `zone_lookup_tool.py` | Searches taxi zones and LocationIDs       |
| `combined_query.py`   | Combines zone lookup with SQL analytics   |

---

# Datasets Used

## Yellow Taxi Trip Data

Stored in:

```text
data/parquet/
```

Example files:

* yellow_tripdata_2024-01.parquet
* yellow_tripdata_2024-02.parquet
* yellow_tripdata_2024-03.parquet

---

## Taxi Zone Lookup CSV

Stored in:

```text
data/lookup/
```

File:

```text
taxi_zone_lookup.csv
```

---

# Features Implemented

## 1. DuckDB Integration

DuckDB is used for efficient SQL analytics directly over parquet files.

Benefits:

* no database server required
* fast analytical queries
* parquet-native execution

---

## 2. SQL Query Tool

The `sql_query_tool`:

* accepts dynamic SQL queries
* restricts unsafe queries
* supports SELECT/WITH statements only
* returns results in markdown format

Example:

```sql
SELECT AVG(fare_amount) AS avg_fare FROM trips;
```

---

## 3. SQL Safety Validation

Blocked queries:

```sql
DROP TABLE trips;
```

Allowed queries:

```sql
SELECT * FROM trips LIMIT 5;
```

---

## 4. Zone Lookup Tool

The `zone_lookup_tool` resolves human-readable place names.

Example:

```text
JFK
```

Returns:

```text
LocationID: 132
Borough: Queens
```

---

# How to Run

## Run DuckDB Setup

```bash
python member1-data-infra/duckdb_setup.py
```

---

## Run SQL Tool

```bash
python member1-data-infra/sql_tool.py
```

---

## Run Zone Lookup Tool

```bash
python member1-data-infra/zone_lookup_tool.py
```

---

## Run Combined Query Tool

```bash
python member1-data-infra/combined_query.py
```

---

# Example Queries

## SQL Example

```sql
SELECT COUNT(*) AS total_trips FROM trips;
```

---

## SQL Average Example

```sql
SELECT AVG(fare_amount) AS avg_fare FROM trips;
```

---

## Zone Example

```text
Times
```

---
