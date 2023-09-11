// src/components/CarForm.tsx
import React, { useState } from "react";
import {
  StyledFormContainer,
  StyledLabel,
  StyledInput,
  StyledButton,
  StyledErrorText,
} from "./CarFormStyles/CarFormStyles";

interface CarFormProps {
  onSubmit: (predictedPrice: string) => void; // Change the type to string
  onError: (error: string) => void;
}

const CarForm: React.FC<CarFormProps> = ({ onSubmit, onError }) => {
  const [carData, setCarData] = useState({
    brand: "",
    year: 2020, // Set as a number
    fuel: "",
    gearbox: "",
    mileage: 10000, // Set as a number
  });

  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log(carData);
    try {
      // Simulate an API request
      // Replace this with your actual API call
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

      const data = await response.json();
      // Ensure data.predicted_price_eur is extracted as a string
      const predictedPrice = data.predicted_price_eur.toString();

      // If successful, call onSubmit with the extracted predicted price
      onSubmit(predictedPrice);

      // Clear any previous errors
      setError(null);
    } catch (error) {
      // Handle the error and call onError with the error message
      setError((error as Error).message || "An error occurred.");
    }
  };

  return (
    <StyledFormContainer onSubmit={handleSubmit}>
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

      <StyledButton type="submit">Predict Price</StyledButton>

      {/* Display error message */}
      {error && <StyledErrorText>{error}</StyledErrorText>}
    </StyledFormContainer>
  );
};

export default CarForm;
