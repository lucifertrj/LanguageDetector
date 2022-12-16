import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

data = pd.read_csv("data/Language_Detection.csv")

target = open("classes.txt","r").readlines()
for ind in range(len(target)):
    target[ind] = target[ind].strip('\n')

def predictions(text):
    model = pickle.load(open("model/LangDetect.pkl",'rb'))
    text = [text]
    tfidf = TfidfVectorizer()
    X_new = tfidf.fit(data['Text'])
    new_text = tfidf.transform(text).toarray()
    pred = model.predict(new_text)
    return target[pred[0]]