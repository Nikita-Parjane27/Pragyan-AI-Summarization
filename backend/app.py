from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import uuid
import os

# Custom functions
from text_summarizer import get_text_summary
from pdf_summarizer import get_pdf_summary
from docx_summarizer import get_docx_summary
from audio_summarizer import audio_summary
from excel_csv_summarizer import excel_summary
from article_summarizer import article_summary
from yt_video_summarizer import video_summary
from image_summary import image_summary
from pdf_chatbot import get_chatbot_response
from docx_chatbot import get_chatbot_response1
from sentiment_analysis import get_sentiment_analysis


app = Flask(__name__)
CORS(app)

DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)


# =============================
# TEST ROUTE
# =============================
@app.route('/test', methods=['GET'])
def test():
    return "Hello, World!"


# =============================
# TEXT SUMMARY
# =============================
@app.route('/text-summarize', methods=['POST'])
def summarize_text():
    try:
        data = request.get_json()
        text = data.get('text')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        summary = get_text_summary(text)
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# PDF SUMMARY
# =============================
@app.route('/pdf-summary', methods=['POST'])
def pdf_summary_api():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']

        if not file.filename.endswith('.pdf'):
            return jsonify({"error": "Invalid file type. Upload PDF"}), 400

        summary = get_pdf_summary(file)
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# DOCX SUMMARY
# =============================
@app.route('/docx-summary', methods=['POST'])
def docx_summary_api():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']

        if not file.filename.endswith('.docx'):
            return jsonify({"error": "Invalid file type. Upload DOCX"}), 400

        summary = get_docx_summary(file)
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# EXCEL / CSV SUMMARY
# =============================
@app.route('/excel-summary', methods=['POST'])
def excel_summary_api():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        filepath = os.path.join(DATA_FOLDER, filename)

        file.save(filepath)

        summary = excel_summary(filename)

        os.remove(filepath)

        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# ARTICLE SUMMARY
# =============================
@app.route('/article-summary', methods=['POST'])
def article_summary_api():
    try:
        data = request.get_json()
        link = data.get('link')

        if not link:
            return jsonify({"error": "No link provided"}), 400

        result = article_summary(link)
        return jsonify({"article_summary": result["summary"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# YOUTUBE SUMMARY
# =============================
@app.route('/youtube-summary', methods=['POST'])
def youtube_summary_api():
    try:
        data = request.get_json()
        video_link = data.get('video_link')

        if not video_link:
            return jsonify({"error": "No video link provided"}), 400

        result = video_summary(video_link)
        return jsonify({"video_summary": result["summary"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# AUDIO SUMMARY
# =============================
@app.route('/audio-summary', methods=['POST'])
def audio_summary_api():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        filepath = os.path.join(DATA_FOLDER, filename)

        file.save(filepath)

        result = audio_summary(filename)

        os.remove(filepath)

        return jsonify({"audio_summary": result["summary"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# IMAGE SUMMARY
# =============================
@app.route('/image-summary', methods=['POST'])
def image_summary_api():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        filepath = os.path.join(DATA_FOLDER, filename)

        file.save(filepath)

        result = image_summary(filename)

        os.remove(filepath)

        return jsonify({"summary": result["summary"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# PDF CHATBOT
# =============================
@app.route('/pdf-chatbot', methods=['POST'])
def pdf_chatbot():
    try:
        if 'file' not in request.files:
            message = request.form.get('message')
            response = get_chatbot_response(message=message)
            return jsonify({"response": response})

        file = request.files['file']
        response = get_chatbot_response(file=file)

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# DOCX CHATBOT
# =============================
@app.route('/docx-chatbot', methods=['POST'])
def docx_chatbot():
    try:
        if 'file' not in request.files:
            message = request.form.get('message')
            response = get_chatbot_response1(message=message)
            return jsonify({"response": response})

        file = request.files['file']
        response = get_chatbot_response1(file=file)

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# SENTIMENT ANALYSIS
# =============================
@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis_api():
    try:
        data = request.get_json()
        text = data.get('text')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        sentiment, analysis = get_sentiment_analysis(text)

        return jsonify({
            "sentiment": sentiment,
            "analysis": analysis
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# RUN SERVER
# =============================
@app.route('/')
def home():
    return jsonify({"status": "Backend is running!"}), 200
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
