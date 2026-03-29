import os
from pdfminer.high_level import extract_text
from pdfminer.pdfdocument import PDFPasswordIncorrect

folder = "resumes"

for filename in os.listdir(folder):
    if filename.lower().endswith(".pdf"):
        filepath = os.path.join(folder, filename)
        try:
            text = extract_text(filepath)
            print(f"{filename} → ✅ Readable")
        except PDFPasswordIncorrect:
            print(f"{filename} → 🔒 Password-protected")
        except Exception as e:
            print(f"{filename} → ⚠ Error: {e}")