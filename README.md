
# Potato Plant Disease Detection

Potato Plant Disease Detection is a project aimed at detecting two major diseases in potato plants, namely Early Blight, Late Blight, and Healthy plants. The project involves training a deep learning model using TensorFlow and Keras, achieving an impressive accuracy of 97%. Additionally, the model is connected to a web application using FastAPI, which allows users to interact with the model through a user-friendly interface built using React and basic HTML, CSS, and JS.

# Dataset
The dataset used for training the model was obtained from Kaggle and can be found at the following link: [Potato Plant Disease Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village)
. It contains images of potato plants affected by Early Blight, Late Blight, and Healthy plants.

# Model Training
The model was trained using TensorFlow and Keras libraries. The dataset of potato plant images was split into training, testing and validation sets to prevent overfitting. The deep learning model was trained on the training set and validated on the validation set to achieve the reported accuracy of 97%. The trained model is then saved for later use in the web application.

# Visualizing Model Accuracy
To visualize the accuracy of the trained model, Matplotlib was used. The accuracy metrics of the model are displayed graphically, providing insights into the model's performance during the training process.

## Screenshots

![Web App without uploading](https://github.com/Akib-Raihan-4/Potato_disease_prediction/blob/main/Visualizing%20the%20training%20and%20validation%20accuracy%20and%20their%20loss.png)

# Web Application
The web application is built using FastAPI, a modern, fast, web framework for building APIs with Python. The trained model is integrated with the web application, enabling users to upload images of potato plants and get predictions for their health status (Early Blight, Late Blight, or Healthy). The frontend of the web app is developed with React and also with HTML, CSS, and JavaScript to create an interactive and user-friendly experience.

## Screenshots

![Web App without uploading](https://github.com/Akib-Raihan-4/Potato_disease_prediction/blob/main/SS_Frontend-without-prediction.png)


## Screenshots

![Web App with uploading](https://github.com/Akib-Raihan-4/Potato_disease_prediction/blob/main/SS_Frontend-with-prediction.png)

# Conclusion
Potato Plant Disease Detection is a comprehensive project that combines deep learning, web development, and data visualization to detect diseases in potato plants accurately. The trained model achieves a high accuracy of 97%, making it a valuable tool for farmers and researchers in identifying plant diseases early on and taking appropriate actions to protect their crops.
