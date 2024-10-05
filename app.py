import streamlit as st
from PIL import Image
import pytesseract

# Set tesseract path (adjust it to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\textextraction\tesseract\Tesseract-OCR\tesseract.exe'  # For Windows

def extract_text_from_image(image):
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    return text

st.title("Text Extraction from Image using OCR")

# Upload an image
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg", "webp"])

if uploaded_image is not None:
    # Open the image file
    image = Image.open(uploaded_image)

    # Display the uploaded image
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Extract text from the image
    extracted_text = extract_text_from_image(image)

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(extracted_text)
