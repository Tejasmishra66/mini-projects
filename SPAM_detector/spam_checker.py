import joblib
import re
from nltk.corpus import stopwords
import nltk

# Download NLTK data (first-time only)
nltk.download('stopwords')

# Load models (they must be in the same folder!)
tfidf = joblib.load('tfidf_vectorizer.joblib')
model = joblib.load('spam_model.joblib')

def clean_text(text):
    """Preprocess text exactly like during training"""
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special chars
    text = text.lower()                       # Lowercase
    text = ' '.join([word for word in text.split() 
                    if word not in stopwords.words('english')])
    return text

def predict_spam(text):
    """Classify a message"""
    cleaned = clean_text(text)
    vec = tfidf.transform([cleaned])
    return "SPAM 🚨" if model.predict(vec)[0] == 1 else "HAM 📨"

# ===== TEST IT =====
if __name__ == "__main__":
    while True:
        user_input = input("\nEnter a message (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        print("Prediction:", predict_spam(user_input))
