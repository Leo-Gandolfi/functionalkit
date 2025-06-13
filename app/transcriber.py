import os
import tempfile
import whisper

def transcribe_audio(uploaded_file):
    model = whisper.load_model("base")
    temp_dir = tempfile.mkdtemp()
    audio_path = os.path.join(temp_dir, uploaded_file.name)

    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())

    result = model.transcribe(audio_path)
    text = result["text"]

    transcript_path = os.path.join(temp_dir, "transcript.txt")
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(text)

    return transcript_path
