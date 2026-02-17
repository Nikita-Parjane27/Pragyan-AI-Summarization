from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
import os

load_dotenv()


def extract_video_id(url):
    parsed_url = urlparse(url)

    if "youtu.be" in parsed_url.netloc:
        return parsed_url.path.strip("/")

    if "youtube.com" in parsed_url.netloc:
        query = parse_qs(parsed_url.query)
        if "v" in query:
            return query["v"][0]

    return None


def video_summary(link):
    client = genai.Client(
        api_key=os.getenv("GENERATIVEAI_API_KEY"),
        http_options={"api_version": "v1"}
    )

    video_id = extract_video_id(link)

    if not video_id:
        return {"summary": "Invalid YouTube URL"}

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception:
        return {"summary": "Transcript not available for this video"}

    # Convert transcript JSON into plain text
    transcript_text = " ".join([item["text"] for item in transcript])

    # Limit size to prevent token overflow
    transcript_text = transcript_text[:12000]

    prompt = f"""
Summarize the following YouTube video transcript clearly and concisely.
Provide plain text summary only.

Transcript:
{transcript_text}
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
        config={
            "temperature": 0.7,
            "max_output_tokens": 1024,
        }
    )

    summary = response.text.strip()

    return {"summary": summary}
