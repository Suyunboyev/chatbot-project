import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o")
DATABASE_URL = "sqlite:///./data/users.db"
CSV_PATH = "./data/users_table_uz_full.csv"