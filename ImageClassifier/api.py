from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import tensorflow as tf
import numpy as np
import cv2
import io
from PIL import Image

app = FastAPI(title="Happy-Sad Image Classifier API",
             description="API for classifying images as happy or sad")

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup jinja templates
templates = Jinja2Templates(directory="templates")

# Load the trained model
model = tf.keras.models.load_model('models/happy_sad_model.h5')

# Image preprocessing
def preprocess_image(image):
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize to match training size (assumed to be 256x256)
    image = image.resize((256, 256))
    
    # Convert to numpy array and normalize
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)
    img_array = img_array / 255.0
    
    return img_array

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Validate file
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File provided is not an image")
    
    try:
        # Read and preprocess the image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        processed_image = preprocess_image(image)
        
        # Make prediction
        prediction = model.predict(processed_image)
        probability = float(prediction[0][0])
        
        # Convert probability to label
        label = "happy" if probability >= 0.5 else "sad"
        confidence = probability if label == "happy" else 1 - probability
        
        return {
            "label": label,
            "confidence": float(confidence),
            "probability_happy": float(probability)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
