import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def get_text_summary(text):
    client = genai.Client(
        api_key=os.getenv("GENERATIVEAI_API_KEY"),
        http_options={"api_version": "v1"}
    )

    prompt = f"""
Give a clear and concise summary of the following text.
Provide only the summary without extra formatting.

Text:
"{text}"
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # <- Replace with a valid model from client.models.list()
            contents=prompt,
            config={
                "temperature": 0.7,
                "top_p": 0.5,
                "top_k": 5,
                "max_output_tokens": 1024,
            }
        )
        return response.text.strip()

    except Exception as e:
        print("Error generating summary:", e)
        return "Could not generate summary at this time."
