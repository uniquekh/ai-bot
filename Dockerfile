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

# Run the bot
CMD ["python", "bot.py"]
