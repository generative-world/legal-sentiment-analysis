import psycopg2
import pandas as pd
from config.config import DB_CONFIG

def fetch_clauses():
    """Fetches legal clauses from PostgreSQL."""
    conn = psycopg2.connect(**DB_CONFIG)
    query = "SELECT id, clause_text FROM legal_clauses;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_dict(orient="records")
