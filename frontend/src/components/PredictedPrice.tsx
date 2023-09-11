// src/components/PredictedPrice.tsx
import React from "react";

interface PredictedPriceProps {
  predictedPrice: string | undefined; // Predicted price as a string
}

const PredictedPrice: React.FC<PredictedPriceProps> = ({ predictedPrice }) => {
  const isPriceValid = typeof predictedPrice === "string";

  return (
    <div className="predicted-price">
      <h2>Predicted Price</h2>
      {isPriceValid ? (
        <p>
          Predicted Price: €
          {parseFloat(predictedPrice).toLocaleString(undefined, {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
          })}
        </p>
      ) : (
        <p>No predicted price available</p>
      )}
    </div>
  );
};

export default PredictedPrice;
