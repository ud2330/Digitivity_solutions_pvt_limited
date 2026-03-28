from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

try:
    model = joblib.load('medical_model.pkl')
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    print(f"Error loading assets: {e}")

@app.route('/')
def home():
    return render_template('index.html', prediction_text=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form.get('age'))
        bmi = float(request.form.get('bmi'))
        children = int(request.form.get('children'))
        sex = int(request.form.get('gender'))
        smoker = int(request.form.get('smoker'))

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

        scaled_data = scaler.transform(data)
        prediction = model.predict(scaled_data)[0]
        
        formatted_result = f"${round(float(prediction), 2):,}"
        return render_template('index.html', prediction_text=formatted_result)

    except Exception as e:
        return render_template('index.html', prediction_text="Error")

if __name__ == "__main__":
    app.run(debug=True)
