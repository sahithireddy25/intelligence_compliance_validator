This directory contains the code for Intelligent compliance validator.

Requirements:

Groq API: Please generate you Groq API Key here(https://console.groq.com/) and cross-check the model once the API key is generated(change the model if required in config)

Python Packages : json, PIL, pdf2image, pytesseract, groq

Command to install : pip install pillow pdf2image pytesseract groq (Ideally JSON should install with python itself, if not use pip install simplejson)

Here is how you can install Tesseract OCR:
Windows: Tesseract Installer(https://github.com/UB-Mannheim/tesseract/wiki)
macOS: brew install tesseract
Linux (Ubuntu): sudo apt install tesseract-ocr

For the details of the model, please refer to Intelligent_document_compliance_flow.pdf


To Run the code Follow the steps:

1. git clone https://github.com/sahithireddy25/intelligence_compliance_validator.git
2. cd intelligence_compliance_validator
3. Update the config with API Key, Model(if required), File location(Not Mandatory to give all 4, model can work with the files that are present), Rules
4. python main.py