# modules/summarizer.py
"""
Contract Summarization Module using Gemini 2.5 Flash
-----------------------------------------------------
Generates a concise summary of key contract terms and risks.
"""

from google import genai
from config import GEMINI_API_KEY, MODEL_NAME

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

def summarize_contract(text: str) -> str:
    """
    Summarize the contract (~50 words), including:
    - Parties involved
    - Effective dates
    - Payment obligations
    - Termination clauses
    - Non-standard or risky clauses
    """
    prompt = f"""
You are a legal AI assistant. Summarize the following contract in about 150 words.
Include:
- Parties involved
- Effective dates
- Payment obligations
- Termination clauses
- Any non-standard or risky clauses

Return a clear, concise summary.

Contract text:
{text}
"""

    # Generate summary using Gemini 2.5 Flash
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
