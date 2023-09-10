import pickle

from joblib import load
from sklearn.preprocessing import OneHotEncoder

path = '/Users/shina-alukoa/Documents/GitHub/Personal Projects/car-price-predictions/backend/ml_model/'
# Load the machine learning model
regrModel = load(path + 'model.joblib')
cars_csv = path + 'used_cars_data.csv'

# Create an encoder
encoder = OneHotEncoder(handle_unknown='ignore')

# Load the trained model using pickle
liner_regression_model = path + 'linear_regression_model.pkl'
with open(liner_regression_model, "rb") as model_file:
    newModel = pickle.load(model_file)

