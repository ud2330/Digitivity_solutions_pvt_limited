from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

try:
    model = joblib.load('medical_model.pkl')
    scaler = joblib.load('scaler.pkl')
    print("Model assets loaded successfully.")
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
        region = request.form.get('region')

        nw, se, sw = 0, 0, 0
        if region == 'northwest': nw = 1
        elif region == 'southeast': se = 1
        elif region == 'southwest': sw = 1

        data = pd.DataFrame([[age, sex, bmi, children, smoker, nw, se, sw]], 
                            columns=['age', 'sex', 'bmi', 'children', 'smoker', 
                                     'region_northwest', 'region_southeast', 'region_southwest'])

        scaled_data = scaler.transform(data)
        prediction = model.predict(scaled_data)[0]
        
        formatted_result = f"${max(0, float(prediction)):,.2f}"
        
        return render_template('index.html', prediction_text=formatted_result)

    except Exception as e:
        print(f"Prediction Error: {e}")
        return render_template('index.html', prediction_text="Error in calculation")

if __name__ == "__main__":
    app.run(debug=True)
