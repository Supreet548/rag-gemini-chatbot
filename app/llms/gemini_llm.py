from langchain_google_genai import ChatGoogleGenerativeAI
from app.config.settings import *

llm = ChatGoogleGenerativeAI(
    model=MODEL_CHAT,
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)