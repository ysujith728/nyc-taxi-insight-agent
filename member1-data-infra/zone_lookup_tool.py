import pandas as pd

# Load lookup CSV
zones = pd.read_csv("data/lookup/taxi_zone_lookup.csv")

print("Zone Lookup Tool Ready!")


def get_zone_id(zone_name):
    """
    Returns LocationID for a given zone name.
    """

    result = zones[
        zones["Zone"].str.contains(zone_name, case=False, na=False)
    ]

    return result[["LocationID", "Zone", "Borough"]]


# Example search
search = "JFK"

result = get_zone_id(search)

print("\nSEARCH RESULT:")
print(result)