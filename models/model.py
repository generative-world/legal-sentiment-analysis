# models/model.py
import torch
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from config.config import AWS_CONFIG

MODEL_PATH = "models/roberta_legal_sentiment.pth"

def download_model_from_s3():
    try:
        s3 = boto3.client('s3')
        s3.download_file(AWS_CONFIG['s3_bucket'], "roberta_legal_sentiment.pth", MODEL_PATH)
    except NoCredentialsError:
        raise Exception("AWS credentials not found!")
    except PartialCredentialsError:
        raise Exception("Incomplete AWS credentials provided!")

def load_model():
    download_model_from_s3()
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=5)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
    model.eval()
    return tokenizer, model
