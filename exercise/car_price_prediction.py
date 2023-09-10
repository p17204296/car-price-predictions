import pandas as pd
import datetime
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from joblib import dump

# Load the dataset
df = pd.read_csv("used_cars_data.csv")

# One-hot encode categorical features
enc = OneHotEncoder(handle_unknown='ignore')
X = df[['brand', 'fuel', 'gearbox']]
enc.fit(X)
X_features = pd.DataFrame(enc.transform(X).toarray())

# Feature engineering
year = datetime.datetime.now().year
df['age'] = year - df['year']
X_num = df[['age', 'mileage (kms)']]
y = df['price (eur)']

# Combine numerical and one-hot encoded features
X = pd.concat([X_num, X_features], axis=1)

# Rename the columns for one-hot encoded features
feature_names = enc.get_feature_names_out(input_features=['brand', 'fuel', 'gearbox'])
X.columns = ['age', 'mileage (kms)'] + list(feature_names)

# Initialize and train the random forest regressor model
regr = RandomForestRegressor()
regr.fit(X, y)

# Save the trained model to a file
dump(regr, '../backend/ml_model/car_price_prediction_model.joblib')
