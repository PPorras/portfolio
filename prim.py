import argparse
from src import get_ephemerides

def main(lines_to_display=10):
    """Main function to fetch and display ephemerides."""
    try:
        ephemerides = get_ephemerides()
        if not ephemerides:
            print("No ephemerides data retrieved.")
            return
        
        print("Inserting data into database...")
        insert_data(ephemerides)

        print("Fetched Ephemerides:")
        for line in ephemerides[:lines_to_display]:  # Print limited lines
            print(line)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and display ephemerides data.")
    parser.add_argument(
        "-n", "--num_lines", type=int, default=10,
        help="Number of ephemerides lines to display (default: 10)"
    )
    args = parser.parse_args()
    main(args.num_lines)
