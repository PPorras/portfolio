import requests
import sqlite3
import json

# Define query parameters
params = {
    "format": "json",
    "COMMAND": "'499'",  # Mars code in JPL Horizons
    "EPHEM_TYPE": "OBSERVER",
    "CENTER": "'500'",   # Observation center: Earth
    "START_TIME": "'2025-06-01'",
    "STOP_TIME": "'2025-06-05'",
    "STEP_SIZE": "'1 d'",
    "QUANTITIES": "'1,20,23,24'"  # Position, distance, magnitude data
}

# JPL Horizons API URL
url = "https://ssd.jpl.nasa.gov/api/horizons.api"

# Make GET request to the API
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()  # Convert response to JSON

    # 📌 Print response for analysis
    ## print(json.dumps(data, indent=4))

    # Check if "result" key exists in JSON
    if "result" not in data:
        print("Error: Unexpected response format")
        exit()

    # Split into lines
    ephemerides = data["result"].splitlines()

    # Filter only data lines (discard headers)
    clean_data = []
    for line in ephemerides:
        if line.strip() and not any(x in line for x in ["Date", "=", "Target", "JDTDB"]):  # Skip headers
            clean_data.append(line)

    # Connect to SQLite
    conn = sqlite3.connect("ephemerides.db")
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ephemerides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        object TEXT,
        date TEXT,
        RA TEXT,
        DEC TEXT,
        distance_AU TEXT
    )
    """)

    # Process clean data
    for line in clean_data:
        cols = line.split()
        if len(cols) < 4:
            continue  # Avoid errors from incomplete lines

        try:
            date = cols[0]
            RA = cols[1]  # Store as text to avoid errors
            DEC = cols[2]
            distance = cols[3]

            # Insert data into database
            cursor.execute("INSERT INTO ephemerides (object, date, RA, DEC, distance_AU) VALUES (?, ?, ?, ?, ?)",
                           ("Mars", date, RA, DEC, distance))

        except Exception as e:
            print(f"Error processing line: {line} - {e}")
            continue

    # Save and close connection
    conn.commit()
    conn.close()
    print("Data saved in SQLite database 'ephemerides.db'")

else:
    print(f"Error retrieving data: {response.status_code}")

