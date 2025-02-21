import pandas as pd
import streamlit as st

# Google Sheet URL
sheet_url = "https://docs.google.com/spreadsheets/d/14D4QPPGM4I1zQNLXmoZmU9k4MjikF3As9MUEcifAFk8/edit?usp=sharing"

# Extract sheet ID
sheet_id = sheet_url.split('/')[-2]

# Construct the CSV export URL
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

# Read the CSV data into a pandas DataFrame
try:
    df = pd.read_csv(csv_url)
except Exception as e:
    st.error(f"Error: Could not read the Google Sheet. Make sure it's publicly accessible. Details: {e}")
    df = pd.DataFrame({
        'School or District': [],
        'Having trouble with the link on the left? Paste this into your browser instead.': [],
        'Link Text': []
    })

# Streamlit app
st.title("School District Lookup")

# Create a dropdown menu
selected_district = st.selectbox(
    "Select your School or District:",
    df['School or District'].tolist()
)

# Display the result
if selected_district:
    row = df[df['School or District'] == selected_district]
    if not row.empty:
        mailto_link = row['Having trouble with the link on the left? Paste this into your browser instead.'].iloc[0]
        link_text = row['Link Text'].iloc[0]
        st.markdown(f'[**{link_text}**]({mailto_link})', unsafe_allow_html=True)
    else:
        st.write("District not found.")
