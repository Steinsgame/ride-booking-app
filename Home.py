import streamlit as st
from PIL import Image
import os
import pathlib
import sys

# Set page config
st.set_page_config(
    page_title="RideEase Home", 
    page_icon="🚖", 
    layout="wide"
)

# Debugging setup
DEBUG = True  # Set to False in production

def debug_info():
    if DEBUG:
        debug_expander = st.sidebar.expander("Debug Information")
        with debug_expander:
            st.write("### System Path Info")
            st.write(f"Current working directory: {os.getcwd()}")
            st.write(f"Python path: {sys.path}")
            
            st.write("### File Structure")
            try:
                pages_dir = pathlib.Path("pages")
                if pages_dir.exists():
                    st.write("Pages directory contents:")
                    st.write([f.name for f in pages_dir.iterdir() if f.is_file()])
                else:
                    st.error("Pages directory does not exist")
                
                assets_dir = pathlib.Path("Assets")
                if assets_dir.exists():
                    st.write("Assets directory contents:")
                    st.write([f.name for f in assets_dir.iterdir() if f.is_file()])
                else:
                    st.error("Assets directory does not exist")
            except Exception as e:
                st.error(f"Debug error: {e}")

# Load image with robust error handling
def load_image(img_name):
    try:
        img_path = pathlib.Path("Assets") / img_name
        if not img_path.exists():
            raise FileNotFoundError(f"Image not found at {img_path}")
        return Image.open(img_path)
    except Exception as e:
        if DEBUG:
            st.error(f"Image load error ({img_name}): {e}")
        return None

# Safe page navigation
def navigate_to(page_name):
    try:
        # Try direct path first
        page_path = pathlib.Path("pages") / page_name
        if page_path.exists():
            st.switch_page(f"pages/{page_name}")
        
        # Try alternative naming conventions
        alternatives = [
            f"{page_name}.py",
            f"{page_name.lower()}.py",
            f"{page_name.replace(' ', '_')}.py"
        ]
        
        for alt in alternatives:
            alt_path = pathlib.Path("pages") / alt
            if alt_path.exists():
                st.switch_page(f"pages/{alt}")
                return
        
        raise FileNotFoundError(f"No valid page found for {page_name}")
    except Exception as e:
        st.error(f"Navigation failed: {e}")
        if DEBUG:
            st.exception(e)

# Display debug info
debug_info()

# Load images
book_img = load_image("booking.png") or Image.new('RGB', (300, 200), color='gray')
details_img = load_image("details.png") or Image.new('RGB', (300, 200), color='gray')
support_img = load_image("support.png") or Image.new('RGB', (300, 200), color='gray')

# UI Layout
st.markdown("""
    <h1 style='text-align: center; font-size: 3rem;'>
        🚖 Welcome to RideEase
    </h1>
    <p style='text-align: center; font-size: 1.3rem;'>
        Your comfort ride across the city starts here 🚗
    </p>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image(book_img, use_column_width=True)
    if st.button("🚗 Book a Trip", key="book_trip"):
        navigate_to("ride_booking_app.py")

with col2:
    st.image(details_img, use_column_width=True)
    if st.button("📋 View Trip Details", key="trip_details"):
        navigate_to("Trip_Details.py")

with col3:
    st.image(support_img, use_column_width=True)
    if st.button("💬 Contact Support", key="contact_support"):
        st.markdown("""
            <div style='text-align: center;'>
                <h3>Need Help?</h3>
                <a href='https://www.linkedin.com/in/joseph-fadero/' target='_blank'>
                    <button style='
                        background-color: #0077B5; 
                        color: white; 
                        border: none; 
                        padding: 10px 20px; 
                        border-radius: 5px;
                        cursor: pointer;
                    '>
                        Contact on LinkedIn
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: gray;'>
        <hr>
        <p>© 2023 RideEase</p>
    </div>
""", unsafe_allow_html=True)
