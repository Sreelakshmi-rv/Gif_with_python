import streamlit as st
import imageio.v3 as iio
from PIL import Image
import io

# --- Page Configuration ---
st.set_page_config(
    page_title="GIF Creator",
    page_icon="✨"
)

# --- App UI ---
st.title("Simple GIF Creator 🖼️")
st.info("Instructions: Upload two images of the same dimensions (PNG or JPG). A GIF will be generated which you can then preview and download.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Image 1")
    uploaded_file1 = st.file_uploader("Upload the first image", type=['png', 'jpg', 'jpeg'], key="uploader1")

with col2:
    st.subheader("Image 2")
    uploaded_file2 = st.file_uploader("Upload the second image", type=['png', 'jpg', 'jpeg'], key="uploader2")

# --- GIF Generation and Download Logic ---
if uploaded_file1 is not None and uploaded_file2 is not None:
    image1 = Image.open(uploaded_file1)
    image2 = Image.open(uploaded_file2)

    # --- NEW LOGIC: Check if image dimensions are the same ---
    if image1.size == image2.size:
        # If sizes match, proceed to create the GIF
        st.success("Image dimensions match! Creating your GIF...")
        
        images = [image1, image2]
        gif_bytes = io.BytesIO()
        iio.imwrite(gif_bytes, images, format='GIF', duration=0.5, loop=0)
        gif_bytes.seek(0)

        st.subheader("Your Generated GIF")
        st.image(gif_bytes, caption='Your awesome GIF!')

        st.download_button(
            label="Download GIF",
            data=gif_bytes,
            file_name="generated_gif.gif",
            mime="image/gif"
        )
    else:
        # If sizes don't match, show an error message with the dimensions
        st.error(
            f"Image dimensions do not match. Please upload images of the same size.\n"
            f"- **Image 1:** {image1.size[0]}x{image1.size[1]} pixels\n"
            f"- **Image 2:** {image2.size[0]}x{image2.size[1]} pixels"
        )
# --- END OF NEW LOGIC ---
