import streamlit as st
from datetime import datetime
import requests
import json

st.set_page_config(page_title="Book a Ride", page_icon="🚗")

st.title("🚗 Book Your Trip")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

locations = ["Ikeja", "Lekki Phase 1", "Festac", "Ajah", "VI", "Ogba"]
pickup = st.selectbox("Pickup Location", locations)
destination = st.selectbox("Destination", [loc for loc in locations if loc != pickup])

trip_date = st.date_input("Trip Date", min_value=datetime.today())
trip_time = st.time_input("Trip Time")

discount_code = st.text_input("Enter Discount Code (Optional)")

# Pricing logic
def calculate_cost(pickup, destination):
    fares = {
        frozenset(["Ikeja", "Lekki Phase 1"]): 3000,
        frozenset(["Ikeja", "Ogba"]): 1500,
        frozenset(["Ikeja", "Ajah"]): 3500,
        frozenset(["Ikeja", "Festac"]): 4000,
        frozenset(["Lekki Phase 1", "Festac"]): 3000,
        frozenset(["Lekki Phase 1", "Ajah"]): 2000,
        frozenset(["Lekki Phase 1", "VI"]): 1500,
        frozenset(["Lekki Phase 1", "Ogba"]): 2500,
        frozenset(["Ajah", "Festac"]): 4000,
        frozenset(["Ajah", "VI"]): 2500,
        frozenset(["Ajah", "Ogba"]): 3000,
        frozenset(["Festac", "VI"]): 4000,
        frozenset(["Festac", "Ogba"]): 3500,
        frozenset(["VI", "Ogba"]): 3500,
    }
    return fares.get(frozenset([pickup, destination]), 0)

# Discount logic
def apply_discount(cost, code):
    code = code.strip()
    if code == "Joseph123":
        return cost * 0, 100
    elif code == "Joseph555":
        return cost * 0.5, 50
    elif code == "Joseph456":
        return cost * 0.75, 25
    else:
        return cost, 0

# Final cost
base_cost = calculate_cost(pickup, destination)
final_cost, discount_percent = apply_discount(base_cost, discount_code)

st.write(f"### Trip Cost: ₦{int(final_cost):,}")
if discount_percent:
    st.caption(f"💸 Discount Applied: {discount_percent}%")

# Trigger event + navigate
if st.button("🎫 Book Now"):
    if all([first_name, last_name, email, phone, pickup, destination]):
        trip_data = {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "phone": phone,
            "pickup": pickup,
            "destination": destination,
            "tripDate": trip_date.strftime("%Y-%m-%d"),
            "tripTime": trip_time.strftime("%H:%M"),
            "discountCode": discount_code,
            "discountPercent": discount_percent,
            "cost": int(final_cost)
        }

        # Send to Azure Event Hub
        try:
            from azure.eventhub import EventHubProducerClient, EventData

            connection_str = (
                "Endpoint=sb://esehdbyml1002c2lc7xhxy.servicebus.windows.net/;"
                "SharedAccessKeyName=key_1bfc13af-80f7-4684-9ebc-b5df0a73ec76;"
                "SharedAccessKey=/5KMnQposiaf+lxDdy7i9nueNzCgks+xf+AEhDFDOQg=;"
                "EntityPath=es_6b4ffc1d-fa59-4c4b-9708-dbe96a2d0b46"
            )
            eventhub_name = "es_6b4ffc1d-fa59-4c4b-9708-dbe96a2d0b46"

            producer = EventHubProducerClient.from_connection_string(
                conn_str=connection_str,
                eventhub_name=eventhub_name
            )
            event_data_batch = producer.create_batch()
            event_data_batch.add(EventData(json.dumps(trip_data)))
            producer.send_batch(event_data_batch)
            producer.close()

            st.success("✅ Trip successfully booked and sent to Azure Event Hub!")

            # Navigate (simulate by switching session state and rerun)
            st.session_state["trip_details"] = trip_data
            st.switch_page("pages/trip_details.py")

        except Exception as e:
            st.error(f"🚨 Failed to send data to Azure Event Hub: {str(e)}")
