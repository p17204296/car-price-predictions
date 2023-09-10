
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from joblib import load
import datetime

# Load the trained model
path = '/Users/shina-alukoa/Documents/GitHub/Personal Projects/car-price-predictions/backend/ml_model/'
regrModel = load(path + 'model.joblib')

# Initialize the encoder
encoder = OneHotEncoder(handle_unknown='ignore')

# Load the training data or use your training data path
training_data_path = path + 'used_cars_data.csv'  # Replace with the actual path
training_data = pd.read_csv(training_data_path)


# Specify categorical columns for one-hot encoding
categorical_columns = ['brand', 'fuel', 'gearbox']

# Fit the encoder with training data
encoder.fit(training_data[categorical_columns])

# Sample input data for prediction
sample_data = {
    'brand': 'Volkswagen',
    'fuel': 'Gasolina',
    'gearbox': 'Manual',
    'year': 2016,
    'mileage (kms)': 60000
}

# Calculate 'age' based on the current year
current_year = datetime.datetime.now().year
sample_data['age'] = current_year - sample_data['year']

# Convert input data to a DataFrame
input_data = pd.DataFrame([sample_data])

# Perform one-hot encoding using the fitted encoder
input_encoded = encoder.transform(input_data[categorical_columns]).toarray()

# Construct feature names for one-hot encoded columns
feature_names = list(encoder.get_feature_names_out(input_features=categorical_columns))

# Create a DataFrame with the correct feature names
input_features = pd.DataFrame(input_encoded, columns=feature_names)

# Add numerical features
input_features['age'] = input_data['age']
input_features['mileage (kms)'] = input_data['mileage (kms)']

# Make predictions
predictions = regrModel.predict(input_features)
print("Predicted Price:", predictions[0])

