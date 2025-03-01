# # assets_streamlit_app.py
# import streamlit as st
# import pandas as pd

# def app():
#     st.title("Asset Management")

#     # Example form to add an asset
#     asset_name = st.text_input("Asset Name")
#     asset_location = st.text_input("Location")
#     asset_status = st.selectbox("Status", ["Active", "Inactive"])

#     if st.button("Add Asset"):
#         st.write(f"Asset Added: {asset_name}, Location: {asset_location}, Status: {asset_status}")

# if __name__ == "__main__":
#     app()

import streamlit as st
import pandas as pd
from sqlalchemy.orm import sessionmaker
from assets.db import engine

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Function to generate Domain ID
def generate_domain_id(company, device_type, serial):
    company_abbr = company[:3].upper()
    device_letter = 'L' if device_type == 'Laptop' else 'D'
    dept = "ICT"
    serial_suffix = serial[-4:]
    return f"{company_abbr}-{device_letter}-{dept}-{serial_suffix}"

# Streamlit App
def app():
    st.title("Asset Management System")

    # Asset Input Form
    asset_name = st.text_input("Asset Name")
    assigned_user = st.text_input("Assigned User (if any)")
    user_company = st.text_input("User Company")
    device_type = st.selectbox("Device Type", ["Laptop", "Desktop"])
    asset_code = st.text_input("Asset Code (if available)")
    product_number = st.text_input("Product Number")
    serial_number = st.text_input("Serial Number")

    # Desktop-specific fields
    if device_type == "Desktop":
        keyboard = st.checkbox("Has Keyboard?")
        monitor = st.checkbox("Has Monitor?")
        mouse = st.checkbox("Has Mouse?")
    else:
        keyboard, monitor, mouse = False, False, False

    additional_info = st.text_area("Additional Info")

    # Generate Domain ID
    domain_id = generate_domain_id(user_company, device_type, serial_number)
    st.write(f"Generated Domain ID: **{domain_id}**")

    if st.button("Add Asset"):
        try:
            with engine.connect() as conn:
                query = f"""
                INSERT INTO assets (name, assigned_user, user_company, device_type, asset_code, product_number, 
                serial_number, domain_id, additional_info, keyboard, monitor, mouse)
                VALUES ('{asset_name}', '{assigned_user}', '{user_company}', '{device_type}', '{asset_code}', 
                '{product_number}', '{serial_number}', '{domain_id}', '{additional_info}', {keyboard}, {monitor}, {mouse})
                """
                conn.execute(query)
                st.success(f"Asset '{asset_name}' added successfully with Domain ID: {domain_id}")
        except Exception as e:
            st.error(f"Error adding asset: {e}")

    # Fetch and display assets
    if st.button("View Assets"):
        df = pd.read_sql("SELECT * FROM assets", con=engine)
        st.write(df)

if __name__ == "__main__":
    app()
