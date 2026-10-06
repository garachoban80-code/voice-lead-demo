from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import tempfile

from voice_to_text import transcribe_audio
from lead_extractor import extract_lead

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok", "service": "voice-lead-demo"}


@app.post("/process-voice")
async def process_voice(file: UploadFile = File(...)):
    suffix = Path(file.filename or "").suffix or ".wav"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        temp.write(await file.read())
        temp_path = temp.name

    try:
        text = transcribe_audio(temp_path)
        lead = extract_lead(text)

        return {
            "success": True,
            "text": text,
            "lead": lead,
        }

    finally:
        Path(temp_path).unlink(missing_ok=True)
