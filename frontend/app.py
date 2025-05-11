import requests

def predict_image(image_path):
    url = "http://127.0.0.1:8000/predict"
    with open(image_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
    print("Response:", response.json())

if __name__ == "__main__":
    # Example usage: replace with your test image path
    test_image = r"C:\Users\Tejas\OneDrive\Desktop\MedIntuit\mediscan\data\chest_xray\test\PNEUMONIA\person1_virus_6.jpeg"
    predict_image(test_image)
