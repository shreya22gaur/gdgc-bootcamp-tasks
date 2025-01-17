# Titanic Survival Prediction Project

## Overview
This project focuses on predicting whether a passenger on the Titanic would survive or not based on various features like age, gender, passenger class, and more. The dataset and problem are sourced from the popular Kaggle Titanic competition.

## Dataset
The dataset contains the following key features:
- **PassengerId**: Unique identifier for each passenger.
- **Survived**: Target variable (0 = No, 1 = Yes).
- **Pclass**: Passenger class (1 = First, 2 = Second, 3 = Third).
- **Name**: Passenger's name.
- **Sex**: Gender of the passenger.
- **Age**: Age of the passenger.
- **SibSp**: Number of siblings or spouses aboard.
- **Parch**: Number of parents or children aboard.
- **Ticket**: Ticket number.
- **Fare**: Amount paid for the ticket.
- **Cabin**: Cabin number.
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

## Steps Performed

### 1. Data Preprocessing
- **Handled Missing Values**:
  - `Age` was filled with the median.
  - `Embarked` was filled with the mode.
  - `Fare` in the test dataset was filled with the median.
- **Feature Encoding**:
  - Converted `Sex` to numerical values (0 for male, 1 for female).
  - Converted `Embarked` to numerical values (C = 0, Q = 1, S = 2).

### 2. Feature Selection
Selected the following features for training:
- `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`.

### 3. Model Training
- **Algorithm Used**: Random Forest Classifier
- **Training and Validation**:
  - Split the data into training (80%) and validation (20%) sets.
  - Achieved a validation accuracy of **82%**.

### 4. Predictions
- Made predictions on the test dataset.
- Saved the results to a CSV file (`submission.csv`).

## Files in Repository
- **titanic.ipynb**: Jupyter Notebook containing the code for the entire process.
- **submission.csv**: Output file with predictions for the test dataset.
- **README.md**: Documentation for the project.

## How to Run
1. Clone the repository.
2. Open the `titanic.ipynb` file in Jupyter Notebook.
3. Run all cells sequentially.
4. Ensure the Titanic dataset is available in the specified path (`/kaggle/input/titanic`).

## Results
- **Best Algorithm**: Random Forest Classifier
- **Validation Accuracy**: 82%

## Future Improvements
- Try other classification algorithms like Logistic Regression, SVM, or K-Nearest Neighbors.
- Perform hyperparameter tuning for the Random Forest model.
- Explore additional feature engineering techniques.

