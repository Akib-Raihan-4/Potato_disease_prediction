from fastapi import FastAPI
import tensorflow as tf
import numpy as np
import uvicorn
from typing_extensions import TypeAlias
from typing_extensions import TypeAliasType
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, HTTPException




app = FastAPI()



model = tf.keras.models.load_model('potatoes.h5')  

class_name = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']  



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def predict(model, img):
    img_array = tf.expand_dims(img, 0)

    predictions = model.predict(img_array)

    predicted_class = class_name[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence



@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    # Ensure the uploaded file is an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload an image.")

    # Convert the uploaded image to a format compatible with the prediction function
    img = tf.keras.preprocessing.image.load_img(BytesIO(await file.read()), target_size=(256, 256))
    img_array = tf.keras.preprocessing.image.img_to_array(img)

    # Perform the prediction
    predicted_class, confidence = predict(model, img_array)

    # Create the response JSON
    response_data = {
        'predicted_class': predicted_class,
        'confidence': confidence
    }

    return response_data




@app.get("/ping")
async def ping():
    return "Hello, I am alive"

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port = 8000)
