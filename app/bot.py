from pyrogram import Client, filters
import openai
from app.tts import text_to_speech
from app.config import TELEGRAM_BOT_TOKEN, OPENAI_API_KEY

# OpenAI and Pyrogram initialization
openai.api_key = OPENAI_API_KEY
app = Client(
    "chatgpt_bot",
    bot_token=TELEGRAM_BOT_TOKEN,
)

# Dictionary to store conversation context
user_context = {}

@app.on_message(filters.private & ~filters.command(["start", "clear"]))
async def handle_message(client, message):
    user_id = message.from_user.id
    user_input = message.text

    # Maintain conversation history for the user
    if user_id not in user_context:
        user_context[user_id] = []

    user_context[user_id].append({"role": "user", "content": user_input})

    try:
        # Generate response using OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=user_context[user_id]
        )
        reply = response['choices'][0]['message']['content'].strip()

        # Add bot reply to context
        user_context[user_id].append({"role": "assistant", "content": reply})

        # Send the reply
        await message.reply(reply)

        # Optionally send a voice message
        audio_file = text_to_speech(reply)
        if audio_file:
            await message.reply_voice(audio_file)

    except Exception as e:
        await message.reply("An error occurred while processing your request.")

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! I'm your AI assistant. You can start chatting with me.")

@app.on_message(filters.command("clear"))
async def clear(client, message):
    user_id = message.from_user.id
    user_context.pop(user_id, None)
    await message.reply("Context cleared! Let's start a new conversation.")

if __name__ == "__main__":
    app.run()
