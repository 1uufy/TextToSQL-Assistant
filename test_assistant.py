
from src.assistant import ask_database

question = "Show the five highest-paid employees"

result = ask_database(question)

print("\nQuestion:", result["question"])
print("Generated SQL:", result["sql"])

if result["success"]:
    print("\nDatabase results:")
    for row in result["rows"]:
        print(row)

    print("\nTotal rows:", result["row_count"])
else:
    print("\nError:", result["error"])
