# MediScan: AI-Powered Web App for Medical Image Diagnosis

MediScan is a full-stack AI application that enables users to upload chest X-ray images and receive:
- Disease classification using Vision Transformers (ViT)
- Explainable heatmaps (Captum)
- Natural language diagnostic reports (LLM)

---

## 🚀 Project Setup

### 1. Create the Folder Structure

```bash
mkdir mediscan
cd mediscan

mkdir app frontend models data notebooks
mkdir app/model app/llm app/utils frontend/assets frontend/utils
touch README.md requirements.txt .gitignore
```

### 2. Initialize Git Repository

```bash
git init
```

Sample `.gitignore`:

```txt
__pycache__/
*.pyc
*.pkl
*.pth
.env
models/
data/
```

### 3. Create a Python Virtual Environment

```bash
python -m venv venv
# On Unix/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 4. Install Core Dependencies

```bash
pip install torch torchvision timm transformers fastapi uvicorn streamlit gradio pillow numpy captum
```

Add to `requirements.txt`:

```txt
torch
torchvision
timm
transformers
fastapi
uvicorn
streamlit
gradio
pillow
numpy
captum
```

### 5. (Optional) Create Initial Placeholder Files

```bash
touch app/main.py
touch frontend/app.py
```

---

## Folder Structure

```
mediscan/
├── README.md
├── requirements.txt
├── .gitignore
├── app/
│   ├── model/
│   ├── llm/
│   └── utils/
├── frontend/
│   ├── assets/
│   └── utils/
├── models/
├── data/
└── notebooks/
```

## Quick Start

1. Clone the repo and install requirements.
2. Train or download the ViT model weights.
3. Run the FastAPI backend and Streamlit frontend.
4. Upload a chest X-ray and view predictions, heatmaps, and reports.

---

## 🏃‍♂️ How to Run the Project with Your Fine-Tuned Model

### 1. Place Your Fine-Tuned Model

- After training, copy the `fine_tuned_model` folder (containing `pytorch_model.bin`, `config.json`, etc.) into `mediscan/app/model/fine_tuned_model`.

### 2. Update Model Loading Code

- In your FastAPI backend (e.g., `app/model/vit_classifier.py`), change:
  ```python
  model_name = "app/model/fine_tuned_model"
  processor = AutoImageProcessor.from_pretrained(model_name)
  model = AutoModelForImageClassification.from_pretrained(model_name)
  ```
- This ensures the backend uses your fine-tuned weights.

### 3. Start the Backend API

```bash
cd mediscan
uvicorn app.main:app --reload
```
- The API will be available at `http://127.0.0.1:8000`.

### 4. Test the API

- Use the provided Python script in `frontend/app.py` or the `/docs` Swagger UI to upload an image and get a prediction.

```bash
python frontend/app.py
```

### 5. (Optional) Run the React Frontend

- Use the provided React component (`ImageUpload.js`) in your frontend React app to upload images and display predictions.

---

## 🧪 Testing the Backend and Frontend

### Test the FastAPI Backend

1. **Start the backend:**
   ```bash
   cd mediscan
   uvicorn app.main:app --reload
   ```
2. **Test with Swagger UI:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
   - Use the `/predict` endpoint to upload an image and see the prediction.

3. **Test with Python script:**
   - Run the provided script:
     ```bash
     python frontend/app.py
     ```
   - This will upload a test image and print the prediction.

---

### Test the React Frontend

1. **Add the `ImageUpload.js` component to your React app.**
2. **Start your React app:**
   ```bash
   cd path/to/your/react/app
   npm start
   ```
3. **Open the app in your browser.**
   - Upload a chest X-ray image.
   - The prediction will be displayed after upload.

---

**Note:**  
- Ensure the backend (`uvicorn`) is running before testing the frontend.
- The backend and frontend can run simultaneously on different ports.

---

**Note:**  
- Make sure all dependencies are installed (`pip install -r requirements.txt`).
- If you retrain or fine-tune again, repeat step 1 to update the model files.

---

**Disclaimer:** AI-aided results – not for clinical use.
