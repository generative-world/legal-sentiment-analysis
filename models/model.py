import torch
import boto3
from transformers import RobertaTokenizer, RobertaForSequenceClassification

# AWS S3 Config (Loads model from AWS S3)
S3_BUCKET_NAME = "your-bucket-name"
MODEL_FILE_NAME = "roberta_legal_sentiment.pth"
MODEL_LOCAL_PATH = f"models/{MODEL_FILE_NAME}"

def download_model_from_s3():
    """Download the model from S3 if not available locally."""
    s3 = boto3.client("s3")
    try:
        s3.download_file(S3_BUCKET_NAME, MODEL_FILE_NAME, MODEL_LOCAL_PATH)
        print("✅ Model downloaded from S3")
    except Exception as e:
        print(f"❌ Error downloading model: {e}")

# Ensure the model is available
download_model_from_s3()

# Load model
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
model = RobertaForSequenceClassification.from_pretrained("roberta-base", num_labels=5)
model.load_state_dict(torch.load(MODEL_LOCAL_PATH, map_location=torch.device("cpu")))
model.eval()
