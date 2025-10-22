import json
from datetime import datetime


# Helper function to convert ISO date format to milliseconds
def iso_to_millis(iso_time):
    """
    Convert ISO 8601 timestamp (e.g. '2020-07-01T12:00:00Z')
    into milliseconds since epoch.
    """
    dt = datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)


# IMPLEMENT: Transform data from data-1.json to unified format
def transform_data1(data):
    """
    Transform the data structure from data-1.json into the unified format.
    Expected unified format:
    {
        "device_id": str,
        "timestamp": int (milliseconds),
        "temperature": float,
        "humidity": float
    }
    """
    transformed = {
        "device_id": data["device"]["id"],
        "timestamp": iso_to_millis(data["telemetry"]["time"]),
        "temperature": data["telemetry"]["temp"],
        "humidity": data["telemetry"]["hum"]
    }
    return transformed


# IMPLEMENT: Transform data from data-2.json to unified format
def transform_data2(data):
    """
    Transform the data structure from data-2.json into the unified format.
    This data already uses milliseconds for timestamps.
    """
    transformed = {
        "device_id": data["dev_id"],
        "timestamp": data["ts"],
        "temperature": data["metrics"]["temperature"],
        "humidity": data["metrics"]["humidity"]
    }
    return transformed


# MAIN EXECUTION (for testing and verification)
if __name__ == "__main__":
    try:
        # Load data from both JSON files
        with open("data-1.json") as f1, open("data-2.json") as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)

        # Transform both datasets
        unified_data = [transform_data1(data1), transform_data2(data2)]

        # Print unified output in pretty JSON format
        print("Unified Result:")
        print(json.dumps(unified_data, indent=2))

        # Optionally, write output to file (for your GitHub repo)
        with open("data-output.json", "w") as outfile:
            json.dump(unified_data, outfile, indent=2)
        print("\n✅ data-output.json created successfully!")

    except Exception as e:
        print("❌ Error while processing:", e)


# NOTES:
# - Converted ISO timestamps to milliseconds using datetime.
# - Ensured both formats produce identical output keys as data-result.json.
# - If you see red text in Replit console, ignore unless tests fail.
