from google import genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GENERATIVEAI_API_KEY"))

# Store session chat in memory
chat_session = None


def get_chatbot_response(file=None, message=None):
    global chat_session

    # -------- PDF Upload & Initial Summary --------
    if file is not None and message is None:

        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        # Limit size to avoid token overflow
        text = text[:15000]

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Provide a clear and concise summary of the following PDF text.
            Return summary only.

            {text}
            """,
            config={
                "temperature": 0.7,
                "max_output_tokens": 1000,
            }
        )

        # Create persistent chat session
        chat_session = client.chats.create(
            model="gemini-1.5-flash",
            history=[
                {
                    "role": "user",
                    "parts": [{"text": f"Here is a document:\n{text}"}]
                }
            ]
        )

        return response.text.strip()

    # -------- Follow-up Questions --------
    elif message is not None and file is None:

        if chat_session is None:
            return "Please upload a PDF first."

        response = chat_session.send_message(message)
        return response.text.strip()

    else:
        return "Invalid Input"
