from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure API Key
genai.configure(api_key=st.secrets("Google_api_key"))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get response
def get_response(input_text, image):
    if input_text.strip():
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit Page Configuration
st.set_page_config(page_title="Image to Text with Gemini", page_icon="📷", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: #4A90E2;
        }
        .upload-box {
            border: 2px dashed #4A90E2;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            background-color: #f9f9f9;
        }
        .response-box {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
            font-size: 16px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .submit-button {
            background-color: #4A90E2;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            width: 100%;
        }
        .submit-button:hover {
            background-color: #357ABD;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 class='title'>📷 Image to Text Generator</h1>", unsafe_allow_html=True)
st.write("Upload an image and enter a prompt to generate a response using **Gemini-1.5 Flash**.")

# Input Section
input_text = st.text_input("📝 Enter a prompt (Optional):", key="input")

# Image Upload Section
st.markdown("<div class='upload-box'>📤 Upload an image (JPG, PNG, JPEG)</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

# Submit Button
if st.button("🔍 Analyze Image", key="submit", help="Click to generate a response"):
    if uploaded_file is None:
        st.warning("⚠️ Please upload an image first.")
    else:
        response = get_response(input_text, image)
        st.subheader("✨ Generated Response:")
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
