
from src.sql_executor import execute_sql, validate_sql

# Test 1: A permitted query
query = "SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 5"

print("Testing valid SQL...")
result = execute_sql(query)
print("Columns:", result["columns"])
print("Rows:", result["row_count"])
for row in result["rows"]:
    print(row)

# Test 2: A query that should be rejected
print("\nTesting invalid SQL...")
try:
    validate_sql("DELETE FROM employees")
except ValueError as error:
    print("Correctly rejected:", error)
