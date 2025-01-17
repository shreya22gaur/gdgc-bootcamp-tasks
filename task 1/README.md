# Housing Price Prediction Project

## Overview
This project aims to predict housing prices using a dataset containing various attributes such as area, number of bedrooms, bathrooms, stories, parking, and more. The project utilizes machine learning techniques to preprocess the data, train a predictive model, and evaluate its performance.

## Dataset
The dataset used for this project is sourced from Kaggle: [Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset). It contains the following key features:

- **area**: The area of the property in square feet.
- **bedrooms**: Number of bedrooms.
- **bathrooms**: Number of bathrooms.
- **stories**: Number of stories.
- **parking**: Number of parking spaces.
- Various binary indicators for attributes like `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`, and furnishing status.
- **price**: The target variable representing the property price.

## Project Steps

### 1. Libraries and Dataset Loading
The following libraries are used:
- `pandas` for data manipulation.
- `scikit-learn` for machine learning operations.

The dataset is loaded into a pandas DataFrame and prepared for preprocessing.

### 2. Data Preprocessing
- The target variable (`price`) is separated from the features.
- Categorical variables are encoded using `pd.get_dummies`.
- The dataset is split into training and testing sets (80%-20%).

### 3. Model Training
A Random Forest Regressor is used to train the model on the training dataset. The model is configured with default parameters and a random seed of 42 for reproducibility.

### 4. Model Evaluation
The model's performance is evaluated using:
- **R-squared Score**: To measure how well the model explains the variance in the target variable.
- **Mean Absolute Error (MAE)**: To measure the average magnitude of prediction errors.

#### Results:
- Training Score: **0.95**
- Testing Score: **0.61**
- Mean Absolute Error: **1,021,546.04**

## File Structure
- **housing problem.ipynb**: The main Jupyter Notebook containing the implementation.
- **README.md**: This file describing the project.

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.7 or above
- Jupyter Notebook
- Required Python libraries: `pandas`, `scikit-learn`

## How to Run
1. Clone the repository.
2. Open the `housing problem.ipynb` file in Jupyter Notebook.
3. Run all the cells sequentially.

## Future Improvements
- Perform hyperparameter tuning for the Random Forest model to improve performance.
- Explore additional machine learning models.
- Incorporate more advanced feature engineering techniques.

## License
This project is open-source 

---

For any questions or contributions, feel free to create an issue or submit a pull request.

