from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('models/model.pkl', 'rb'))

# Create Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values (same order as model input)
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        bp = float(request.form['bp'])
        bmi = float(request.form['bmi'])
        age = float(request.form['age'])

        # Convert input to 2D array
        data = np.array([[pregnancies, glucose, bp, bmi, age]])

        # Make prediction
        prediction = model.predict(data)[0]
        result = "Diabetic" if prediction == 1 else "Not Diabetic"

        return render_template('index.html', prediction_text=f'Result: {result}')
    
    except Exception as e:
        return f"Error: {e}"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
