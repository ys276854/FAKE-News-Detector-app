import streamlit as st
import pandas as pd
import pickle
import re

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
stemmer = SnowballStemmer("english")
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)


# Load the dataset
df = pd.read_csv('news.csv')

# Load the vector and the model
vector_load = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('pac_model.pkl', 'rb'))

# Apply the stemmer to the text data
def stemming(content):
    con = re.sub('[^a-zA-Z]', ' ', content)
    con = con.lower()
    con = con.split()
    # Apply the Snowball stemmer and filter out the stopwords
    con = [stemmer.stem(word) for word in con if not word in stopwords.words('english')]
    stems = ' '.join(con)

    return stems

# Classify and predict using the model
def fake_news_detect(news):
    news = stemming(news)
    input_data = [news]
    vector_form1 = vector_load.transform(input_data)
    prediction = load_model.predict(vector_form1)

    return prediction

if __name__ == '__main__':
    st.title('Fake News Classification App')
    st.image('image.jpg')
    st.subheader("Select a News Title")

    sentence = ""
    # add a selection box to retrieve the titles and their content
    title = st.selectbox("Choose a news title", df['title'])
    
    if title:
        sentence = df[df['title'] == title]['text'].values[0]
        st.text_area("News content", sentence, height=200)
    
    predict_button = st.button("predict")

    if predict_button:
        prediction_class = fake_news_detect(sentence)
        print(prediction_class)

        if prediction_class == 'FAKE':
            st.warning('This is a Fake news')
        else:
            st.success('This is Real news')
