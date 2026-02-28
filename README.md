# 📰 Fake News Detector: An NLP-Powered Web App

This **Streamlit** web application uses a **pre-trained machine learning model** and **Natural Language Processing (NLP)** techniques to classify news articles as either **Real** or **Fake**. Combat misinformation with a simple, interactive tool! 

## ✨ Features

* **Input Selection:** Easily select a news title from a dropdown menu to load its content.
* **Text Analysis:** The selected news content is instantly preprocessed and vectorized using robust **NLP methods**.
* **Prediction:** A trained classifier provides a quick, data-driven prediction on the news authenticity.
* **Intuitive UI:** Built with **Streamlit**, the application offers a clean, user-friendly interface for immediate interaction and results.

---

## 🚀 Get Started

Follow these simple steps to get the application running on your local machine.

### Prerequisites

Ensure you have **Python 3.x** installed.

### 💻 Installation and Setup

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/kyouexe/Fake-News-Detection-App.git
    cd Fake-News-Detection-App
    ```

2.  **Install Dependencies:**

    Install all required Python libraries using the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App:**

    Start the Streamlit web application:

    ```bash
    streamlit run app.py
    ```

    Your web browser will automatically open the app. If not, navigate to `http://localhost:8501`.

### 🌐 Live Demo

You can also try the application instantly via the public Streamlit sharing link:

[Open the Live App](https://fake-news-detection-app-kyouexe.streamlit.app/)

---

## 💡 Usage

1.  **Select** a news title from the dropdown menu.
2.  **Review** the news content displayed in the text area.
3.  Click the **"Predict"** button to classify the article as **Fake** or **Real**.

---

## 🛠️ Technologies & Components

### **Stack**
* **Python:** The core programming language.
* **Streamlit:** Used for building the interactive web interface.
* **Pandas:** Essential for data manipulation (reading the `news.csv` file).
* **Scikit-learn (sklearn):** Provides the machine learning framework and the pre-trained model.
* **NLTK (Natural Language Toolkit):** Utilized for text preprocessing and NLP tasks.

### **Dataset and Model**
* **Dataset:** `news.csv` - Contains sample news titles and content used for demonstration and model training.
* **Model:** `pac_model.pkl` - A pre-trained machine learning model (likely a Passive Aggressive Classifier) persisted via Python's `pickle` library, used for the final classification prediction.

---
