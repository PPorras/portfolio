import sqlite3

def create_db(db_name="data/ephemerides.db"):
    """Create SQLite database and ephemerides table if not exists."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
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
    
    conn.commit()
    conn.close()

def insert_data(data, db_name="data/ephemerides.db"):
    """Insert ephemerides data into the database."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    for line in data:
        cols = line.split()
        if len(cols) < 4:
            continue  # Skip incomplete lines
        
        try:
            date, RA, DEC, distance = cols[0], cols[1], cols[2], cols[3]
            cursor.execute("""
                INSERT INTO ephemerides (object, date, RA, DEC, distance_AU)
                VALUES (?, ?, ?, ?, ?)
            """, ("Mars", date, RA, DEC, distance))
        except Exception as e:
            print(f"Error inserting data: {e}")
            continue
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    print("Database initialized.")

