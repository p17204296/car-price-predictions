# car-price-prediction-app

FastAPI, React

This web application allows users to predict the price of a car based on various input parameters.

## Features

- Enter car details such as brand, year, fuel type, gearbox, and mileage.
- Click the "Predict Price" button to get a price prediction.
- View the predicted price on the screen.

## Set up Back-End

- Install python and pip

- cd into backend directory: `cd .\backend\`

- **To Install python packages using the requirements.txt (see below)**
  -- Install txt file: `pip install -r requirements.txt`
  > This will download the packages using the requirements.txt file

**To Run Backend Server**
Enter in terminal `python .\main.py`

- Should be running on Port 8000 (http://localhost:8000)
  You can see the **API Documentation** at this url: http://localhost:8000/docs#/

**To Run Backend Test**

- cd into tests directory: `cd .\backend\tests`
  Enter in terminal `python test_load_model.py`

## Set up Front-End

- Install NodeJS
- cd out of backend and cd into frontend directory: `cd ..\frontend\`
  > **Note**: If you come across problems in powershell enter this command in terminal `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`
- To install the front end dependencies enter: `npm install`
- Then install yarn using npm `npm install yarn`

**Now you can run the front end server:**
Enter `yarn start` to start the client server

- Should be running on Port 3000 (http://localhost:3000)
