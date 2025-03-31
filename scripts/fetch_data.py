from api.database import fetch_clauses

def fetch_and_preprocess():
    clauses = fetch_clauses()
    return [clause['clause_text'] for clause in clauses]
