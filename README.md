# Resume Job Matching System

A machine learning-based system to match job descriptions with resumes using semantic similarity and embeddings.

## 📋 Project Structure

```
ResumeJobMatching/
│
├── resumes/                     # Directory for resume files (PDF/DOCX)
│   ├── Achyuth Resume_8.pdf
│   ├── Divya Resume_15.pdf
│   └── ...
│
├── data/                        # Job descriptions and metadata
│   └── job_descriptions.csv     # CSV file with job postings
│
├── src/                         # Python scripts
│   ├── extract_text.py          # Extract text from PDF/DOCX files
│   ├── preprocess_text.py       # Clean and preprocess text data
│   ├── encode_resumes.py        # Convert text to embeddings
│   └── match_job.py             # Match resumes to jobs
│
├── outputs/                     # Results directory
│   ├── ranked_resumes.csv       # Ranked resumes for each job
│   └── top_matches.txt          # Top matching resumes
│
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Resume Files

Place your resume files (PDF or DOCX format) in the `resumes/` directory:
- Supported formats: `.pdf`, `.docx`
- Total capacity: 228 resumes (as per requirements)

### 3. Add Job Descriptions

Update `data/job_descriptions.csv` with job postings in the format:
```csv
job_id,job_title,job_description,required_skills,experience_level
```

### 4. Run the Pipeline

```bash
# Extract text from resumes
python src/extract_text.py

# Preprocess text
python src/preprocess_text.py

# Encode resumes into embeddings
python src/encode_resumes.py

# Match resumes to jobs
python src/match_job.py
```

## 📊 Workflow

1. **Extract Text** (`extract_text.py`)
   - Reads PDF and DOCX resume files
   - Extracts raw text content

2. **Preprocess** (`preprocess_text.py`)
   - Cleans text (lowercase, removes special characters)
   - Removes stopwords
   - Tokenizes content

3. **Encode** (`encode_resumes.py`)
   - Uses `sentence-transformers` model to convert text to embeddings
   - Creates vector representations of resumes
   - Normalizes embeddings for comparison

4. **Match & Rank** (`match_job.py`)
   - Calculates cosine similarity between job description and resumes
   - Ranks resumes by relevance score
   - Outputs top matching candidates

## 📦 Dependencies

- **PyPDF2**: PDF text extraction
- **python-docx**: DOCX text extraction
- **nltk**: Natural language processing
- **sentence-transformers**: Text embedding generation
- **scikit-learn**: Similarity calculations and preprocessing
- **numpy & pandas**: Data manipulation

## 📈 Output

### `ranked_resumes.csv`
```csv
resume,similarity_score
Achyuth Resume_8.pdf,0.87
Divya Resume_15.pdf,0.82
...
```

### `top_matches.txt`
Top 10 matching resumes for each job posting.

## 🔧 Configuration

- **Model**: `all-MiniLM-L6-v2` (384-dimensional embeddings)
- **Top-K**: 10 (number of top matches to return)
- **Similarity Metric**: Cosine Similarity

## 💡 Features

✅ Batch processing of multiple resume files  
✅ Support for PDF and DOCX formats  
✅ Text cleaning and normalization  
✅ Semantic text embeddings  
✅ Efficient similarity matching  
✅ CSV export of results  

## 🔍 Example Usage

```python
from src.extract_text import extract_all_resumes
from src.preprocess_text import preprocess_resume
from src.encode_resumes import load_model, encode_resumes
from src.match_job import match_resumes_to_job, rank_resumes

# Load resumes
resumes = extract_all_resumes("resumes/")

# Preprocess
preprocessed = {name: preprocess_resume(text) for name, text in resumes.items()}

# Encode
model = load_model()
embeddings = encode_resumes(model, preprocessed)

# Match to job
job_description = "Looking for Python developer with 5 years experience"
job_embedding = model.encode(job_description)
similarities = match_resumes_to_job(job_embedding, embeddings)

# Rank and save
results = rank_resumes(similarities, list(embeddings.keys()), top_k=10)
results.to_csv("outputs/ranked_resumes.csv", index=False)
```

## 📝 Notes

- Ensure all resume files are named uniquely
- Large number of resumes (200+) may take time for encoding
- Use GPU for faster processing if available
- Pre-trained models are downloaded automatically on first run

## 🤝 Contributing

Feel free to extend this project with:
- Additional preprocessing techniques
- Different embedding models
- Resume parsing for structured extraction
- Web interface for job matching

## 📄 License

This project is open source and available for educational purposes.

---

**Created for**: TECHNOHACKS PRIVATE LIMITED  
**Last Updated**: March 2026
# TechnoHacks-ML-Project
