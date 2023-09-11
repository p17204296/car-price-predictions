import React, { useState } from "react";
import {
  StyledFormContainer,
  StyledLabel,
  StyledInput,
  StyledButton,
  StyledErrorText,
} from "./CarFormStyles/CarFormStyles";

interface CarFormProps {
  // Define the props for the CarForm component
  // 'onSubmit' is a callback function to handle form submission
  // 'onError' is a callback function to handle errors
  onSubmit: (predictedPrice: string) => void; // Change the type to string
  onError: (error: string) => void;
}

const CarForm: React.FC<CarFormProps> = ({ onSubmit, onError }) => {
  // Initialize state to store car data and error messages
  const [carData, setCarData] = useState({
    brand: "BMW",
    year: 2020, // Year as a number
    fuel: "Gasolina",
    gearbox: "Manual",
    mileage: 10000, // Mileage as a number
  });

  const [error, setError] = useState<string | null>(null);

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      // Simulate an API request
      const response = await fetch("/api/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(carData),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }

      // Parse the response data
      const data = await response.json();

      // Extract the predicted price as a string
      const predictedPrice = data.predicted_price_eur.toString();

      // Call the 'onSubmit' callback with the predicted price
      onSubmit(predictedPrice);

      // Clear any previous errors
      setError(null);
    } catch (error) {
      // Handle any errors that occur during the API request
      setError((error as Error).message || "An error occurred.");
    }
  };

  return (
    <StyledFormContainer onSubmit={handleSubmit}>
      {/* Form inputs */}
      <StyledLabel>Brand:</StyledLabel>
      <StyledInput
        type="text"
        name="brand"
        value={carData.brand}
        onChange={(e) => setCarData({ ...carData, brand: e.target.value })}
        required
      />

      <StyledLabel>Year:</StyledLabel>
      <StyledInput
        type="number"
        name="year"
        value={carData.year}
        onChange={(e) =>
          setCarData({ ...carData, year: e.target.valueAsNumber })
        }
        required
      />

      <StyledLabel>Fuel:</StyledLabel>
      <StyledInput
        type="text"
        name="fuel"
        value={carData.fuel}
        onChange={(e) => setCarData({ ...carData, fuel: e.target.value })}
        required
      />

      <StyledLabel>Gearbox:</StyledLabel>
      <StyledInput
        type="text"
        name="gearbox"
        value={carData.gearbox}
        onChange={(e) => setCarData({ ...carData, gearbox: e.target.value })}
        required
      />

      <StyledLabel>Mileage:</StyledLabel>
      <StyledInput
        type="number"
        name="mileage"
        value={carData.mileage}
        onChange={(e) =>
          setCarData({ ...carData, mileage: e.target.valueAsNumber })
        }
        required
      />

      {/* Submit button */}
      <StyledButton type="submit">Predict Price</StyledButton>

      {/* Display error message if there's an error */}
      {error && <StyledErrorText>{error}</StyledErrorText>}
    </StyledFormContainer>
  );
};

export default CarForm;
