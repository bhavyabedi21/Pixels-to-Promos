import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configuring the Key and initiating the model
genai.configure(api_key=os.getenv('GOOGLE-API-KEY'))
model = genai.GenerativeModel('gemini-1.5-flash') # best suitable for images

# Designing the Front End
st.header("📄PixelsToPromos:blue[.ai]: Turning Visuals into Words with AI",divider="green")

st.subheader("📝 What kind of text output do you want to generate?", divider=True)
prompt = st.text_input("Enter prompt below..",placeholder="e.g. captions, product descriptions, ad copy, insights...")

st.subheader("📥 Upload Your Image")
uploaded_img = st.file_uploader("Choose an image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

# Image Display
img = ""
if uploaded_img is not None:
    image = Image.open(uploaded_img)
    st.image(image,use_container_width=True)

def get_llm_response(prompt,image):
    if prompt != "":
        response = model.generate_content([prompt,image]).text
    else:
        response = model.generate_content([prompt]).text
    return response

submit = st.button("🚀 Get AI-Powered Insights")
if submit:
    response = get_llm_response(prompt,image)
    st.markdown("### ✨ Generated Output")
    st.write(response)