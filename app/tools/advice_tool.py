import google.generativeai as genai
import os
import json

def generate_health_advice(extracted_json: str):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are HealthSense, a friendly AI health assistant.

    Based on this extracted prescription JSON:
    {extracted_json}

    Provide:
    - an easy explanation of the medicines
    - safety considerations
    - lifestyle / diet support
    - when to see a doctor
    - a positive helpful tone
    """

    response = model.generate_content(prompt)

    return {"advice": response.text}

