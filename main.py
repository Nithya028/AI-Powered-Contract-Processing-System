import os
import json
import config  # updated import
from modules import ingestion, entity_extraction, summarizer, clause_analysis, risk_matrix

DATA_DIR = config.DATA_DIR
OUTPUT_FILE = config.OUTPUT_FILE
GEMINI_API_KEY = config.GEMINI_API_KEY

def process_contract(file_path):
    # 1️⃣ Ingest contract
    text = ingestion.ingest_document(file_path)
    
    # 2️⃣ AI-powered entity extraction
    entities = entity_extraction.extract_entities(text)
    
    # 3️⃣ Clause analysis (zero-shot)
    clauses = clause_analysis.analyze_clauses(text)

    # 4️⃣ Assign risk to each clause using risk matrix
    for clause in clauses:
        # If clause risk not set by AI, assign via keyword
        if not clause.get("risk"):
            clause["risk"] = risk_matrix.assign_clause_risk(clause.get("clause_text", ""))
    
    # 5️⃣ Compute overall contract risk
    overall_risk = risk_matrix.assign_overall_risk(clauses)

    # 6️⃣ Contract summarization
    summary = summarizer.summarize_contract(text)

    # 7️⃣ Combine results
    result = {
        "file_name": os.path.basename(file_path),
        "entities": entities,
        "clauses": clauses,
        "overall_risk": overall_risk,
        "summary": summary
    }
    return result

def main():
    all_results = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith((".pdf", ".docx")):
            print(f"Processing {filename}...")
            file_path = os.path.join(DATA_DIR, filename)
            result = process_contract(file_path)
            all_results.append(result)
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    
    print(f"Processing complete. Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
