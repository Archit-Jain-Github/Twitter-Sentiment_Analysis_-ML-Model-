from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('trained_model.sav', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    tweet = data['tweet']

    # Preprocess the tweet as per your trained model (like tokenization/vectorization)
    # Example: tweet_vector = vectorizer.transform([tweet])

    prediction = model.predict(tweet_vector)

    # Return the prediction result
    result = 'Positive Tweet' if prediction[0] == 1 else 'Negative Tweet'
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
