
from src.sql_generator import generate_sql

questions = [
    "Show all employees in the IT department.",
    "Find the five highest-paid employees.",
    "Calculate the average salary of employees in Delhi."
]

for question in questions:
    print("\nQuestion:", question)

    try:
        sql = generate_sql(question)
        print("Generated SQL:", sql)
    except Exception as error:
        print("Error:", error)
