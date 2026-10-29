
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "company.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("SELECT name, department, salary FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
