import React, { useState } from "react";
import "./App.css";
import CarForm from "./components/CarForm";
import PredictedPrice from "./components/PredictedPrice";

function App() {
  // State to store the predicted price as a string or undefined
  const [predictedPrice, setPredictedPrice] = useState<string | undefined>(
    undefined
  );

  // State to store any error messages as strings or null
  const [error, setError] = useState<string | null>(null);

  // Function to handle the form submission
  const handleSubmit = (price: string) => {
    // Set the predicted price in state and clear any previous error
    setPredictedPrice(price);
    setError(null);
  };

  // Function to handle errors
  const handleError = (errorMessage: string) => {
    // Set the error message in state and reset the predicted price to undefined
    setError(errorMessage);
    setPredictedPrice(undefined);
  };

  return (
    <div className="App">
      <h1>Car Price Prediction</h1>
      {/* Render the CarForm component, passing in the handleSubmit and handleError functions */}
      <CarForm onSubmit={handleSubmit} onError={handleError} />

      {/* Render the PredictedPrice component, passing in the predictedPrice */}
      <PredictedPrice predictedPrice={predictedPrice} />

      {/* Display an error message if there is one */}
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default App;
