from langchain_core.tools import tool
import pandas as pd
from pathlib import Path

# -----------------------------
# Load Taxi Zone Lookup CSV
# -----------------------------

CSV_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "lookup"
    / "taxi_zone_lookup.csv"
)

zones_df = pd.read_csv(CSV_PATH)

# -----------------------------
# LangChain Tool
# -----------------------------

@tool
def zone_lookup_tool(zone_name: str) -> str:
    """
    Lookup NYC taxi zone information by zone name.
    Returns matching LocationID, Borough, and Zone.
    """

    try:

        matches = zones_df[
            zones_df["Zone"].str.contains(
                zone_name,
                case=False,
                na=False
            )
        ]

        if matches.empty:
            return f"No matching zone found for '{zone_name}'."

        return matches.head(10).to_markdown(index=False)

    except Exception as e:
        return f"ERROR: {str(e)}"


# -----------------------------
# Local testing
# -----------------------------

if __name__ == "__main__":

    print("\nZone Lookup Tool Ready!")

    zone = input("\nEnter Zone Name:\n")

    result = zone_lookup_tool.invoke(zone)

    print("\nRESULT:\n")
    print(result)