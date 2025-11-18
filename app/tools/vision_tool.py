import google.generativeai as genai
import os

def extract_prescription_data(gcs_url: str):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are a prescription-reading assistant.

    Extract structured JSON with:
    - medicines
    - dosage
    - frequency
    - duration (if present)
    - doctor's notes (if any)

    Image URL: {gcs_url}
    """

    response = model.generate_content(prompt)

    return {"extracted_json": response.text}

