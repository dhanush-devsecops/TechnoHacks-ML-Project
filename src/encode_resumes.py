from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.preprocessing import normalize

def load_model(model_name="all-MiniLM-L6-v2"):
    """Load a pre-trained sentence transformer model."""
    model = SentenceTransformer(model_name)
    return model

def encode_text(model, texts):
    """Encode texts into embeddings."""
    embeddings = model.encode(texts, show_progress_bar=True)
    # Normalize embeddings
    embeddings = normalize(embeddings, norm='l2')
    return embeddings

def encode_resumes(model, resume_texts):
    """Encode all resume texts into embeddings."""
    resume_names = list(resume_texts.keys())
    texts = list(resume_texts.values())
    
    embeddings = encode_text(model, texts)
    
    return dict(zip(resume_names, embeddings))

if __name__ == "__main__":
    model = load_model()
    sample_texts = {
        "resume1.pdf": "Python Developer with 5 years experience in web development",
        "resume2.pdf": "Data Scientist with expertise in machine learning and AI"
    }
    
    embeddings = encode_resumes(model, sample_texts)
    print(f"Encoded {len(embeddings)} resumes")
    for name, emb in embeddings.items():
        print(f"{name}: {emb.shape}")
