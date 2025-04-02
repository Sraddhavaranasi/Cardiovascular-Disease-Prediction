from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

model = joblib.load("SVM_model_accuracy_0.729857.joblib")
app = Flask(__name__)

# Define home route
@app.route('/')
def home():
    return render_template('index.html') 

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Return response
        return jsonify({"prediction": int(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
