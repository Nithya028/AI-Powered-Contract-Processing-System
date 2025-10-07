"""
Risk Matrix Module
------------------
Assigns risk to individual clauses based on keywords and computes overall contract risk.
"""

# Predefined clause keyword-based risk mapping
CLAUSE_KEYWORD_RISK = {
    "non-compete": "Medium",
    "force majeure": "Low",
    "payment": "High",
    "confidentiality": "High",
    "termination": "High",
    "governing law": "Medium"
}

def assign_clause_risk(clause_text):
    """
    Assign a risk level (Low, Medium, High) to a single clause based on keywords.
    Default to Medium if no keywords match.
    """
    clause_text_lower = clause_text.lower()
    for keyword, risk in CLAUSE_KEYWORD_RISK.items():
        if keyword in clause_text_lower:
            return risk
    return "Medium"

def map_risk_score_to_level(score):
    """
    Convert numeric or AI-assigned risk to a level: Low, Medium, High.
    """
    if isinstance(score, str):
        return score
    elif isinstance(score, (float, int)):
        if score < 0.4:
            return "Low"
        elif score < 0.7:
            return "Medium"
        else:
            return "High"
    else:
        return "Medium"

def assign_overall_risk(clauses):
    """
    Compute overall contract risk from clause-level risk.
    """
    risk_levels = {"Low": 1, "Medium": 2, "High": 3}
    max_risk_value = 1  # default Low

    for clause in clauses:
        # If clause already has risk, use it; otherwise assign via keywords
        risk = clause.get("risk")
        if not risk:
            risk = assign_clause_risk(clause.get("clause_text", ""))
        level = map_risk_score_to_level(risk)
        max_risk_value = max(max_risk_value, risk_levels.get(level, 2))

    overall_level_map = {1: "Low", 2: "Medium", 3: "High"}
    overall_risk = overall_level_map[max_risk_value]
    return overall_risk
