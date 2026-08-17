import streamlit as st
from snowflake.snowpark.context import get_active_session

# Connect to Snowflake
session = get_active_session()

# -------------------------
# App Title
# -------------------------

st.title("🌍 Travel Companion")

st.header("Travel Booking Form")

# -------------------------
# Travel Details
# -------------------------

trip_id = st.number_input("Trip ID", min_value=1, step=1)

traveler_name = st.text_input("Traveler Name")

source_city = st.text_input("Source City")

destination = st.text_input("Destination")

departure_date = st.date_input("Departure Date")

return_date = st.date_input("Return Date")

transport_mode = st.selectbox(
    "Transport Mode",
    ["Flight", "Train", "Bus", "Car"]
)

hotel_name = st.text_input("Hotel Name")

number_of_travelers = st.number_input(
    "Number of Travelers",
    min_value=1,
    step=1
)

budget = st.number_input(
    "Budget",
    min_value=0.0,
    step=100.0
)

contact_number = st.text_input("Contact Number")

email = st.text_input("Email")

special_requests = st.text_area("Special Requests")

# -------------------------
# Submit Button
# -------------------------

if st.button("Save Travel Plan"):

    session.sql(f"""
    INSERT INTO TRAVEL_DB.PUBLIC.TRAVEL_PLANS
    (
        TRIP_ID,
        TRAVELER_NAME,
        SOURCE_CITY,
        DESTINATION,
        DEPARTURE_DATE,
        RETURN_DATE,
        TRANSPORT_MODE,
        HOTEL_NAME,
        NUMBER_OF_TRAVELERS,
        BUDGET,
        CONTACT_NUMBER,
        EMAIL,
        SPECIAL_REQUESTS
    )

    VALUES
    (
        {trip_id},
        '{traveler_name}',
        '{source_city}',
        '{destination}',
        '{departure_date}',
        '{return_date}',
        '{transport_mode}',
        '{hotel_name}',
        {number_of_travelers},
        {budget},
        '{contact_number}',
        '{email}',
        '{special_requests}'
    )
    """).collect()

    st.success("✅ Travel plan saved successfully!")
