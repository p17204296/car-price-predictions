import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from backend.ml_model.load_model import cars_csv

import pickle


def train_model(csv_file_path):
    # Load the dataset
    data = pd.read_csv(csv_file_path)

    # Split data into features and target
    X = data[['year', 'mileage (kms)']]
    y = data['price (eur)']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # Save the trained model to a file using pickle
    with open('linear_regression_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)


if __name__ == "__main__":
    train_model(cars_csv)
