import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import joblib

# Load your dataset
# Ensure your dataset has two columns: "URL" and "Type"
data = pd.read_csv("url_dataset.csv")  # Replace with the path to your dataset

# Feature extraction using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['URL'])  # Transform URLs into feature vectors
y = data['Type']  # Target labels

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model and vectorizer using joblib
joblib.dump(model, "url_classifier_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and vectorizer saved!")
