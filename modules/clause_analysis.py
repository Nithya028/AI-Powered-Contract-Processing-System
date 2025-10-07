"""
Clause Analysis Module using Gemini 2.5 Flash
---------------------------------------------
Identifies clause types, assigns risk levels, and detects any non-standard clauses.
"""

from google import genai
from config import GEMINI_API_KEY

# Configure Gemini client (same style as your working example)
client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = "gemini-2.5-flash"


def analyze_clauses(text: str):
    """
    Splits contract into clauses and classifies each clause with:
    - Clause type (Confidentiality, Payment, Termination, etc.)
    - Risk level (Low / Medium / High)
    - Optional notes about why it's risky
    """
    prompt = f"""
You are a legal AI assistant specialized in contract clause analysis.

Analyze the following contract text. 
Identify distinct clauses and for each clause, provide:
1. The clause text.
2. The clause type (choose from: Confidentiality, Payment, Termination, Governing Law, Intellectual Property, Liability, Non-compete, Non-solicitation, Arbitration, General, Other).
3. A risk rating (Low / Medium / High) based on the presence of unclear terms, missing protections, or bias toward one party.
4. A short note (1-2 sentences) if the clause has notable risks.

Return the result as a JSON list in this format:
[
  {{
    "clause_text": "...",
    "type": "...",
    "risk": "...",
    "note": "..."
  }}
]

Contract Text:
{text}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        output = response.text

        # Attempt to extract and parse the JSON part of the response
        import json, re
        json_text = re.search(r"\[.*\]", output, re.DOTALL)
        if json_text:
            return json.loads(json_text.group(0))
        else:
            return [{
                "clause_text": text,
                "type": "Unknown",
                "risk": "Medium",
                "note": "Could not parse JSON output"
            }]

    except Exception as e:
        return [{
            "clause_text": text,
            "type": "Error",
            "risk": "Medium",
            "note": f"Error: {str(e)}"
        }]
