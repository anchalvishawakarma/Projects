# Concrete Compressive Strength Prediction

## Project Description
This project aims to predict the compressive strength of concrete mixtures using machine learning models. The dataset consists of various features related to the composition of concrete, and the target variable is the compressive strength. The analysis includes data preprocessing, exploratory data analysis, feature scaling, model training, hyperparameter tuning, and evaluation of multiple regression models.

## Files in Repository
- **`concrete_compressive_strength.csv`**: Dataset containing concrete composition and compressive strength values.
- **`main.py`**: Python script containing all the code for data preprocessing, model training, and evaluation.
- **`README.md`**: Documentation about the project.
- **`requirements.txt`**: List of dependencies required to run the project.

## Project Workflow
1. **Data Import and Exploration:**
   - Load the dataset and understand its structure.
   - Perform basic descriptive statistics and visualize data distributions.

2. **Data Preprocessing:**
   - Split the data into features (X) and target variable (Y).
   - Split the dataset into training and test sets.
   - Scale the features using `MinMaxScaler`.

3. **Model Training:**
   - Train models like Random Forest Regressor, AdaBoost Regressor, and Gradient Boosting Regressor.
   - Evaluate models using R² score, mean squared error (MSE), and mean absolute error (MAE).

4. **Hyperparameter Tuning:**
   - Use GridSearchCV to tune the hyperparameters of the Random Forest Regressor.

5. **Model Evaluation and Comparison:**
   - Compare the performance of all models using metrics and visualizations.

6. **Visualizations:**
   - Plot distributions, feature outliers, model scores, and predictions vs. actual values.

## How to Run the Project
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd concrete-compressive-strength
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python main.py
   ```

## Requirements
Below are the dependencies needed for the project:

```plaintext
numpy
pandas
matplotlib
seaborn
scikit-learn
```

Install these packages using:
```bash
pip install -r requirements.txt
```

## Results
- Random Forest Regressor achieved an R² score of **0.90** on the test set.
- AdaBoost Regressor and Gradient Boosting Regressor also performed well but had slightly lower scores.

## Visualizations
- Feature distributions and outliers are visualized using seaborn.
- Bar charts and scatter plots illustrate model performance and predictions.

---
