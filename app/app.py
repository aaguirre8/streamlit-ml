import pandas as pd
from st_pages import show_pages_from_config
import streamlit as st

from src.authentication import credentials_manager


# Initialize the app
st.set_page_config(
    page_title="Tooling KPI Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Show the pages from the .streamlit/pages.toml config file
# This will change the name of the pages in the sidebar
show_pages_from_config()


# App title
# The title is styled using HTML and CSS combined with the st.markdown function
st.markdown("""
<style>
    .ml-app-title {
        color: #153D64;
        font-size: 48px;
        font-family: font-family: 'Roboto', sans-serif;; 
    }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="ml-app-title">ML App</div>', unsafe_allow_html=True)


# Create layout for the authentication object
col1, col2, col3 = st.columns(3) # This divides the screen in 3 containers, each with a width of 1/3, you can adjust this to your needs

# Create authentication object
with col2:
    # Call custom function to the user credentials
    authenticator = credentials_manager.get_users()
    name, authentication_status, username = authenticator.login("Login", "main")
    # Authentication status is stored in session state, we don't need to store it using st.session_state method

# Validate authentication
if authentication_status:
    st.write("Welcome Lauti")

elif authentication_status is False:
    st.error("The provided username/password is incorrect")


