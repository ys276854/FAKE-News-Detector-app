import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download('stopwords')

stemmer = SnowballStemmer("english")

# Load trained model and vector
vector_load = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('pac_model.pkl', 'rb'))

def stemming(content):
    content = re.sub('[^a-zA-Z]', ' ', content)
    content = content.lower()
    content = content.split()
    content = [stemmer.stem(word) for word in content if word not in stopwords.words('english')]
    return ' '.join(content)

def fake_news_detect(news):
    news = stemming(news)
    vector_form = vector_load.transform([news])
    prediction = load_model.predict(vector_form)
    return prediction

st.title("📰 AI Fake News Detector")
st.write("Enter news text below to check whether it is Real or Fake.")

sentence = st.text_area("Enter News Text Here")

if st.button("Predict"):
    if sentence.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction_class = fake_news_detect(sentence)

        if prediction_class[0] == 'FAKE':
            st.error("⚠️ This is Fake News")
        else:
            st.success("✅ This is Real News")
