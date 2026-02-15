import speech_recognition as sr
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def audio_summary(file):
    client = genai.Client(
    api_key=os.getenv("GENERATIVEAI_API_KEY"),
    http_options={"api_version": "v1"}
)

    recognizer = sr.Recognizer()

    with sr.AudioFile("./data/" + file) as source:
        audio_data = recognizer.record(source)

    # Convert speech to text using Google Speech Recognition
    text = recognizer.recognize_google(audio_data)
    print("Extracted Text:", text)

    prompt = f"""
    This is the transcribed text from an audio file.
    Provide a clear and concise summary.

    Text:
    "{text}"
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
        config={
            "temperature": 0.7,
            "max_output_tokens": 1024,
        }
    )

    summary_text = response.text.strip()

    return {
        "transcription": text,
        "summary": summary_text
    }
