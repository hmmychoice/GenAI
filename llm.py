import config
from langchain_google_genai import GoogleGenerativeAI
#models/text-bison-001models/text-bison-001
llm = GoogleGenerativeAI(model="gemini-pro", 
                         google_api_key=config.api_key, 
                         temperature=0.9)
