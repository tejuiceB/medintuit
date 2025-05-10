import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.model.vit_classifier import predict_disease

# Replace with your test image path
image_path = r"C:\Users\Tejas\OneDrive\Desktop\MedIntuit\mediscan\data\chest_xray\test\PNEUMONIA\person1_virus_6.jpeg"
result = predict_disease(image_path)

print("Prediction:", result)
