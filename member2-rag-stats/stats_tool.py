from langchain_core.tools import tool
import statistics
import math

# -----------------------------
# LangChain Tool
# -----------------------------

@tool
def stats_tool(values: list[float]) -> str:
    """
    Compute basic statistics for a list of numeric values.
    Returns count, mean, median, min, max, and standard deviation.
    """

    try:

        if not values:
            return "ERROR: Empty list provided."

        result = {
            "count": len(values),
            "mean": statistics.mean(values),
            "median": statistics.median(values),
            "min": min(values),
            "max": max(values),
            "std_dev": statistics.stdev(values)
            if len(values) > 1 else 0
        }

        return str(result)

    except Exception as e:
        return f"ERROR: {str(e)}"


# -----------------------------
# Local testing
# -----------------------------

if __name__ == "__main__":

    print("\nStats Tool Ready!")

    raw = input(
        "\nEnter numbers separated by commas:\n"
    )

    try:
        values = [
            float(x.strip())
            for x in raw.split(",")
        ]

        result = stats_tool.invoke({"values": values})

        print("\nRESULT:\n")
        print(result)

    except Exception as e:
        print(f"\nERROR: {e}")