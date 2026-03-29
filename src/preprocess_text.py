# src/preprocess_text.py
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Clean and preprocess a text string"""
    # Use only the first 3000 characters of the resume text
    text = text[:3000]
    
    # Lowercase
    text = text.lower()
    # Remove special characters / punctuation / numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # Tokenize
    words = text.split()
    # Remove stopwords
    words = [w for w in words if w not in stop_words]
    # Lemmatize
    words = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(words)