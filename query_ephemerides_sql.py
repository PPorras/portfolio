import sqlite3

def connect_db(db_name="ephemerides.db"):
    """Connect to SQLite database."""
    return sqlite3.connect(db_name)

def show_tables(conn):
    """Show all tables in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]

def show_schema(conn, table_name="ephemerides"):
    """Show table schema."""
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    schema = cursor.fetchall()
    return schema

def query_data(conn, query="SELECT * FROM ephemerides;"):
    """Execute a query and return the results."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def main():
    db_name = input("Enter database name (default: ephemerides.db): ") or "ephemerides.db"
    conn = connect_db(db_name)
    
    print("\nTables in database:")
    tables = show_tables(conn)
    print(tables)
    
    if tables:
        table_name = tables[0]  # Assume first table
        print(f"\nTable Schema for {table_name}:")
        print(show_schema(conn, table_name))
    
        print("\nQuery Results:")
        results = query_data(conn, f"SELECT * FROM {table_name};")
        for row in results:
            print(row)
    else:
        print("No tables found in the database.")
    
    conn.close()

if __name__ == "__main__":
    main()

