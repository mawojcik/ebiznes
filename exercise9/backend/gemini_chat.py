import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_TOKEN")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def send_to_gemini(history):
    system_instruction = (
    "Answer only questions relating cars and motorization. "
    "If the question is not related to cars, respond with this but translate it language that user used: "
    "'I can only answer questions about cars and motorization.'. "
    "When someone finishes asking questions, respond with one of these messages in appropriate language: "
    "'Do zobaczenia! Jeśli będziesz miał pytania, wróć śmiało.', "
    "'Dziękuję za rozmowę! Miłego dnia i szerokiej drogi!', "
    "'Na razie! Trzymaj się i dbaj o swój samochód.', "
    "'Życzę bezpiecznej jazdy! Do następnego razu!', "
    "'Cześć! Gdybyś czegoś potrzebował, zawsze tu jestem.'"
    "Always translate the response to the language the user is using. "
    )
    history[0]["parts"][0]["text"] = system_instruction + history[0]["parts"][0]["text"]
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
