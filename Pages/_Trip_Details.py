import streamlit as st

st.set_page_config(page_title="Trip Details", page_icon="🧾")

trip = st.session_state.get("trip_details")

if trip:
    st.title("🧾 Trip Details")

    st.write(f"**Name:** {trip['firstName']} {trip['lastName']}")
    st.write(f"**Email:** {trip['email']}")
    st.write(f"**Phone:** {trip['phone']}")
    st.write(f"**From:** {trip['pickup']}")
    st.write(f"**To:** {trip['destination']}")
    st.write(f"**Date:** {trip['tripDate']}")
    st.write(f"**Time:** {trip['tripTime']}")
    st.write(f"**Discount Code:** {trip['discountCode'] or 'None'}")
    st.write(f"**Discount Applied:** {trip['discountPercent']}%")
    st.markdown(f"### 💰 Total Cost: ₦{trip['cost']:,}")
else:
    st.warning("No trip data found. Please book a trip first.")
