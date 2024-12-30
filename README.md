# ChatGPT Telegram Bot with Docker Support

A Telegram bot powered by OpenAI's ChatGPT and Pyrogram. The bot supports text and voice conversations and is fully containerized for deployment on platforms like Koyeb.

## Features
- Dynamic text and voice replies
- Maintains conversation context
- Dockerized for easy deployment

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatgpt-telegram-bot.git
   cd chatgpt-telegram-bot
   ```

2. Add your API keys in the `.env` file or as environment variables:
   - `TELEGRAM_BOT_TOKEN`
   - `OPENAI_API_KEY`

3. Build and run the Docker container:
   ```bash
   docker build -t chatgpt-bot .
   docker run -e TELEGRAM_BOT_TOKEN=your-token -e OPENAI_API_KEY=your-key chatgpt-bot
   ```

4. Deploy on Koyeb:
   - Push the Docker image to a registry (e.g., Docker Hub).
   - Connect the repository to Koyeb and deploy.

## Requirements
- Python 3.9+
- Docker
