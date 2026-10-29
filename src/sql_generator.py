import os
import re
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the API key from the project's .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found. Check your .env file."
    )

# Initialize the working Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key,
    temperature=0
)


# Describe the database structure
DATABASE_SCHEMA = """
Table: employees

Columns:
- employee_id: INTEGER, unique employee identifier
- name: TEXT, employee name
- department: TEXT, department name
- salary: REAL, employee salary
- age: INTEGER, employee age
- city: TEXT, employee city
"""


def generate_sql(question: str) -> str:
    prompt = f"""
You are an expert SQLite SQL query generator.

Use only the schema provided below.

DATABASE SCHEMA:
{DATABASE_SCHEMA}

USER QUESTION:
{question}

Rules:
1. Generate a valid SQLite SELECT query.
2. Use only the listed table and columns.
3. Do not generate INSERT, UPDATE, DELETE, DROP,
   ALTER, CREATE, or other modification statements.
4. Return only the SQL query without explanations.
5. If the question cannot be answered from the schema,
   return INVALID.

SQL:
"""

    response = llm.invoke(prompt)

    # Convert the response into a string
    content = response.content

    if isinstance(content, str):
        sql = content.strip()
    elif isinstance(content, list):
        parts = []

        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict):
                parts.append(block.get("text", ""))

        sql = "".join(parts).strip()
    else:
        raise TypeError(
            f"Unexpected Gemini response type: {type(content).__name__}"
        )

    # Remove Markdown code fences if Gemini includes them
    sql = re.sub(
        r"^```(?:sql)?\s*",
        "",
        sql,
        flags=re.IGNORECASE
    )
    sql = re.sub(r"\s*```$", "", sql)

    return sql.strip()
