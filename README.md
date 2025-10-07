# AI-Powered Contract Processing System

## Problem Statement
Legal teams spend countless hours manually reviewing and analyzing contracts, which is time-consuming and prone to human error. This project automates the extraction, analysis, and summarization of legal contracts using Generative AI.

---

## Solution Overview
This system leverages **Generative AI (Gemini 2.5 Flash)** and NLP techniques to automate contract processing. Key features include:

1. **Document Ingestion**  
   Supports PDF and Word (`.docx`) files. Automatically extracts the textual content for analysis.

2. **Entity Extraction**  
   AI identifies and extracts key entities from contracts, such as:  
   - Parties involved  
   - Dates (effective, termination, deadlines)  
   - Payment obligations  
   - Obligations and responsibilities  

3. **Clause Analysis**  
   - Splits contracts into individual clauses.  
   - Classifies clauses into types (Confidentiality, Payment, Termination, Governing Law, Non-compete, etc.).  
   - Assigns **risk ratings** (Low / Medium / High) based on AI analysis of unclear terms, missing protections, or imbalance.  
   - Detects non-standard clauses.  
   - Handles “Other” clause types dynamically if not predefined.  

4. **Summarization**  
   Generates a concise summary (~150 words) of:  
   - Parties involved  
   - Effective dates  
   - Payment obligations  
   - Termination clauses  
   - Any risky or non-standard clauses  

5. **Risk Scoring**  
   - Computes **overall contract risk** based on individual clause risks.  
   - Uses the maximum clause-level risk as the overall risk.  
   - Optional dynamic risk scoring based on clause context.  

---

