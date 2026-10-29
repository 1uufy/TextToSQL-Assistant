
from src.sql_executor import validate_sql

test_queries = [
    "SELECT * FROM employees",
    "SELECT name, salary FROM employees WHERE department = 'IT'",
    "DELETE FROM employees",
    "DROP TABLE employees",
    "UPDATE employees SET salary = 0",
    "SELECT * FROM employees; DROP TABLE employees;",
    "INVALID",
    "SELECT name FROM employees WHERE age > 30",
    "SELECT name FROM sqlite_master"
]

for query in test_queries:
    print("\nTesting:", query)

    try:
        safe_query = validate_sql(query)
        print("PASSED validation:", safe_query)
    except ValueError as error:
        print("REJECTED:", error)
