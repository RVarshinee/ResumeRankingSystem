#Selecting top five resumes
from operator import itemgetter

@job_post.route("/view_applied_candidates", methods=["POST", "GET"])
def view_applied_candidates():
    job_id = request.form['job_id']
    result_data = None
    result_data = Applied_EMP.find({"job_id": ObjectId(job_id)}, {"User_name": 1, "Matching_percentage": 1, "user_id": 1}).sort([("Matching_percentage", -1)])

    if result_data is None:
        return {"StatusCode": 400, "Message": "Problem in Fetching"}
    else:
        candidates = []

        for candidate in result_data:
            user_id = candidate['user_id']
            user_name = candidate['User_name']
            matching_percentage = candidate['Matching_percentage']

            # Calculate the matching percentage and store it in the `matching_percentage` variable
            matching_percentage=Matching()
            
            candidates.append({
                "Name": user_name,
                "Match": matching_percentage,
                "user_id": user_id
            })

        # Sort the candidates by matching percentage in descending order
        sorted_candidates = sorted(candidates, key=itemgetter("Match"), reverse=True)

        # Display the top five candidates
        top_five_candidates = sorted_candidates[:5]

        response = {
            "candidates": top_five_candidates,
            "total_candidates": len(sorted_candidates)
        }

        return response



#Alternative way to select top five resumes

import os
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk #For data cleaning (preprocessing)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Directory where resume PDFs are stored
resumes_directory = "C:/Users/RAMKUMAR/Desktop/Kaggle/Resumes"

# List of all PDF files in the directory
resume_files = [os.path.join(resumes_directory, filename) for filename in os.listdir(resumes_directory) if filename.endswith(".pdf")]

# Extract text from all PDF resumes
def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(pdf_file)
    for page in doc:
        text += page.get_text()
    return text

resumes_text = [extract_text_from_pdf(resume_file) for resume_file in resume_files]

# Preprocess text data (e.g., remove punctuation, lowercasing)
# Lowercasing
resumes_text = resumes_text.lower()

# Tokenization
tokens = word_tokenize(resumes_text)

# Removing Punctuation
# Translation table to remove punctuation
translator = str.maketrans('', '', string.punctuation)
tokens = [word.translate(translator) for word in tokens]

# Reconstructing the cleaned text
resumes_text = ' '.join(tokens)

# Compute TF-IDF vectors for resumes and job description
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix_resumes = tfidf_vectorizer.fit_transform(resumes_text)
tfidf_matrix_job_description = tfidf_vectorizer.transform([job_description_text])

# Calculate cosine similarity between job description and resumes
cosine_similarities = cosine_similarity(tfidf_matrix_job_description, tfidf_matrix_resumes)

# Sorting resumes by cosine similarity scores in descending order
sorted_indices = cosine_similarities.argsort()[0][::-1]

# Selecting the top 5 resumes with the highest cosine similarity scores
num_top_resumes = 5 
top_resumes = [resume_files[i] for i in sorted_indices[:num_top_resumes]]

# Displaying the top 5 resumes
for i, resume in enumerate(top_resumes):
    print(f"Top Resume {i + 1}: {resume}")








