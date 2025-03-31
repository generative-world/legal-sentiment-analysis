import boto3
from config.config import AWS_CONFIG

def upload_model():
    s3 = boto3.client('s3')
    s3.upload_file("models/roberta_legal_sentiment.pth", AWS_CONFIG['s3_bucket'], "roberta_legal_sentiment.pth")
