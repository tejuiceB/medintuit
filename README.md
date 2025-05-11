# MediScan: AI-Powered Chest X-ray Diagnosis

MediScan is a full-stack AI application for automated chest X-ray analysis. It leverages a fine-tuned Vision Transformer (ViT) model to classify images as **NORMAL** or **PNEUMONIA** and provides explainable, human-readable observations for each prediction.

---

## 🖼️ Example Prediction

![MediScan Prediction Example](https://github.com/tejuiceB/medintuit/raw/main/frontend/screenshots/image.png)

---

## 🚀 Features

- **Disease Classification:** Predicts NORMAL or PNEUMONIA from chest X-ray images.
- **Explainable AI:** Returns detailed, radiology-style observations for each prediction.
- **REST API:** FastAPI backend for easy integration.
- **Frontend:** React-based UI for image upload and result display.
- **Easy Deployment:** Run locally with minimal setup.

---

## 📂 Project Structure

```
mediscan/
├── app/                # FastAPI backend
│   ├── main.py
│   └── model/
│       ├── vit_classifier.py
│       ├── fine_tune.py
│       └── fine_tuned_model/
│           ├── config.json
│           ├── preprocessor_config.json
│           └── pytorch_model.bin
├── frontend/           # React frontend
│   ├── src/
│   │   ├── App.js
│   │   ├── ImageUpload.js
│   │   └── index.js
│   └── public/
├── data/               # Data (not included in repo)
│   └── chest_xray/
│       ├── train/
│       ├── val/
│       └── test/
├── notebooks/          # Jupyter/Colab notebooks
│   └── finetune_vit_chestxray_colab.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

- **Source:** [Chest X-Ray Images (Pneumonia) | Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- **Structure:**
  - `train/` - Training images (NORMAL, PNEUMONIA)
  - `val/` - Validation images (NORMAL, PNEUMONIA)
  - `test/` - Test images (NORMAL, PNEUMONIA)

**Note:**  
Download the dataset from Kaggle and place it in `mediscan/data/chest_xray/`.

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mediscan.git
cd mediscan
```

### 2. Install Python Dependencies

```bash
python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On Unix/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Prepare the Dataset

- Download from [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia).
- Place the folders as:
  ```
  mediscan/data/chest_xray/train/
  mediscan/data/chest_xray/val/
  mediscan/data/chest_xray/test/
  ```

### 4. (Optional) Fine-tune the Model

- Use the provided notebook:  
  [`notebooks/finetune_vit_chestxray_colab.ipynb`](../notebooks/finetune_vit_chestxray_colab.ipynb)
- Or run the script:  
  `python app/model/fine_tune.py`
- Save the resulting model files in `app/model/fine_tuned_model/`.

### 5. Start the Backend API

```bash
uvicorn app.main:app --reload
```
- The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 6. (Optional) Start the Frontend

- Navigate to `frontend/` and run:
  ```bash
  npm install
  npm start
  ```
- Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🧪 Usage

### Predict via API

Send a POST request to `/predict` with an X-ray image:

```python
import requests

with open("path_to_image.jpeg", "rb") as f:
    response = requests.post("http://127.0.0.1:8000/predict", files={"file": f})
print(response.json())
```

**Response Example:**
```json
{
  "prediction": "PNEUMONIA",
  "confidence": 0.95,
  "explanation": "The model detected the following observations in the X-ray image: ..."
}
```

### Predict via Frontend

- Open the React app in your browser.
- Upload a chest X-ray image.
- View the prediction and detailed observations.

---

## 📒 Notebooks

- [`finetune_vit_chestxray_colab.ipynb`](../notebooks/finetune_vit_chestxray_colab.ipynb):  
  Step-by-step guide for fine-tuning ViT on the chest X-ray dataset.

---

## 📝 Model Details

- **Architecture:** Vision Transformer (ViT)
- **Pretrained Weights:** `google/vit-base-patch16-224`
- **Fine-tuning:** Only the classification head is trained on the chest X-ray dataset.
- **Classes:** NORMAL, PNEUMONIA

---

## 🔗 Useful Links

- [Kaggle Chest X-ray Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Vision Transformer Paper](https://arxiv.org/abs/2010.11929)

---

## ⚠️ Disclaimer

This project is for research and educational purposes only.  
**Not for clinical use.**

---

## 📧 Contact

For questions or contributions, open an issue or pull request on [GitHub](https://github.com/yourusername/mediscan).
