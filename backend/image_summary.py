from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def image_summary(image_filename):
    client = genai.Client(
    api_key=os.getenv("GENERATIVEAI_API_KEY"),
    http_options={"api_version": "v1"}
)

    image_path = os.path.join("data", image_filename)

    # Read image as bytes
    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": "Describe this image clearly and concisely."},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_bytes
                        }
                    }
                ]
            }
        ],
        config={
            "temperature": 0.7,
            "max_output_tokens": 1024,
        }
    )

    summary = response.text.strip()

    return {"summary": summary}
