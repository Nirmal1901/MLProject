from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")

app = FastAPI()

model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    """Preprocess the input text for prediction."""
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input_data: TextInput):
    """Predict sentiment from input text."""
    
    processed_text = preprocess_text(input_data.text)
    
    vectorized_text = tfidf.transform([processed_text])
    
    prediction = model.predict(vectorized_text)
    
    
    sentiment = "positive" if prediction[0] == 4 else "negative" if prediction[0] == 0 else "neutral"
    return {"text": input_data.text, "sentiment": sentiment}
