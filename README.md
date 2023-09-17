**Project Overview**

1. This project deals with extracting data from resume and categorizing it as skills, degree, university, etc. Models are built and trained to extract data from resumes and job descriptions. It is useful to determine the matching percentage of the resume content with respect to the job descriptions posted by companies.
   
2. This project includes an interactive interface using which the companies can post various jobs along with the appropriate job descriptions.
 
3. Through the interface the candidates can also login to their accounts and view the jobs posted by the companies.
 
4. The interface enables the candidates to apply for the jobs posted by the companies.
 
5. The company can view the number of applicants along with their name and email
  
6. The company HR can view the details of the applicants.
  
7. The company can view matching percentages of the applied candidates' resume corresponding to the job description posted by the company.

8. The details of the candidates including the resume of the candidates and the job description posted by the company are stored in the database for effective and efficient retrieval of data.

**Approach**

Involves the following steps:

1. Data Preparation: The process begins with a dataset containing resumes and associated annotations. This dataset is split into training and testing subsets, with 70% of the data allocated for training and 30% for testing.

2. Text Data Preprocessing: Each resume text is preprocessed to clean and prepare it for training. Preprocessing includes removing punctuation, and lowercasing the text to ensure consistency.

3. Training Data Conversion to spaCy Format: The training data, consisting of resumes, is converted into the spaCy format. This involves initializing a spaCy pipeline using the blank("en") model, creating a DocBin object to hold processed documents, and constructing spaCy Doc objects with entity annotations. These processed documents are added to the DocBin.

4. Saving the Training Data: The processed training data in spaCy format is saved as a binary file using the to_disk method of the DocBin object. This binary file is stored at a specified location.

5. Model Configuration: A pre-defined spaCy configuration file (config.cfg) is used to specify the model's architecture, hyperparameters, and other settings.

6. Training the Model: The spaCy model training process is initiated using the !python -m spacy train command. This command specifies the path to the configuration file (config.cfg), the paths to the training and development data in spaCy format. The trained model is saved to a specified output directory.

7. Model Training and Evaluation: During training, the model learns to recognize entities and patterns in the resume text. The model's performance is evaluated using the development data to ensure effective learning.

8. Trained Model Saving: After successful training and evaluation, the trained spaCy model is saved to the specified output directory.

9. A web interface is created using flask which enables the candidates to apply to the job posted by the companies.

10. The candidate details, resume uploaded, job description posted by the companies are stored in database.

11. MongoDB is utilized for effectively storing data in database.

12. The matching percentages of the applied candidates' resume corresponding to the job description posted by the company can be acheived using cosine-similarity function as in ResumeRankingProcess.py


**Challenges faced and its solutions**

1. Entity Identification:

Challenge: Identifying relevant entities (e.g., skills, experiences) in resumes accurately was challenging.
Solution: I used Entity Recognition (NER) model using annotated data to extract entities.

2. Model Training

Challenge: Training NER model was taking huge amount of time. The model training was too much slow.
Solution: I utilized cloud-based service offered by Google Colab. It enabled me use T4 GPU service which is hardware accelerator to speed up model training. It significantly reduced the model training time.

**Determining the top 5 candidates for each job description based on similarity scores:**

Matching candidates to job descriptions is a multi-step process that involves two key datasets: job descriptions outlining required skills and qualifications, and candidate resumes detailing their professional background. To ensure accurate assessments, both texts undergo preprocessing. This includes tasks such as removing punctuation and standardizing to lowercase. Feature extraction is then used to identify specific attributes, like keywords, skills, and experience. Text data is transformed into numerical vectors using techniques like TF-IDF or word embeddings. Similarity scores are computed with metrics like cosine similarity, which ranks candidates based on their alignment with the job description. The top 5 candidates with the highest scores are given priority for further evaluation in the recruitment process, which may include interviews and skills assessments.

**Insights from the matching process**

The process of matching job descriptions with candidate resumes provides valuable insights for recruitment. It helps recruiters to evaluate the relevance of candidates' skills and qualifications to specific job requirements, streamlining the initial screening process and enabling them to prioritize the most suitable candidates. This approach offers an efficient method for candidate evaluation, saving time and ensuring quality matches. It empowers recruiters to make data-driven decisions while efficiently handling large volumes of resumes and job descriptions. Ultimately, the matching process improves the recruitment workflow by swiftly identifying top candidates, setting the stage for further assessments, and informed hiring choices.

