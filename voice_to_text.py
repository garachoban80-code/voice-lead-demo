from pathlib import Path
from faster_whisper import WhisperModel
from lead_extractor import extract_lead
import json


def transcribe_audio(file_path: str) -> str:
    audio_file = Path(file_path)

    if not audio_file.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_file}")

    model = WhisperModel("small", device="cpu", compute_type="int8")

    segments, info = model.transcribe(
        str(audio_file),
        language="fa",
        beam_size=5,
    )

    text = " ".join(segment.text.strip() for segment in segments)
    return text


if __name__ == "__main__":
    path = input("مسیر فایل صوتی را وارد کن: ").strip()

    try:
        text = transcribe_audio(path)

        print("\nمتن تشخیص‌داده‌شده:")
        print(text)

        lead = extract_lead(text)

        print("\nاطلاعات استخراج‌شده:")
        print(json.dumps(lead, ensure_ascii=False, indent=2))

    except Exception as error:
        print(f"خطا: {error}")
