from google import genai

client = genai.Client(
    api_key="AIzaSyC1JUwuzFDLonS5hajmrJly9CEVXh_jCA4",
    http_options={"api_version": "v1"}
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say hello in one short sentence."
)

print(response.text)
