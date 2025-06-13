# FunctionalKit

FunctionalKit is a minimal, fast and useful web toolkit to help people with:
- Converting images or text to PDF
- Transcribing audio files
- Extracting audio or video from links (e.g. YouTube)

All in one click — no signups, no clutter.

## MVP Features
- [x] Convert images (.jpg/.png) or text (.txt/.docx) into PDF
- [x] Upload and transcribe audio files using Whisper
- [x] Download audio or video from online URLs

## Getting Started

Install dependencies:
```
pip install -r requirements.txt
```

Run the app:
```
streamlit run app/main.py
```

## Tech Stack
- Python
- Streamlit
- yt-dlp
- Whisper (OpenAI)
- fpdf2 / docx2pdf
