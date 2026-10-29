
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load credentials from the .env file
load_dotenv()

# Check that the API key is configured
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError(
        "GOOGLE_API_KEY is missing. Check your .env file."
    )

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0
)

# Send a test prompt to Gemini
response = llm.invoke(
    "Explain what SQL is in one simple sentence."
)

# Display the model's response
print("Gemini response:")
print(response.content)
