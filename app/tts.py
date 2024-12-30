from gtts import gTTS
import os

def text_to_speech(text, lang="en"):
    try:
        tts = gTTS(text=text, lang=lang)
        file_path = f"audio_response.mp3"
        tts.save(file_path)
        return file_path
    except Exception as e:
        return None
