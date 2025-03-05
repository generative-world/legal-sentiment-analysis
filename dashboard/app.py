import streamlit as st
from api.database import fetch_clauses

st.title("Legal Clause Sentiment Analysis")
clauses = fetch_clauses()
for clause in clauses:
    st.write(f"{clause['id']}: {clause['clause_text']}")
