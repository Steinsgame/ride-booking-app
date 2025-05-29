import streamlit as st
from PIL import Image
import os

# Set page config
st.set_page_config(page_title="RideEase Home", page_icon="🚖", layout="wide")

# Load images
img_path = "Assets"
book_img = Image.open(os.path.join(img_path, "booking.png"))
details_img = Image.open(os.path.join(img_path, "details.png"))
support_img = Image.open(os.path.join(img_path, "support.png"))

# Title section
st.markdown("<h1 style='text-align: center; font-size: 3rem;'>🚖 Welcome to RideEase</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.3rem;'>Your comfort ride across the city starts here 🚗</p>", unsafe_allow_html=True)

# Spacer
st.markdown("<br><br>", unsafe_allow_html=True)

# Navigation section with images
col1, col2, col3 = st.columns(3)

with col1:
    st.image(book_img, use_column_width=True)  # Changed to use_column_width
    if st.button("🚗 Book a Trip"):
        st.switch_page("pages/ride_booking_app.py")  # Ensure file exists with this exact name

with col2:
    st.image(details_img, use_column_width=True)
    if st.button("📋 View Trip Details"):
        st.switch_page("pages/2📋_Trip_Details.py")  # Fixed typo, ensure file exists

with col3:
    st.image(support_img, use_column_width=True)
    if st.button("💬 Contact Support"):
        st.markdown("[Visit my LinkedIn](https://www.linkedin.com/in/joseph-fadero/)", unsafe_allow_html=True)
