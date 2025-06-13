
import streamlit as st
from pdf_converter import convert_to_pdf
from media_extractor import extract_media
from image_converter import convert_image_format

st.set_page_config(page_title="FunctionalKit", layout="centered")

st.title("🛠️ FunctionalKit")
st.subheader("Simple, fast tools to make your digital life easier.")

tabs = st.tabs(["📄 Convert to PDF", "📷 Convert Image Format", "📥 Extract Media"])

# Tab 1: Convert to PDF
with tabs[0]:
    st.header("Convert Image or Text to PDF")
    uploaded_files = st.file_uploader("Upload image(s) or text file(s):", type=["png", "jpg", "jpeg", "txt", "docx"], accept_multiple_files=True)
    if st.button("Generate PDF"):
        if uploaded_files:
            output_path = convert_to_pdf(uploaded_files)
            st.success("PDF generated successfully!")
            st.download_button("Download PDF", open(output_path, "rb"), file_name="converted.pdf")
        else:
            st.warning("Please upload at least one file.")

# Tab 2: Convert Image Format
with tabs[1]:
    st.header("Convert Image Format")
    image_file = st.file_uploader("Upload image file:", type=["png", "jpg", "jpeg", "webp", "bmp"])
    output_format = st.selectbox("Select output format:", ["PNG", "JPEG", "WEBP", "BMP"])
    if st.button("Convert Image"):
        if image_file:
            result_path = convert_image_format(image_file, output_format)
            st.success("Image converted successfully!")
            st.download_button("Download Converted Image", open(result_path, "rb"), file_name=f"converted.{output_format.lower()}")
        else:
            st.warning("Please upload an image file.")

# Tab 3: Extract Media
with tabs[2]:
    st.header("Extract Audio or Video from Link")
    video_url = st.text_input("Enter video URL (YouTube, TikTok, etc):")
    media_type = st.radio("Select type:", ["Audio (.mp3)", "Video (.mp4)"])
    if st.button("Download Media"):
        if video_url:
            path = extract_media(video_url, media_type)
            label = "audio.mp3" if "Audio" in media_type else "video.mp4"
            st.success("Download ready!")
            st.download_button("Download", open(path, "rb"), file_name=label)
        else:
            st.warning("Please enter a valid URL.")
