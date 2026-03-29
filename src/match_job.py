import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

def get_candidate_name(filename):
    name, _ = os.path.splitext(filename)
    name = name.replace("_", " ").strip()
    return name

def match_job_tfidf(resumes_dict, job_description):
    names = list(resumes_dict.keys())
    texts = list(resumes_dict.values())
    
    vectorizer = TfidfVectorizer()
    all_texts = texts + [job_description]
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    job_vec = tfidf_matrix[-1]
    resume_vecs = tfidf_matrix[:-1]
    
    similarities = cosine_similarity(resume_vecs, job_vec)
    
    results = []
    for i, name in enumerate(names):
        candidate_name = get_candidate_name(name)
        results.append((candidate_name, similarities[i][0]))
    
    results.sort(key=lambda x: x[1], reverse=True)
    return results

def save_results(results, csv_path='outputs/ranked_resumes.csv', top_path='outputs/top_matches.txt'):
    df = pd.DataFrame(results, columns=['Candidate Name', 'Similarity Score'])
    df.to_csv(csv_path, index=False)
    with open(top_path, 'w') as f:
        for candidate, score in results[:5]:
            f.write(f"{candidate} | {score:.2f}\n")