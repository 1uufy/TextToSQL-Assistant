
import re
import sqlite3
from pathlib import Path


# Locate the existing database file
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "database" / "company.db"


def validate_sql(sql: str) -> str:
    """Perform basic checks before executing a SQL query."""

    if not isinstance(sql, str) or not sql.strip():
        raise ValueError("SQL query cannot be empty.")

    query = sql.strip()

    # Remove optional Markdown code fences
    query = re.sub(
        r"^```(?:sql)?\s*",
        "",
        query,
        flags=re.IGNORECASE
    )
    query = re.sub(r"\s*```$", "", query).strip()

    # Remove an optional trailing semicolon
    query = query.strip()
    if ";" in query.rstrip(";"):
        raise ValueError("Multiple SQL statements are not allowed.")
    query = query.rstrip(";").strip()

    # Only SELECT and WITH queries are permitted
    if not re.match(r"^(SELECT|WITH)\b", query, re.IGNORECASE):
        raise ValueError("Only SELECT queries are allowed.")

    if not query:
        raise ValueError("SQL query cannot be empty.")
    
    # Restrict queries to the employees table
    if not re.search(
        r"\bemployees\b",
        query,
        flags=re.IGNORECASE
    ):
        raise ValueError(
            "Queries must reference the employees table."
        )

    return query


def execute_sql(sql: str) -> dict:
    """Execute a validated query using a read-only connection."""

    query = validate_sql(sql)

    if not DATABASE_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DATABASE_PATH}"
        )

    # Open SQLite in read-only mode
    database_uri = DATABASE_PATH.as_uri() + "?mode=ro"

    with sqlite3.connect(database_uri, uri=True) as connection:

        # SQLite authorizer: allow only read-related SQL operations
        allowed_actions = {
            sqlite3.SQLITE_SELECT,
            sqlite3.SQLITE_READ,
            sqlite3.SQLITE_FUNCTION,
        }

        # Support recursive CTEs if the Python version exposes this action
        recursive_action = getattr(sqlite3, "SQLITE_RECURSIVE", None)
        if recursive_action is not None:
            allowed_actions.add(recursive_action)

        def authorize(action, arg1, arg2, database, trigger):
            if action in allowed_actions:
                return sqlite3.SQLITE_OK

            return sqlite3.SQLITE_DENY

        connection.set_authorizer(authorize)

        cursor = connection.execute(query)
        columns = [
            description[0] for description in cursor.description or []
        ]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return {
            "columns": columns,
            "rows": rows,
            "row_count": len(rows),
        }
