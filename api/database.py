import psycopg2
import pandas as pd
from config.config import DB_CONFIG

def fetch_clauses():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        query = "SELECT id, clause_text FROM legal_clauses;"
        df = pd.read_sql(query, conn)
        conn.close()
        return df.to_dict(orient="records")
    except psycopg2.DatabaseError as e:
        raise Exception(f"Database error: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")
