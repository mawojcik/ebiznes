from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from gemini_chat import send_to_gemini

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    history = data.get("history", [])

    if not history:
        return jsonify({"error": "No history found"}), 400
        
    response_text = send_to_gemini(history)

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
