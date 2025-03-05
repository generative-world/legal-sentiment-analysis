from fastapi import FastAPI
from models.model import load_model
from api.database import fetch_clauses

app = FastAPI()

@app.on_event("startup")
def startup_event():
    global tokenizer, model
    tokenizer, model = load_model()

@app.get("/")
def root():
    return {"message": "Legal Sentiment API is running!"}

@app.get("/clauses")
def get_clauses():
    return fetch_clauses()

# utils/text_processing.py
from pdfminer.high_level import extract_text

def preprocess_text(pdf_path):
    text = extract_text(pdf_path)
    return text.replace('\n', ' ')

# utils/clause_extraction.py
import re

def extract_clauses(text):
    clauses = re.split(r'\d+\.\s[A-Z ]+', text)[1:]
    return clauses
