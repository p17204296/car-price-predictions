import React from "react";

// Define the props for the PredictedPrice component
interface PredictedPriceProps {
  predictedPrice: string | undefined; // Predicted price as a string or undefined
}

const PredictedPrice: React.FC<PredictedPriceProps> = ({ predictedPrice }) => {
  // Check if the predicted price is a valid string
  const isPriceValid = typeof predictedPrice === "string";

  return (
    <div className="predicted-price">
      <h2>Predicted Price</h2>
      {isPriceValid ? (
        // If the predicted price is a valid string, display it
        <p>
          Predicted Price: €
          {/* Format the predicted price with 2 decimal places and add thousand separators */}
          {parseFloat(predictedPrice).toLocaleString(undefined, {
            minimumFractionDigits: 2, // Ensure at least 2 decimal places
            maximumFractionDigits: 2, // Allow up to 2 decimal places
          })}
        </p>
      ) : (
        // If the predicted price is not a valid string, display a message
        <p>No predicted price available</p>
      )}
    </div>
  );
};

export default PredictedPrice;
