from flask import Flask, request
from pyrogram import Client
import google.generativeai as genai

# Replace with your actual API keys
API_ID = "21179966"
API_HASH = "d97919fb0a3c725e8bb2a25bbb37d57c"
BOT_TOKEN = "7257652625:AAEk7gVuGUYmjGAMFl1ZXFkzUjZLM5hbcI8" 
GROUP_ID = -5967615566  # Replace with your group's chat ID (negative value)
GEMINI_API_KEY = "AIzaSyACejlDYl4Szlj1t2f-4ep4RO0yK0r-8wU" 

# Initialize Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Initialize Google's Gemini client for text generation
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize Flask app
flask_app = Flask(__name__)

@flask_app.route('/', methods=['POST'])
def webhook():
    try:
        update = app.receive_updates(timeout=10)
        if update:
            if update.message and update.message.text:
                user_input = update.message.text
                if user_input.startswith("officer "):
                    try:
                        user_input = user_input[8:] 
                        response = model.generate_content(user_input)
                        update.message.reply_text(response.text)
                    except Exception as e:
                        update.message.reply_text(f"An error occurred: {str(e)}")
    except Exception as e:
        print(f"Error processing update: {str(e)}")
    return "OK", 200

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
