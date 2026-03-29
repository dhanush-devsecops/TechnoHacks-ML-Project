import sys
from src.extract_text import extract_resumes
from src.preprocess_text import preprocess_text
from src.match_job import match_job_tfidf, save_results
from src.language_utils import detect_language, translate_to_english

# Step 1: Extract resumes
resumes_dict = extract_resumes('resumes')

# Step 2: Preprocess all resumes
resumes_dict_clean = {name: preprocess_text(text) for name, text in resumes_dict.items()}

# Step 3: Input job description (MULTI-LINE)
print("Paste the job description. Press CTRL+D when finished:\n")
job_description = sys.stdin.read()

# Step 4: Detect language
language = detect_language(job_description)
print(f"\nDetected Language: {language}")

# Step 5: Translate if not English
if language != "en":
    print("Translating job description to English...\n")
    job_description = translate_to_english(job_description)

# Step 6: Preprocess translated job description
job_desc_clean = preprocess_text(job_description)

# Step 7: Match resumes
results = match_job_tfidf(resumes_dict_clean, job_desc_clean)

# Step 8: Save & display results
save_results(results)

threshold = 0.35
filtered_results = [(c, s) for c, s in results if s >= threshold]

print("\n================ AI Resume Screening Results ================\n")

if filtered_results:
    print("Top Matching Candidates:\n")
    for i, (candidate, score) in enumerate(filtered_results[:5], 1):
        print(f"{i}. {candidate}  -->  Match Score: {score:.2f}")

else:
    print("⚠️ No strong candidates matched the job description.")
    print("\nClosest available candidates (low similarity):\n")

    for i, (candidate, score) in enumerate(results[:5], 1):
        print(f"{i}. {candidate}  -->  Match Score: {score:.2f}")

print("\nTotal resumes analyzed:", len(resumes_dict_clean))