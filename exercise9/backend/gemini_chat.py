import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_TOKEN")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def send_to_gemini(history):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": history
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        try:
            parts = response.json()["candidates"][0]["content"]["parts"]
            return ''.join(part.get("text", "") for part in parts)
        except (KeyError, IndexError):
            return "Error: Couldn't parse the response."
    else:
        return f"Error: {response.status_code} - {response.text}"
