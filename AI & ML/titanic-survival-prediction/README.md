# Titanic Survival Prediction (Supervised ML)

Predicting passenger survival on the Titanic using supervised machine learning with scikit-learn.

## Project Overview
This project applies a complete supervised ML workflow to the Kaggle Titanic dataset:
- Exploratory Data Analysis (EDA)
- Missing value handling (imputation)
- Feature engineering (Title, FamilySize, IsAlone, Deck)
- Preprocessing pipeline (ColumnTransformer + OneHotEncoder)
- Baseline model (Logistic Regression)
- Final model (Random Forest)
- Evaluation (accuracy, confusion matrix, classification report)
- Cross-validation (5-fold)

## Dataset
Source: Kaggle Titanic Competition  
Files used: `train.csv` (and optional `test.csv`)

> If the dataset is not included in this repo, download it from Kaggle and place it in `data/`.

## Key Feature Engineering
- **Title** extracted from `Name` (captures demographic/social grouping)
- **FamilySize** = `SibSp + Parch + 1`
- **IsAlone** indicates if the passenger travelled alone
- **Deck** extracted from `Cabin` (missing treated as `Unknown`)

## Results (Holdout Test Set)
- **Accuracy:** ~0.816  
- Confusion matrix and classification report are included in the notebook.

## Notebook
See: `notebooks/Titanic_Supervised_ML_Week2.ipynb`

## How to Run
1. Clone the repo
2. Create a virtual environment (recommended)
3. Install requirements:
   ```bash
   pip install -r requirements.txt


