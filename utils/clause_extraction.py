import re

def extract_clauses(text):
    clauses = re.split(r'\d+\.\s[A-Z ]+', text)[1:]
    return clauses
