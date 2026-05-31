from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

MODEL_CHAT = os.getenv("MODEL_CHAT")

MODEL_EMBED = os.getenv("MODEL_EMBED")

CHROMA_DB = os.getenv("CHROMA_DB")