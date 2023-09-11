import styled from "styled-components";

export const StyledFormContainer = styled.form`
  display: flex;
  flex-direction: column;
  max-width: 400px;
  margin: 0 auto;
`;

export const StyledLabel = styled.label`
  font-weight: bold;
  margin-bottom: 5px;
`;

export const StyledInput = styled.input`
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
`;

export const StyledButton = styled.button`
  background-color: #007bff;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 18px;
`;

export const StyledErrorText = styled.p`
  color: red;
  margin-top: 10px;
`;
