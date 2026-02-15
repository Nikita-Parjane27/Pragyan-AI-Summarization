from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def get_sentiment_analysis(text):
    client = genai.Client(
    api_key=os.getenv("GENERATIVEAI_API_KEY"),
    http_options={"api_version": "v1"}
)

    prompt = f"""
    Analyze the sentiment of the text and classify it as one of the following categories:
    Analytical, Critical, Enthusiastic, Fearful, Joyful, Sad, Questioning, or Neutral.

    Give only ONE sentiment word that best describes the text.

    Text: "{text}"
    """

    response1 = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    sentiment = response1.text.strip()

    explanation_prompt = f"""
    Briefly explain why this text is classified as {sentiment}.
    Do not use bold or italic formatting.
    """

    response2 = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=explanation_prompt
    )

    analysis = response2.text.strip()

    return sentiment, analysis
