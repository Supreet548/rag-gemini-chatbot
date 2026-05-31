from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config.settings import *

embeddings = GoogleGenerativeAIEmbeddings(
    model=MODEL_EMBED,
    google_api_key=GOOGLE_API_KEY
)