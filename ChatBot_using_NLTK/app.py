from flask import Flask, jsonify, request, render_template
import json
import random
import pickle
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import load_model

# download NLTK data files
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

# intialize the flask app
app = Flask(__name__)

# load the data and model
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

chat_model = load_model('chat_model.h5')

# function for cleaning up the sentences
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # lemmatize each word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    
    return sentence_words

# function for converting sentence into bag of words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    
    bag = [0] * len(words)
    # create the bag of words array
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                
    return np.array(bag)

# function for predicting the class of the sentence
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = chat_model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    # filter out predictions below a threshold  
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    
    return_list = []
    # create a list of intents and their probabilities
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
        
    return return_list

# function for getting a response from the model
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    
    # search for the tag in the intents JSON
    for i in list_of_intents:
        if i['tag'] == tag:
            # choose a random response from the list of responses
            result = random.choice(i['responses'])
            break
            
    return result

# route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# route for getting the chatbot response
@app.route('/chat_response', methods=['POST'])
def chat_response():
    # get the message from the request
    message = request.json.get('message')
    
    # predict the class of the message and get the response
    ints = predict_class(message)
    
    # get the response
    res = get_response(ints, intents)
    
    return jsonify({'response': res})

# run the app
if __name__ == '__main__':
    app.run(debug=True)