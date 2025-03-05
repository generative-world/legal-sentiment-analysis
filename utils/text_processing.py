from pdfminer.high_level import extract_text

def preprocess_text(pdf_path):
    text = extract_text(pdf_path)
    return text.replace('\n', ' ')
