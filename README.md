# Intelligent Text-to-SQL Database Assistant

An AI-powered application that converts natural-language questions into SQL queries and retrieves results from a SQLite database using Google Gemini and Streamlit.

## Features

- **Natural Language to SQL:** Convert everyday English questions into SQL queries.
- **AI Integration:** Use Google Gemini through LangChain.
- **Database Integration:** Query an SQLite employee database.
- **SQL Safety Checks:** Validate queries and restrict execution to read-only operations.
- **Interactive Interface:** Ask questions and view generated SQL and query results in a Streamlit web application.
- **Error Handling:** Display useful feedback when queries fail.

## Tech Stack

- Python
- Google Gemini API
- LangChain
- SQLite
- Streamlit
- Pandas

## Project Structure

```text
TextToSQL-Assistant/
├── database/
│   ├── company.db
│   ├── setup_database.py
│   └── test_database.py
├── src/
│   ├── assistant.py
│   ├── sql_executor.py
│   └── sql_generator.py
├── app.py
├── test_gemini.py
├── test_sql_generator.py
├── test_sql_executor.py
├── test_assistant.py
├── test_safety.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd TextToSQL-Assistant
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```text
GOOGLE_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own API key. Never commit your `.env` file or publish your API key.

### 5. Set up the database

If the SQLite database is not included in the repository, run:

```powershell
python database/setup_database.py
```

### 6. Launch the application

```powershell
streamlit run app.py
```

Open the local URL displayed in your terminal.

## Example Questions

- Show all employees in the IT department.
- Find the five highest-paid employees.
- Calculate the average salary of employees in Delhi.
- Show employees older than 30.

## How It Works

1. The user enters a natural-language question.
2. Gemini generates an SQL query based on the database schema.
3. The application validates the generated query.
4. SQLite executes permitted queries through a read-only connection and an authorizer.
5. The application displays the generated SQL and query results.

## Limitations

- The current database contains sample employee data.
- Query quality depends on the generated SQL and the database schema.
- SQL validation is a safeguard, not a guarantee against every possible malicious or malformed query.
- The application requires a valid Gemini API key and network access.

## Future Improvements

- Support multiple database schemas.
- Add query explanations and result summaries.
- Improve SQL parsing and validation.
- Add automated unit tests.
- Deploy the application to a hosted platform.

## Author

Ammar Hasan
