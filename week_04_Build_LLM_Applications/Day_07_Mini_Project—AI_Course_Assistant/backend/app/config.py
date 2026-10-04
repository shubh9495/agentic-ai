import os
from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3.1-flash-lite")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:Admin@123@localhost:5432/course_db"
)

FRONTEND_ORIGIN = os.getenv(
    "FRONTEND_ORIGIN",
    "http://localhost:5173"
)
