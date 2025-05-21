{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Times-Bold;\f2\froman\fcharset0 Times-Roman;
\f3\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue233;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c0\c0\c93333;}
\paperw11900\paperh16840\margl1440\margr1440\vieww20220\viewh12760\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 This directory contains the code for Intelligent compliance validator.\
\
Requirements:\
\
Groq API: Please generate you Groq API Key {\field{\*\fldinst{HYPERLINK "https://console.groq.com"}}{\fldrslt here}} and cross-check the model once the API key is generated(change the model if required in config)\
\
Python Packages : json, PIL, pdf2image, pytesseract, groq\
\
Command to install : pip install pillow pdf2image pytesseract groq (Ideally JSON should install with python itself, if not use pip install simplejson)\
\
Here is how you can install Tesseract OCR:\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Windows:
\f2\b0  {\field{\*\fldinst{HYPERLINK "https://github.com/UB-Mannheim/tesseract/wiki"}}{\fldrslt \cf3 \ul \ulc3 \strokec3 Tesseract Installer}}\

\f1\b macOS:
\f2\b0  
\f3\fs26 brew install tesseract
\f2\fs24 \

\f1\b Linux (Ubuntu):
\f2\b0  
\f3\fs26 sudo apt install tesseract-ocr\
\
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 To Run the code Follow the steps:\
\
1. }