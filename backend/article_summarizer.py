import requests
from bs4 import BeautifulSoup
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def article_summary(link):
    client = genai.Client(
    api_key=os.getenv("GENERATIVEAI_API_KEY"),
    http_options={"api_version": "v1"}
)

    # Fetch webpage
    response = requests.get(link, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract paragraph text
    paragraphs = soup.find_all("p")
    article_text = " ".join([p.get_text() for p in paragraphs])

    # Limit text to prevent token overflow
    article_text = article_text[:8000]

    prompt = f"""
    Summarize the following article clearly and concisely.
    Provide only the summary text.

    Article:
    {article_text}
    """

    ai_response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
        config={
            "temperature": 0.7,
            "max_output_tokens": 1024,
        }
    )

    summary = ai_response.text.strip()

    return {"summary": summary}
