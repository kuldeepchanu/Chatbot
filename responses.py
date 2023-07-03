import pickle
import random
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
import json

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    if isinstance(text, float):
        text = str(text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
    return ' '.join(tokens).lower()

df = pd.read_csv('New\databooks.csv')
df['processed_user_text'] = df['User'].apply(preprocess)
X = df['processed_user_text']
y = df['Assistant']
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(X).toarray()

file_path = 'New\model.pkl'
with open(file_path, 'rb') as file:
    model = pickle.load(file)

with open('New\intents.json') as file:
    intents = json.load(file)

specific_responses = intents['specific_responses']
greet_inputs = intents['greet_inputs']
greet_responses = intents['greet_responses']
thanks_inputs = intents['thanks_inputs']
thanks_responses = intents['thanks_responses']
help_inputs = intents['help_inputs']
help_responses = intents['help_responses']
help_list = intents['help_list']
joke_inputs = intents['joke_inputs']
jokes_list = intents['jokes_list']
day_inputs = intents['day_inputs']
no_inputs = intents['no_inputs']
exit_inputs = intents['exit_inputs']
exit_responses = intents['exit_responses']
about_inputs = ["about", "about company", "about your company"]
cyber_inputs = ["security", "cybersecurity"]
intern_inputs = ["internship", "internships"]

def response(text):
    processed_text = preprocess(text)
    
    if processed_text in about_inputs:
        response = "AI Hawks, one of the top consulting companies for information technology, offers specialised IT consulting and corporate IT assistance to companies of all kinds. By partnering with AI Hawks, we can assist you in creating highly effective IT strategies and implementing cutting-edge solutions. You can connect with us on the below mentioned links."
        return {"status": 200, "response": response}

    elif any(keyword in processed_text for keyword in intern_inputs):
        response = "As a startup we do encourage interships. For more info visit our website or contact us through the specified links."
        return {"status": 200, "response": response}
    
    elif any(keyword in processed_text for keyword in cyber_inputs):
        response = "AI Hawks specializes in providing comprehensive cybersecurity services to protect systems, networks, and data from cyberattacks. Their Cybersecurity as a Service package includes tactical cyber defense, vulnerability management, and incident response. Partnering with AI Hawks ensures businesses have a skilled team and robust strategies to mitigate risks and safeguard against unauthorized access."
        return {"status": 200, "response": response}
    
    elif processed_text in exit_inputs:
        response = random.choice(exit_responses)
        return {"status": 200, "response": f"{response}"}

    elif any(keyword in processed_text for keyword in greet_inputs):
        response = random.choice(greet_responses)
        return {"status": 200, "response": f"{response}"}

    elif any(keyword in processed_text for keyword in thanks_inputs):
        response = random.choice(thanks_responses)
        return {"status": 200, "response": f"{response} Do you have more queries?"}

    elif processed_text in no_inputs:
        return {"status": 200, "response": f"{random.choice(exit_responses)}"}

    elif any(keyword in processed_text for keyword in help_inputs):
        user_input_vector = tfidf_vectorizer.transform([processed_text]).toarray()
        cosine_similarities = cosine_similarity(user_input_vector, tfidf_matrix).flatten()
        index = cosine_similarities.argsort()[-2]

        if cosine_similarities[index] == 0:
            response = random.choice(specific_responses)
            return {"status": 200, "response": f"{response}"}

        predicted_label = model.predict([processed_text])
        if len(predicted_label) >= 1:
            return {"status": 200, "response": f'{random.choice(help_list)} {predicted_label[0]}'}
        else:
            return {"status": 200, "response": f"{random.choice(help_responses)}"}

    elif any(keyword in processed_text for keyword in joke_inputs):
        return {"status": 200, "response": f'{random.choice(help_list)} {random.choice(jokes_list)}'}

    elif any(keyword in processed_text for keyword in day_inputs):
        current_time = datetime.now().time()
        if current_time < datetime.strptime('12:00', '%H:%M').time():
            response = "Good Morning!"
        elif current_time < datetime.strptime('16:00', '%H:%M').time():
            response = "Good Afternoon!"
        elif current_time < datetime.strptime('21:00', '%H:%M').time():
            response = "Good Evening!"
        else:
            response = "Good Night!"
        return {"status": 200, "response": f'{response}'}

    else:
        user_input_vector = tfidf_vectorizer.transform([processed_text]).toarray()
        cosine_similarities = cosine_similarity(user_input_vector, tfidf_matrix).flatten()
        index = cosine_similarities.argsort()[-2]

        if cosine_similarities[index] == 0:
            response = random.choice(specific_responses)
            return {"status": 200, "response": f"{response}"}

        predicted_label = model.predict([processed_text])
        return {"status": 200, "response": f'{predicted_label[0]}'}