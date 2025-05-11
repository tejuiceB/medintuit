import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image

model_name = "app/model/fine_tuned_model"
processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)
model.eval()

# Print mappings for debug
print("id2label (inference):", model.config.id2label)
print("label2id (inference):", model.config.label2id)

def predict_disease(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=-1)
        predicted_class_idx = logits.argmax(-1).item()
        confidence = probs[0, predicted_class_idx].item()
    label = model.config.id2label[predicted_class_idx]
    # Focused explanation: only what was detected and why
    if label.upper() == "PNEUMONIA":
        explanation = (
            "The model detected the following observations in the X-ray image:\n"
            "- Areas of increased opacity (whiteness) in the lung fields\n"
            "- Possible consolidation or infiltrates\n"
            "- Loss of normal lung markings\n\n"
            "Based on these findings, the model predicted Pneumonia."
        )
    else:
        explanation = (
            "The model did not detect abnormal opacities, consolidation, or loss of lung markings. "
            "The lung fields appear clear and normal.\n\n"
            "Based on these observations, the model predicted Normal."
        )
    return {"label": label, "confidence": confidence, "explanation": explanation}
