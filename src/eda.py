import os
from extract_text import extract_resumes
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re

# --- Step 1: Extract resumes ---
resumes = extract_resumes('../resumes')
print(f"Total resumes extracted: {len(resumes)}")

# --- Step 2: Basic stats ---
resume_lengths = [len(text.split()) for text in resumes.values()]
avg_words = sum(resume_lengths) / len(resume_lengths)
print(f"Average words per resume: {avg_words:.2f}")

# Plot distribution of resume lengths
plt.figure(figsize=(10,6))
plt.hist(resume_lengths, bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Resume Lengths')
plt.xlabel('Number of Words')
plt.ylabel('Number of Resumes')
plt.show()

# --- Step 3: WordCloud for most frequent words ---
all_text = " ".join(resumes.values()).lower()
all_text = re.sub(r'\b(the|and|a|an|of|in|to|with|for|on|as|by|is|at|from|that|this|be|are)\b', '', all_text)  # remove stopwords
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Frequent Words in Resumes')
plt.show()

# --- Step 4: Common skills extraction ---
skills_keywords = [
    'python', 'java', 'c++', 'c#', 'javascript', 'ml', 'machine learning',
    'deep learning', 'nlp', 'sql', 'aws', 'docker', 'kubernetes', 
    'excel', 'tableau', 'power bi', 'spark', 'hadoop', 'tensorflow', 'pytorch'
]

skills_counter = Counter()
for text in resumes.values():
    text_lower = text.lower()
    for skill in skills_keywords:
        if skill in text_lower:
            skills_counter[skill] += 1

print("\nMost Common Skills Across Resumes:")
for skill, count in skills_counter.most_common(15):
    print(f"{skill}: {count}")

# Plot skills distribution
plt.figure(figsize=(12,6))
skills, counts = zip(*skills_counter.most_common(15))
plt.bar(skills, counts, color='lightgreen')
plt.xticks(rotation=45)
plt.title('Top 15 Skills in Resumes')
plt.show()

# --- Step 5: Extract roles/job titles ---
role_patterns = [
    r'(software engineer|developer|data scientist|business analyst|project manager|qa engineer|java developer|python developer|full stack developer|machine learning engineer)'
]

roles_counter = Counter()
for text in resumes.values():
    text_lower = text.lower()
    for pattern in role_patterns:
        matches = re.findall(pattern, text_lower)
        for match in matches:
            roles_counter[match] += 1

print("\nMost Common Roles / Job Titles:")
for role, count in roles_counter.most_common(15):
    print(f"{role}: {count}")

# Plot roles distribution
plt.figure(figsize=(12,6))
roles, counts = zip(*roles_counter.most_common(15))
plt.bar(roles, counts, color='salmon')
plt.xticks(rotation=45)
plt.title('Top 15 Roles / Job Titles')
plt.show()

# --- Step 6: Check for unusual/missing resumes ---
empty_resumes = [name for name, text in resumes.items() if len(text.strip()) == 0]
if empty_resumes:
    print("\nResumes with missing or empty text:")
    for name in empty_resumes:
        print(name)
else:
    print("\nNo empty resumes found. All data looks good.")