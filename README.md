# 🩺 Diabetes Prediction Web App
![image](https://github.com/user-attachments/assets/25796632-d1ce-450a-b680-17d5a6e57bfc)


A simple and accurate web app to predict whether a person is diabetic or not using Logistic Regression.  
Built using a Kaggle dataset, this project combines machine learning with a user-friendly Flask interface.

---

## 📌 Project Highlights

- ✅ Logistic Regression Model (with GridSearchCV for hyperparameter tuning)
- ✅ Data preprocessing using Scikit-learn Pipeline
- ✅ Evaluation with Confusion Matrix, ROC Curve, AUC, Accuracy, Classification Report
- ✅ Web app built with Flask, HTML, and CSS
- ✅ Real patient test input (diabetic & non-diabetic)
- ✅ Model saved using Pickle for deployment

---

## 🗂️ Folder Structure

Diabetes_Prediction/
├── notebook/ # Jupyter notebook for EDA, preprocessing, and training
│ └── model_building.ipynb
├── templates/ # HTML frontend
│ └── index.html
├── static/ # CSS styling
│ └── style.css
├── models/ # Saved ML model (.pkl)
│ └── model.pkl
├── app.py # Flask app


---

## 📊 Dataset Information

- **Source**: [Kaggle - Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Rows**: 768  
- **Features**:
  - Pregnancies
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age  
- **Target**: `Outcome` (0 = Non-Diabetic, 1 = Diabetic)

---

## ⚙️ How to Run Locally

### 🛠️ Step-by-step

1. **Clone the repository**
   ```bash
   git clone https://github.com/qosain-bukhari/Diabetes_Prediction.git
   cd Diabetes_Prediction
