import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import classification_report

nlp = spacy.load('en_core_web_sm')   #Load Spacy small language english model
df = pd.read_csv('New\databooks.csv')   #Reading the csv file.

def preprocess(text):     #This function is used to remove all the punctuation marks and stop words from the text.
    if isinstance(text, float):     #By chance if there is any text present in float format, we convert it into string format.
        text = str(text)
    doc = nlp(text)     #Text is being passed through the nlp pipeline. 
    tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]   #Performing lemmatization for the tokenised words from the doc, if they are not in stop words list or not punctuation marks.
    return ' '.join(tokens).lower()     #Returns the output in string format.

df['processed_user_text'] = df['User'].apply(preprocess)    #Processed text is stored in new column named 'processed_user_text'.
X = df['processed_user_text']
y = df['Assistant']

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(X).toarray() #Each row represents of a document and each column represents a feature.

#Creating a pipeline where the mentioned tasks are performed on the labeled dataset.
pipeline = Pipeline([
    ("TfIdf", TfidfVectorizer()),   #Text feature extraction.
    ("SVM", SVC())    #Support Vector Machine classifier.
])

parameters = {
    'TfIdf__ngram_range': [(1, 1), (1, 2)],  # Specifies the range of n-grams to consider during TF-IDF vectorization.
    'SVM__C': [0.1, 1, 10],  # Regularization parameter for the SVM classifier.
    'SVM__kernel': ['linear', 'rbf']  # Kernel function to be used in the SVM classifier.
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)  # Cross-validation strategy
grid_search = GridSearchCV(pipeline, parameters, cv=cv)  # Grid search for hyperparameter tuning
grid_search.fit(X, y)  # Fit the grid search on the data

import pickle
file_name = 'model.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(grid_search, file)