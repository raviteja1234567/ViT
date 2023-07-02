import streamlit as st
from PIL import Image
from transformers import ViTForImageClassification, ViTFeatureExtractor

# Load the pre-trained model and feature extractor
model_path = "/home/ra02983/vit-base-beans/"
model = ViTForImageClassification.from_pretrained(model_path)
feature_extractor = ViTFeatureExtractor.from_pretrained(model_path)

# Set the labels corresponding to the model
labels = ['Among Us', 'Apex Legends', 'Fortnite', 'Forza Horizon', 'Free Fire', 'Genshin Impact', 'God of War', 'Minecraft', 'Roblox', 'Terraria']  # Replace with your own labels

def predict(image):
    # Tokenize the image
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Perform the prediction
    outputs = model(**inputs)
    predicted_label = labels[outputs.logits.argmax(dim=1).item()]
    return predicted_label

# Streamlit web app
def main():
    st.title("Image Classification using ViT")
    st.write("Upload an image in PNG or JPF format and get the predicted label.")

    # Image upload
    uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        image = image.convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Predict the label
        predicted_label = predict(image)
        st.write("Gameplay:", predicted_label)

# Run the web app
if __name__ == "__main__":
    main()
