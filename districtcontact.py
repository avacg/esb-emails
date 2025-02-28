import pandas as pd
import streamlit as st

# Google Sheet URL
sheet_url = "https://docs.google.com/spreadsheets/d/1wi7E8m37I3bAdDiqJRa1lsR2qmWhKXOL5kL2v0jEbqc/edit?usp=sharing"

# Extract sheet ID
sheet_id = sheet_url.split('/')[-2]

# Construct the CSV export URL
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

# Read the CSV data into a pandas DataFrame
try:
    df = pd.read_csv(csv_url)
    df = df.dropna(subset=['School or District'])
except Exception as e:
    st.error(f"Error: Could not read the Google Sheet. Details: {e}")
    df = pd.DataFrame({
        'School or District': [],
        'Having trouble with the link on the left? Paste this into your browser instead.': [],
        'Link Text': []
    })

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        margin-top: 0px;
        margin-bottom: 20px;  /* Reduced margin */
        width: 100%;
    }
    .header-image-container {
        width: 100%;
        margin: 0 auto;
        margin-bottom: 0px;
    }
    .header-logo {
        width: 100%;
        height: auto;
    }
    .content-container {
        width: min(90vw, 800px);
        margin: 0 auto;
    }
    .title-container {
        background-color: #ffe0a1;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 15px;  /* Reduced margin */
    }
    .description-container {
        background-color: #ffe0a1;
        color: #0c343d;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;  /* Adjusted margin */
        font-size: 18px;
    }
    .email-button-container {
        text-align: center;
        margin: 20px 0;  /* Adjusted margin */
        font-size: 18px;
    }
    .email-button {
        display: inline-block;
        background-color: #0c343d;
        color: #ffffff !important;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 18px;
        transition: transform 0.2s;
        margin-bottom: 20px;  /* Adjusted margin */
    }
    .email-button:hover {
        transform: scale(1.05);
    }
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 30px;
        margin-top: 30px;  /* Adjusted margin */
        flex-wrap: wrap;
    }
    .logo-large {
        width: 100%;
        max-width: 800px;
        height: auto;
        margin: 0 auto;
        display: block;
    }
    .logo-regular1 {
        height: 70px !important;
        width: auto !important;
    }

    }
    .logo-regular2 {
        height: 100px !important;
        width: auto !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page header with logo above title
with st.container():
    st.markdown(
        """
        <div class="header-container">
            <div class="header-image-container">
                <img src="https://iili.io/32d0oGt.png" class="header-logo" alt="MN Advocates for Electric School Buses Logo">
            </div>
            <div class="title-container">
                <h1>Electric School Bus Outreach Tool</h1>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# First description
with st.container():
    st.markdown(
        """
        <div class="description-container">
            Use this tool to send your district a pre-written message supporting electric school buses!
        </div>
        """,
        unsafe_allow_html=True
    )

# Second description (updated text)
with st.container():
    st.markdown(
        """
        <div class="description-container">
            🖱️ 1. Select your school or district from the dropdown menu below.🖱️<br>
            🔗 2. Click the custom email link that's generated for you.🔗<br>
            ✉️ 3. Send the email to your district! ✉️
        </div>
        """,
        unsafe_allow_html=True
    )

# Main content container
with st.container():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    # Create a dropdown menu
    default_text = "Choose an option"
    options = [default_text] + df['School or District'].tolist()
    
    selected_district = st.selectbox(
        "Select your school or district:",
        options,
        index=0  # Ensure a default selection
    )

    # Display the result
    if selected_district and selected_district != default_text:
        row = df[df['School or District'] == selected_district]
        if not row.empty:
            mailto_link = row['Having trouble with the link on the left? Paste this into your browser instead.'].iloc[0]
            link_text = row['Link Text'].iloc[0]
            st.markdown(
                f'<div class="email-button-container">'
                f'<a href="{mailto_link}" class="email-button">{link_text}</a>'
                '</div>',
                unsafe_allow_html=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close content container

# Add logos at the bottom
with st.container():
    st.markdown(
        """ <br> <br>
        <div class="logo-container">
            <img src="https://iili.io/32FWfXs.png" alt="HPHC Logo">
        </div>
        """,
        unsafe_allow_html=True
    )
with st.container():
    st.markdown(
        """
        <div class="logo-container">
            <img src="https://iili.io/32Hqgvj.png" class="logo-regular1" alt="MN350 Logo">
        </div>
        """,
        unsafe_allow_html=True
    )
