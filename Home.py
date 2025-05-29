import streamlit as st
from PIL import Image
import os
import pathlib

# Set page config
st.set_page_config(
    page_title="RideEase Home", 
    page_icon="🚖", 
    layout="wide",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/joseph-fadero/',
        'About': "### RideEase - Your Comfort Ride Across The City"
    }
)

# Debugging - shows files in pages directory (can remove after confirming it works)
st.sidebar.write("Debug Info:")
try:
    pages_dir = pathlib.Path("pages")
    st.sidebar.write("Pages available:", [f.name for f in pages_dir.iterdir() if f.is_file()])
except Exception as e:
    st.sidebar.error(f"Couldn't read pages directory: {e}")

# Load images function with error handling
def load_image(img_name):
    try:
        img_path = pathlib.Path("Assets") / img_name
        return Image.open(img_path)
    except Exception as e:
        st.error(f"Couldn't load image {img_name}: {e}")
        return None

# Load images
book_img = load_image("booking.png")
details_img = load_image("details.png")
support_img = load_image("support.png")

# Title section
st.markdown("""
    <h1 style='text-align: center; font-size: 3rem;'>
        🚖 Welcome to RideEase
    </h1>
    <p style='text-align: center; font-size: 1.3rem;'>
        Your comfort ride across the city starts here 🚗
    </p>
""", unsafe_allow_html=True)

# Spacer
st.markdown("<br><br>", unsafe_allow_html=True)

# Navigation section with images
col1, col2, col3 = st.columns(3)

with col1:
    if book_img:
        st.image(book_img, use_column_width=True)
    if st.button("🚗 Book a Trip", key="book_trip", help="Book a new ride"):
        try:
            st.switch_page("pages/ride_booking_app.py")
        except Exception as e:
            st.error(f"Couldn't navigate to booking page: {e}")

with col2:
    if details_img:
        st.image(details_img, use_column_width=True)
    if st.button("📋 View Trip Details", key="trip_details", help="View your current trips"):
        try:
            st.switch_page("pages/Trip_Details.py")
        except Exception as e:
            st.error(f"Couldn't navigate to trip details: {e}")

with col3:
    if support_img:
        st.image(support_img, use_column_width=True)
    if st.button("💬 Contact Support", key="contact_support"):
        st.markdown("""
            <div style='text-align: center;'>
                <h3>Need Help?</h3>
                <p>Contact us through:</p>
                <a href='https://www.linkedin.com/in/joseph-fadero/'>
                    <button style='background-color: #0077B5; color: white; border: none; padding: 10px 20px; border-radius: 5px;'>
                        LinkedIn
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: gray;'>
        <hr>
        <p>© 2023 RideEase - All Rights Reserved</p>
    </div>
""", unsafe_allow_html=True)
