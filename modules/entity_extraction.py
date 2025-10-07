# modules/entity_extraction.py

import json
from google import genai
from config import GEMINI_API_KEY, MODEL_NAME

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

def extract_entities(text: str) -> dict:
    """
    Extracts key entities from contract text:
    - Parties involved
    - Dates
    - Payment obligations
    - Obligations and responsibilities
    Returns a structured JSON dictionary.
    """
    prompt = f"""
You are a legal AI assistant. Carefully read the following contract text and extract the following key entities:

1. **Parties involved** — Names of all organizations or individuals (e.g., "Orion Data Systems Pvt. Ltd.", "InnovEdge Analytics").
2. **Dates** — Any specific or relative dates (e.g., "April 5, 2025", "valid for 2 years", "effective from").
3. **Payments** — Amounts, rates, or financial terms (e.g., "Rs. 15,000 per sq. ft.", "milestone-based payments").
4. **Obligations** — Responsibilities or duties of each party (e.g., "Party A must deliver...", "Party B shall pay...").

Return the output strictly as a **valid JSON object** using this format:
{{
  "parties": ["Party A", "Party B"],
  "dates": ["Effective from April 5, 2025", "valid for 2 years"],
  "payments": ["No payment obligations"],
  "obligations": ["Both parties agree to maintain confidentiality"]
}}

Do not include any explanation or text outside the JSON.

Contract text:
{text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    try:
        response_text = response.text.strip()
        if response_text.startswith("```"):
            response_text = "\n".join(response_text.split("\n")[1:-1])
        result = json.loads(response_text)
        for key in ["parties", "dates", "payments", "obligations"]:
            result.setdefault(key, [])
        return result
    except json.JSONDecodeError:
        print("Failed to parse JSON from AI response:")
        print(response.text)
        raise



    # Parse JSON safely
