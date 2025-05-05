import requests
import base64
import os
import time
import streamlit as st

st.set_page_config(page_title="📸 Smart Image Caption Generator", layout="centered")

OLLAMA_MODEL = "llava"

def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def generate_caption_ollama(image_path, user_context=""):
    image_data = encode_image(image_path)
    
    prompt = "Describe this image as an Instagram caption."
    if user_context:
        prompt += f" Context: {user_context}"

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "images": [image_data],
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        result = response.json()
        return result["response"].strip()
    except Exception as e:
        print("❌ Error talking to Ollama:", e)
        return None

# UI
st.title("🖼️ Smart Image Caption Generator")
st.write("Upload an image and (optionally) describe it to get a more accurate caption.")

uploaded_file = st.file_uploader("📤 Choose an image...", type=["jpg", "jpeg", "png"])
user_context = st.text_input("📝 Optional context about the image (e.g. 'friends on a vacation')")

# Display image 
if uploaded_file:
    st.image(uploaded_file, caption="📷 Uploaded Image", use_column_width=True)

# Button to trigger caption generation
if uploaded_file and st.button("✨ Generate Caption"):
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("⏳ Generating caption...")
    start_time = time.time()
    caption = generate_caption_ollama("temp_image.jpg", user_context)
    end_time = time.time()

    if caption:
        st.subheader("📝 Generated Caption:")
        st.success(caption)
    else:
        st.error("❌ Failed to generate caption.")

    st.write(f"⏱️ Time taken: {end_time - start_time:.2f} seconds.")
elif not uploaded_file:
    st.info("Please upload an image to enable caption generation.")
