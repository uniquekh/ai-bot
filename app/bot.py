from pyrogram import Client, filters
import google.generativeai as genai

# Replace with your actual API keys
API_ID = "21179966"
API_HASH = "d97919fb0a3c725e8bb2a25bbb37d57c"
BOT_TOKEN = "7257652625:AAEk7gVuGUYmjGAMFl1ZXFkzUjZLM5hbcI8"  # Replace with your group's chat ID (negative value)  # Replace with your Telegram user ID (obtainable from @get_my_id bot)
GEMINI_API_KEY = "AIzaSyACejlDYl4Szlj1t2f-4ep4RO0yK0r-8wU"

# Initialize Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Initialize Google's Gemini client for text generation
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# No filters used here (handles all messages)
@app.on_message(filters.text & ~filters.command(["start", "help"]))
async def echo_message(client, message):
    user_input = message.text

    try:
        response = model.generate_content(user_input)
        await message.reply(response.text)
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! I'm your Gemini-powered AI assistant. Ask me anything.")

@app.on_message(filters.command("help"))
async def help(client, message):
    await message.reply("Available commands:\n/start - Start the bot\n/help - Show this help message")
print("Bot started!")
app.run()
