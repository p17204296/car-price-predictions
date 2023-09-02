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

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Initialize and train the random forest regressor model
regr = RandomForestRegressor()
regr.fit(X_train, y_train)

# Make predictions on the test set
y_pred = regr.predict(X_test)

# Model evaluation - Mean Squared Error
mse = mean_squared_error(y_test, y_pred, squared=False)
print(f"Root Mean Squared Error: {mse:.2f}")

# Model evaluation - Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.2f}")

# Save the trained model to a file
dump(regr, 'car_price_prediction_model.joblib')
