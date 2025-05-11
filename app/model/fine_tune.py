from datasets import load_dataset, Dataset
from transformers import AutoImageProcessor, AutoModelForImageClassification, TrainingArguments, Trainer
from transformers import DefaultDataCollator
import os
import torch
from PIL import Image
import glob
from sklearn.metrics import confusion_matrix, classification_report

# Set dataset paths (absolute paths for clarity)
train_dir = os.path.join("data", "chest_xray", "train")
val_dir = os.path.join("data", "chest_xray", "val")

# Manual dataset loading function
def load_image_dataset(directory):
    data = {"image": [], "label": [], "label_name": []}
    
    # Sort class folders for consistent mapping
    class_folders = sorted([f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))])
    label2id = {label: i for i, label in enumerate(class_folders)}
    id2label = {i: label for i, label in enumerate(class_folders)}
    
    for class_name in class_folders:
        class_dir = os.path.join(directory, class_name)
        class_id = label2id[class_name]
        
        # Get all images in this class folder
        image_paths = glob.glob(os.path.join(class_dir, "*.jpeg")) + \
                     glob.glob(os.path.join(class_dir, "*.jpg")) + \
                     glob.glob(os.path.join(class_dir, "*.png"))
        
        for img_path in image_paths:
            try:
                # Load image to ensure it's valid
                image = Image.open(img_path).convert("RGB")
                data["image"].append(image)
                data["label"].append(class_id)
                data["label_name"].append(class_name)
            except Exception as e:
                print(f"Error loading {img_path}: {e}")
    
    return Dataset.from_dict(data), id2label, label2id

# Load datasets
print("Loading train dataset...")
train_dataset, id2label, label2id = load_image_dataset(train_dir)
print("Loading validation dataset...")
val_dataset, _, _ = load_image_dataset(val_dir)

# After loading datasets, print mappings for verification
print("id2label:", id2label)
print("label2id:", label2id)

print(f"Loaded {len(train_dataset)} training images and {len(val_dataset)} validation images")
print(f"Classes: {list(id2label.values())}")

# Define processor and model
model_name = "google/vit-base-patch16-224"
processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

# Replace the classification head
model.classifier = torch.nn.Linear(model.classifier.in_features, len(id2label))
model.config.num_labels = len(id2label)
model.config.id2label = id2label
model.config.label2id = label2id

# Preprocessing function
def transform(example_batch):
    # Process images
    inputs = processor(images=example_batch["image"], return_tensors="pt")
    inputs["labels"] = example_batch["label"]
    return inputs

# Apply transformations
train_dataset.set_transform(transform)
val_dataset.set_transform(transform)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    do_eval=True,
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    save_strategy="epoch",
    logging_dir='./logs',
    logging_steps=10,
)

# Data collator
data_collator = DefaultDataCollator()

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=data_collator,
)

def evaluate_on_dataset(dataset, model, processor, id2label):
    y_true = []
    y_pred = []
    for i in range(len(dataset)):
        img = dataset[i]['image']
        label = dataset[i]['label']
        inputs = processor(images=img, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
            pred_idx = outputs.logits.argmax(-1).item()
        y_true.append(label)
        y_pred.append(pred_idx)
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("Classification Report:")
    print(classification_report(y_true, y_pred, target_names=[id2label[i] for i in sorted(id2label)]))

# Start training
if __name__ == "__main__":
    trainer.train()
    # Example usage after training:
    # evaluate_on_dataset(val_dataset, model, processor, id2label)