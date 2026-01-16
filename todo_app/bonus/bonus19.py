import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

def convert(fp):
    # Convert Capture to a pillow image
    img = Image.open(fp)
    # Convert the image to grayscale
    gray_img = img.convert("L")

    # Show the converted image
    st.image(gray_img)

uploaded_image = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])
if uploaded_image is not None:
    convert(uploaded_image)

with st.expander("Start Camera"):
    # Open camera and capture
    camera_image = st.camera_input("Camera")

if camera_image is not None:
    convert(camera_image)