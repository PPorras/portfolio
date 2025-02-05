import requests
import json

def get_ephemerides():
    """Fetch ephemerides data from JPL Horizons API."""
    params = {
        "format": "json",
        "COMMAND": "'499'",  # Mars
        "EPHEM_TYPE": "OBSERVER",
        "CENTER": "'500'",  # Earth
        "START_TIME": "'2025-06-01'",
        "STOP_TIME": "'2025-06-05'",
        "STEP_SIZE": "'1 d'",
        "QUANTITIES": "'1,20,23,24'"  # Position, distance, magnitude
    }
    url = "https://ssd.jpl.nasa.gov/api/horizons.api"
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            return data["result"].splitlines()
        else:
            raise ValueError("Unexpected response format")
    else:
        raise ConnectionError(f"Error fetching data: {response.status_code}")

if __name__ == "__main__":
    try:
        ephemerides = get_ephemerides()
        print("Fetched Ephemerides:")
        for line in ephemerides[:10]:  # Print first 10 lines for preview
            print(line)
    except Exception as e:
        print(f"Error: {e}")

