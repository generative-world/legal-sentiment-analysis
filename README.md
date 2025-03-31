# legal-sentiment-analysis

```
legal_sentiment_analysis/
│── models/
│   ├── model.py                     # Load the RoBERTa model from AWS S3
│
│── utils/
│   ├── text_processing.py            # Extract and preprocess text
│   ├── clause_extraction.py          # Extract clauses from legal documents
│
│── api/
│   ├── main.py                       # FastAPI app with endpoints
│   ├── database.py                   # PostgreSQL connection & queries
│
│── scripts/
│   ├── train_model.py                 # Fine-tune RoBERTa using PostgreSQL data
│   ├── fetch_data.py                  # Script to fetch and preprocess clauses
│   ├── upload_model_s3.py             # Upload trained model to AWS S3
│
│── data/
│   ├── contracts/                     # Store legal contract PDFs
│
│── dashboard/
│   ├── app.py                        # Streamlit/Flask dashboard for visualization
│
│── Dockerfile                         # Docker setup
│── docker-compose.yml                  # Container orchestration
│── requirements.txt                    # Python dependencies
```
