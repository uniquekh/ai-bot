# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy app files
COPY app/ /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (if needed for debugging)
EXPOSE 8000

# Set environment variables
ENV TELEGRAM_BOT_TOKEN= 7257652625:AAEk7gVuGUYmjGAMFl1ZXFkzUjZLM5hbcI8
ENV OPENAI_API_KEY= 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

# Run the bot
CMD ["python", "bot.py"]
