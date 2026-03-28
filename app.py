from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load your model and scaler
try:
    model = joblib.load('medical_model.pkl')
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    print(f"Error loading assets: {e}")

@app.route('/')
def home():
    # Pass None initially so the second box doesn't exist on page load
    return render_template('index.html', prediction_text=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Capture Data
        age = float(request.form.get('age'))
        bmi = float(request.form.get('bmi'))
        children = int(request.form.get('children'))
        sex = int(request.form.get('gender'))
        smoker = int(request.form.get('smoker'))

        # 2. Create DataFrame matching training columns
        data = pd.DataFrame({
            'age': [age],
            'sex': [sex],
            'bmi': [bmi],
            'children': [children],
            'smoker': [smoker],
            'region_northwest': [0],
            'region_southeast': [0],
            'region_southwest': [0]
        })

        # 3. Scale and Predict
        scaled_data = scaler.transform(data)
        prediction = model.predict(scaled_data)[0]
        
        # Format the number as currency
        result = f"${round(float(prediction), 2):,}"
        
        return render_template('index.html', prediction_text=result)

    except Exception as e:
        print(f"Prediction error: {e}")
        return render_template('index.html', prediction_text="Error")

if __name__ == "__main__":
    app.run(debug=True)