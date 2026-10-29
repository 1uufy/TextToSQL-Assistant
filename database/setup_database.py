
import sqlite3
from pathlib import Path

# Find the project directory and database file
PROJECT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_DIR / "database" / "company.db"

# Connect to the SQLite database
connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Create the employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL,
    age INTEGER,
    city TEXT
)
""")

# Insert sample employee records
employees = [
    (1, "Aarav Sharma", "IT", 85000, 28, "Delhi"),
    (2, "Priya Singh", "HR", 60000, 31, "Mumbai"),
    (3, "Rahul Verma", "IT", 95000, 35, "Bengaluru"),
    (4, "Neha Gupta", "Finance", 72000, 29, "Delhi"),
    (5, "Arjun Mehta", "IT", 78000, 26, "Pune"),
    (6, "Ananya Rao", "HR", 68000, 32, "Bengaluru"),
    (7, "Vikram Patel", "Finance", 90000, 38, "Mumbai"),
    (8, "Isha Kapoor", "IT", 105000, 30, "Delhi"),
    (9, "Rohan Das", "Marketing", 65000, 27, "Kolkata"),
    (10, "Meera Nair", "Marketing", 75000, 33, "Chennai")
]

# Avoid inserting duplicates if the script is run again
cursor.executemany("""
INSERT OR IGNORE INTO employees
(employee_id, name, department, salary, age, city)
VALUES (?, ?, ?, ?, ?, ?)
""", employees)

# Save changes and close the connection
connection.commit()
connection.close()

print(f"Database created successfully: {DB_PATH}")
