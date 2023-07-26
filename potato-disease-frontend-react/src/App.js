import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [prediction, setPrediction] = useState(null);

  const handleImageChange = async (event) => {
    const formData = new FormData();
    formData.append('file', event.target.files[0]);

    try {
      const response = await fetch("http://localhost:8000/predict/", {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      setPrediction(data);
    } catch (error) {
      console.error('Error predicting:', error);
    }

    setSelectedImage(URL.createObjectURL(event.target.files[0]));
  };

  return (
    <div className="container flex flex-col items-center justify-center h-screen">
      <h1 className="text-4xl font-bold text-blue-700 mb-8">Potato Plant Disease Detection</h1>
      <div className="mb-4">
        <label htmlFor="imageFile" className="custom-file-input">
          Choose File
        </label>
        <input
          type="file"
          id="imageFile"
          accept="image/*"
          onChange={handleImageChange}
          className="hidden"
        />
      </div>
      <div className="imagePreviewWrapper mb-4">
        {selectedImage && <img src={selectedImage} alt="Uploaded Image" className="imagePreview" />}
      </div>
      {prediction && (
        <div className="text-center">
          <h2 className="text-green-700 font-bold text-xl">Prediction:</h2>
          <p>Predicted Class: {prediction.predicted_class}</p>
          <p>Confidence: {prediction.confidence}%</p>
        </div>
      )}
    </div>
  );
}

export default App;
