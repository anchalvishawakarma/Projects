# Heart Disease Prediction Model  

This project builds a machine learning pipeline to predict heart disease based on clinical parameters. It involves data preprocessing, exploratory data analysis (EDA), model building, evaluation, and hyperparameter tuning using various machine learning algorithms.  

---

## Table of Contents  
1. [Project Overview](#project-overview)  
2. [Dataset Information](#dataset-information)  
3. [Key Features](#key-features)  
4. [Technologies Used](#technologies-used)  
5. [Installation](#installation)  
6. [Getting Started](#getting-started)  
7. [Results](#results)  
9. [The repository](#The-repository)

---

## Project Overview  

Heart disease remains one of the leading causes of mortality worldwide. Early diagnosis and prediction of heart disease can save lives. This project uses the **Heart Disease dataset** to train and evaluate various machine learning models for predicting the presence of heart disease.  

---

## Dataset Information  

The dataset is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php). It contains 303 records with 14 features, including:  
- **Demographics:** Age, Gender  
- **Clinical Parameters:** Chest Pain Type (cp), Resting Blood Pressure (trestbps), Cholesterol (chol)  
- **Functional Tests:** Maximum Heart Rate Achieved (thalach), ST Depression (oldpeak)  
- **Target Variable:** `0` (No Heart Disease) and `1` (Heart Disease)  

---

## Key Features  

1. **Data Preprocessing**  
   - Cleaning and handling missing values.  
   - Exploratory Data Analysis (EDA) to extract insights and visualize patterns.  

2. **Machine Learning Models**  
   - Logistic Regression  
   - Random Forest Classifier  
   - K-Nearest Neighbors (KNN)  

3. **Hyperparameter Tuning**  
   - Manual tuning and RandomizedSearchCV for optimization.  

4. **Model Evaluation**  
   - Metrics: Accuracy, Precision, Recall, F1-Score, and Cross-Validation.  

5. **Data Visualization**  
   - Heatmaps, scatter plots, and bar plots for pattern recognition and result interpretation.  

---

## Technologies Used  

- **Programming Language:** Python  
- **Libraries:**  
  - Data Manipulation: Pandas, NumPy  
  - Visualization: Matplotlib, Seaborn  
  - Machine Learning: Scikit-learn  
- **Tools:** Jupyter Notebook, Git  

---

## Installation  

### Prerequisites  
- Python 3.7 or higher  
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  

### Steps  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
2. Install the required libraries:

    pip install -r requirements.txt

## Getting Started

### Results
Best Model: Random Forest Classifier
Accuracy: 89%
Precision: 87%
Recall: 85%

## The repository
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m "Add feature-name").
Push to the branch (git push origin feature-name).
Open a Pull Request.

