import os
from PIL import Image
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_file(path):
    ext = os.path.splitext(path)[-1].lower()
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    if ext == '.pdf':
        images = convert_from_path(path)
        return "\n".join(pytesseract.image_to_string(img) for img in images)
    elif ext in ['.jpg', '.jpeg', '.png', '.webp']:
        return pytesseract.image_to_string(Image.open(path))
    elif ext == '.txt':
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise ValueError(f"Unsupported file type: {ext}")