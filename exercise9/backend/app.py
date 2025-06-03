from flask import Flask, request, jsonify, send_from_directory
import os
from gemini_chat import send_to_gemini

app = Flask(__name__, static_folder="../frontend", static_url_path="")
from flask_cors import CORS
CORS(app)

@app.route("/")
def serve_index():
    return app.send_static_file("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Brak prompta"}), 400

    instructions = (
        "You are a helpful assistant. Answer only questions relating cars and motorization. "
        "If the question is not related to cars, respond with "
        "'I can only answer questions about cars and motorization.'"
    )
    full_prompt = f"{instructions}\nAnswer this message from user: {prompt}"

    response = send_to_gemini(full_prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
