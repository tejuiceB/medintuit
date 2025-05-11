from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.model.vit_classifier import predict_disease
from PIL import Image
import io

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    temp_path = "temp_uploaded_image.jpg"
    image.save(temp_path)
    result = predict_disease(temp_path)
    return {
        "prediction": result["label"],
        "confidence": result["confidence"],
        "explanation": result["explanation"]
    }

@app.get("/")
def read_root():
    return {"message": "MediScan API is running. Use /predict to POST an image."}
