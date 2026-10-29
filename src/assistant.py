
from src.sql_generator import generate_sql
from src.sql_executor import execute_sql


def ask_database(question: str) -> dict:
    """Convert a question into SQL and return database results."""

    # Step 1: Generate SQL from the user's question
    sql = generate_sql(question)

    # Step 2: Reject invalid model responses
    if not sql or sql.strip().upper() == "INVALID":
        return {
            "question": question,
            "sql": sql,
            "success": False,
            "error": "This question cannot be answered using the database schema."
        }

    # Step 3: Validate and execute the SQL safely
    try:
        result = execute_sql(sql)

        return {
            "question": question,
            "sql": sql,
            "success": True,
            "columns": result["columns"],
            "rows": result["rows"],
            "row_count": result["row_count"]
        }

    except (ValueError, RuntimeError) as error:
        return {
            "question": question,
            "sql": sql,
            "success": False,
            "error": str(error)
        }
    except Exception as error:
        return {
            "question": question,
            "sql": sql,
            "success": False,
            "error": f"Query execution failed: {error}"
        }
