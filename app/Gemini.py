
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()


genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')


def get_story(prompt: str):
    """Generates a story based on a given prompt."""
    return model.generate_content(prompt)

