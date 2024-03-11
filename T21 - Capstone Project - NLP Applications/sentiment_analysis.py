import pandas as pd
import spacy
from spacytextblob import spacytextblob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

def preprocess(text):
    """Preprocess the text data by removing stopwords and performing basic text cleaning."""
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    clean_text = ' '.join(tokens)
    return clean_text

def predict_sentiment(review):
    """Predict the sentiment (positive, negative, neutral) of a product review."""

    clean_review = preprocess(review)
    doc = nlp(clean_review)
    polarity = doc._.polarity

    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

data = pd.read_csv('amazon_product_reviews.csv')

clean_data = data.dropna(subset=['reviews.text'])

review1 = clean_data['reviews.text'][0]
review2 = clean_data['reviews.text'][1]

sample_reviews = [
    "This product is amazing! I love it.",
    "I'm disappointed with the quality. It's not what I expected.",
    "It's okay, but nothing special."
]

for review in sample_reviews:
    sentiment = predict_sentiment(review)
    print(f"Review: '{review}'")
    print(f"Predicted sentiment: {sentiment}\n")

doc1 = nlp(review1)
doc2 = nlp(review2)
similarity_score = doc1.similarity(doc2)
print(f"Similarity score between review 1 and review 2: {similarity_score}")
