from flask import Flask, request, jsonify
import joblib

# Load the trained model and vectorizer
model = joblib.load("url_classifier_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify_url():
    data = request.get_json()
    url = data.get("url")

    # Transform the URL into feature vectors
    features = vectorizer.transform([url])

    # Predict the type
    prediction = model.predict(features)[0]

    return jsonify({"type": prediction})

if __name__ == "__main__":
    app.run(debug=True)
