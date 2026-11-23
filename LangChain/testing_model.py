
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Reply with just the word: SUCCESS"
)

print(response.text)
