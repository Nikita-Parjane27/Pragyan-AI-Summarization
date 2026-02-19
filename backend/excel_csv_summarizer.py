import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def excel_summary(filename):
    client = genai.Client(
    api_key=os.getenv("GENERATIVEAI_API_KEY"),
    http_options={"api_version": "v1"}
)

    # Read CSV file
    df = pd.read_csv("./data/" + filename)

    # Convert full dataset into structured text
    data_preview = df.head(10).to_string()  # limit to avoid token overflow
    column_info = "\n".join([f"{col}: {df[col].dtype}" for col in df.columns])

    prompt = f"""
    This is a CSV dataset.

    Dataset preview:
    {data_preview}

    Column Data Types:
    {column_info}

    Please analyze and provide:

    1. Key themes or topics
    2. Patterns or trends
    3. Potential errors or inconsistencies
    4. Data type observations
    5. Descriptive statistics (if numerical)
    6. Potential relationships
    7. Data quality checks
    8. Domain insight (guess carefully)
    9. Sentiment analysis only if text-based dataset
    10. Advanced analysis suggestions
    11. Conclusion (mandatory)

    Formatting Rules:
    - Do NOT use bold or italic symbols.
    - Use <strong>Title</strong><br/>
      <p>Paragraph</p>
      <br/><br/>
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature": 0.7,
            "max_output_tokens": 2048,
        }
    )

    summary_text = response.text.strip()

    return {"excel_summary": summary_text}
