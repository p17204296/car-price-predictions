import pandas as pd
from fastapi import APIRouter, HTTPException

from backend.ml_model.load_model import cars_csv
from backend.ml_model.load_model import regrModel
from backend.ml_model.load_model import newModel

from backend.ml_model.load_model import encoder

from backend.models.car_model import Car


router = APIRouter()

feature_names = None

@router.on_event("startup")
def startup_event():
    global feature_names  # Use a global variable to store feature names

    training_data = pd.read_csv(cars_csv)
    categorical_columns = ['brand', 'fuel', 'gearbox']
    encoder.fit(training_data[categorical_columns])

    # Construct feature names for one-hot encoded columns
    feature_names = list(encoder.get_feature_names_out(input_features=categorical_columns))


@router.post("/predict_price/")
async def predict_car_price(car_data: Car):
    try:
        # Data Validation
        if not is_valid_input(car_data):
            raise HTTPException(status_code=400, detail="Invalid input data")

        # Preprocessing
        processed_features = preprocess_data(car_data)

        # Print out the shape and content of processed_features
        print("Processed Features Shape:", processed_features.shape)
        print("Processed Features Content:", processed_features)

        # Make Prediction
        predicted_price = newModel.predict([processed_features])[0]

        return {"predicted_price": predicted_price}

    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error: {e}")
        # Handle any errors and return appropriate HTTP responses
        raise HTTPException(status_code=500, detail="Internal Server Error")


def is_valid_input(car_data: Car):
    # Check if the brand is a non-empty string
    if not car_data.brand or not isinstance(car_data.brand, str):
        return False

    # Check if the year is a positive integer
    if car_data.year is not None and (not isinstance(car_data.year, int) or car_data.year <= 0):
        return False

    # Check if fuel and gearbox are non-empty strings
    if (not car_data.fuel or not isinstance(car_data.fuel, str)) or \
            (not car_data.gearbox or not isinstance(car_data.gearbox, str)):
        return False

    # Check if mileage is a non-negative integer
    if car_data.mileage is not None and (not isinstance(car_data.mileage, int) or car_data.mileage < 0):
        return False

    # If all checks pass, return True
    return True


def preprocess_data(car_data: Car):

    # Load the dataset
    df = pd.read_csv(cars_csv)

    X = df[['brand', 'fuel', 'gearbox']]

    # Lowercase the 'brand' feature
    brand = car_data.brand.lower()

    # Create a DataFrame with the same structure as 'X_features' from model training
    input_data = pd.DataFrame({
        'brand': [brand],
        'fuel': [car_data.fuel],
        'gearbox': [car_data.gearbox]
    })

    # Perform one-hot encoding using the fitted encoder
    input_encoded = encoder.transform(input_data).toarray()

    # Create a DataFrame with the same structure as 'X' from model training
    input_features = pd.DataFrame(input_encoded, columns=X.columns)

    # Add numerical features
    input_features['year'] = car_data.year
    input_features['mileage (kms)'] = car_data.mileage

    # Convert feature names to strings
    input_features.columns = input_features.columns.astype(str)

    return input_features


@router.post("/predict/")
async def predict_car_price(car_info: Car):

    try:
        # data for prediction
        input_data = [[
            car_info.year,
            car_info.mileage
        ]]

        # Make Prediction
        predicted_price = newModel.predict(input_data)[0]

        print(predicted_price)

        return {"predicted_price_eur": predicted_price}
    except Exception as e:
        print(f"Error: {e}")
        return HTTPException(status_code=500, detail="Internal server error")

