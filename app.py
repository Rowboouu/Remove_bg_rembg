import streamlit as st
from rembg import remove
from PIL import Image
import io  # Ensure io is imported
import numpy as np

# Function to remove background using Rembg
def remove_background_rembg(image):
    # Convert the image to PNG format and save to a BytesIO stream
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes = image_bytes.getvalue()

    # Use rembg to remove the background
    output = remove(image_bytes)

    # Convert the output bytes back to a PIL image
    output_image = Image.open(io.BytesIO(output)).convert("RGBA")
    return output_image

# Streamlit App
st.title("Background Removal with Rembg")
st.write("Upload an image to remove its background using Rembg.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Original Image", use_container_width=True)

    # Perform background removal
    result = remove_background_rembg(image)

    # Display the result
    st.image(result, caption="Image with Background Removed", use_container_width=True)

st.write("This app uses Rembg for fast and accurate background removal.")
