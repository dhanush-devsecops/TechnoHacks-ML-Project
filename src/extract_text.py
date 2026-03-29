import os
from pdfminer.high_level import extract_text as extract_pdf_text
from pdfminer.pdfdocument import PDFPasswordIncorrect
import docx2txt

def extract_resumes(folder_path):
    resumes = {}
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        try:
            if filename.lower().endswith('.pdf'):
                try:
                    text = extract_pdf_text(filepath)
                    if text.strip():
                        resumes[filename] = text
                except PDFPasswordIncorrect:
                    print(f"Skipping password-protected PDF: {filename}")
            elif filename.lower().endswith('.docx'):
                text = docx2txt.process(filepath)
                if text.strip():
                    resumes[filename] = text
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    print("Extracted resumes:", resumes.keys())
    return resumes