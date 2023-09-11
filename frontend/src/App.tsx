// src/App.tsx
import React, { useState } from "react";
import "./App.css";
import CarForm from "./components/CarForm";
import PredictedPrice from "./components/PredictedPrice";

function App() {
  const [predictedPrice, setPredictedPrice] = useState<string | undefined>(
    undefined
  ); // Change to string
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = (price: string) => {
    // Change the type of price to string
    setPredictedPrice(price);
    setError(null);
  };

  const handleError = (errorMessage: string) => {
    setError(errorMessage);
    setPredictedPrice(undefined); // Change to undefined
  };

  return (
    <div className="App">
      <h1>Car Price Prediction</h1>
      <CarForm onSubmit={handleSubmit} onError={handleError} />
      <PredictedPrice predictedPrice={predictedPrice} />
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default App;
