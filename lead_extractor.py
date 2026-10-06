import re
import json


def extract_lead(text: str) -> dict:
    text = text.strip()

    lead = {
        "project_type": None,
        "need": None,
        "timeline": None,
        "budget": None,
        "raw_text": text,
    }

    # نوع پروژه
    if re.search(r"فروشگاه|فروشگاهی|وب ?سایت|سایت", text):
        lead["project_type"] = "وب‌سایت فروشگاهی"

    # زمان شروع
    if re.search(r"همین ماه|این ماه", text):
        lead["timeline"] = "همین ماه"

    # نیاز
    if lead["project_type"]:
        lead["need"] = "ساخت وب‌سایت فروشگاهی"

    return lead


if __name__ == "__main__":
    text = input("متن را وارد کن: ").strip()

    result = extract_lead(text)

    print("\nاطلاعات استخراج‌شده:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
