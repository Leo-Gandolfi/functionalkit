
import streamlit as st
from pdf_converter import convert_to_pdf
from media_extractor import extract_media
from image_converter import convert_image_format

st.set_page_config(page_title="SimpleKitTools", layout="wide")

def ad_box(position="side"):
    styles = {
        "side": "background-color: rgba(255, 255, 255, 0.05); border: 1px solid #444; padding: 20px; margin: 10px; text-align: center; border-radius: 8px; color: #ddd;",
        "top": "background-color: rgba(255, 255, 255, 0.05); border: 1px solid #444; padding: 10px; text-align: center; border-radius: 6px; color: #ddd;",
        "bottom": "background-color: rgba(255, 255, 255, 0.05); border: 1px solid #444; padding: 10px; margin-top: 30px; text-align: center; border-radius: 6px; color: #ddd;"
    }
    return f"<div style='{styles[position]}'>🚀 <b>Your Ad Could Be Here!</b><br><small>Advertise with SimpleKitTools</small></div>"

left_col, center_col, right_col = st.columns([1, 4, 1])

with left_col:
    st.markdown(ad_box("side"), unsafe_allow_html=True)

with center_col:
    st.markdown(ad_box("top"), unsafe_allow_html=True)
    st.title("🛠️ SimpleKitTools")
    st.subheader("Simple, fast tools to make your digital life easier.")

    tabs = st.tabs(["📄 Convert to PDF", "📷 Convert Image Format", "📥 Extract Media"])

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

    with st.container():
        st.markdown("---")
        st.markdown("☕️ **Want to support SimpleKitTools?**", unsafe_allow_html=True)
        st.markdown("If this tool helped you, you can support it with a donation. Every bit helps keep it online and growing!", unsafe_allow_html=True)

        st.markdown("**📬 PIX (for Brazilians):**")
        st.markdown("```pix@simplekittools.com```")
        st.caption("Copy and paste this Pix key in your banking app to send any amount.")

        st.markdown("**🌍 International support via Ko-fi:**")
        st.markdown("[Click here to donate with card or PayPal](https://ko-fi.com/leonardogandolfi)")

        st.markdown(ad_box("bottom"), unsafe_allow_html=True)

    with st.container():
        st.markdown("---")
        st.markdown("💡 **Missing something?**")
        st.markdown("If there's a feature you'd like to see here, or if a tool would make your workflow easier, let me know!")
        st.markdown("📬 Suggestions welcome at: `contact@simplekittools.com`")

with right_col:
    st.markdown(ad_box("side"), unsafe_allow_html=True)
