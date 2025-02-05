# Ephemerides Fetcher

## 📌 Description
This project retrieves astronomical ephemeris data from the **JPL Horizons API**, stores it in a **SQLite** database, and allows querying through SQL. Additionally, it provides a command-line interface to visualize the retrieved data.

## 📂 Project Structure
```
ephemerides_project/
│── src/
│   │── __init__.py  # Defines src as a Python package
│   │── fetch_data.py  # Fetches data from the JPL Horizons API
│   │── database.py  # Manages the SQLite database (upcoming)
│   │── queries.py  # SQL queries for data analysis (upcoming)
│   │── visualization.py  # Generates plots from the data (upcoming)
│── data/
│   │── ephemerides.db  # SQLite database
│── notebooks/
│   │── exploratory_analysis.ipynb  # Data analysis (upcoming)
│── main.py  # Main script to execute the full workflow
│── README.md  # Project documentation
│── requirements.txt  # Python dependencies (upcoming)
│── .gitignore  # Files to be ignored in Git
```

## 🚀 Installation and Execution
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your_username/ephemerides_project.git
cd ephemerides_project
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies (Upcoming)
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Main Script
```bash
python main.py
```
By default, it will display 10 lines of data. To specify a different number of lines:
```bash
python main.py -n 5  # Displays 5 lines
```

## 🛠 Technologies Used
- **Python** (requests, sqlite3, argparse)
- **SQLite** for data storage
- **JPL Horizons API** for ephemeris acquisition

## 📌 Next Steps
✅ Fetch ephemerides data from the API ✔️
✅ Display data in the terminal with CLI arguments ✔️
🔲 Store data in SQLite
🔲 Advanced SQL queries
🔲 Data visualization with plots

---

## 📜 License
This project is open-source under the MIT license.

## 📬 Contact
For questions or suggestions, contact me at [your email or GitHub].


