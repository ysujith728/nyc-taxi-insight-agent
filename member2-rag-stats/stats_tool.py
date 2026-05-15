import pandas as pd


def compute_stats(data, column_name):

    df = pd.DataFrame(data)

    if column_name not in df.columns:
        return f"Column '{column_name}' not found."

    col = df[column_name]

    stats = {
        "count": int(col.count()),
        "mean": float(col.mean()),
        "median": float(col.median()),
        "min": float(col.min()),
        "max": float(col.max()),
        "std_dev": float(col.std())
    }

    return stats


# Test
if __name__ == "__main__":

    sample_data = {
        "fare_amount": [10, 20, 15, 30, 25, 100]
    }

    result = compute_stats(sample_data, "fare_amount")

    print(result)