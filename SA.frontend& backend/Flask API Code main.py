from flask import Flask, request, jsonify
from app.chatbot import get_bot_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = get_bot_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
