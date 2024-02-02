import os

import pandas as pd
import streamlit as st


# Page title
st.markdown("""
<style>
    .datasets-title {
        color: #153D64;
        font-size: 36px;
        font-family: font-family: 'Roboto', sans-serif;; 
    }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="datasets-title">Datasets</div>', unsafe_allow_html=True)

# Add spadding (space)
# Spacing
st.markdown("""
<style>
    .custom-spacing {
        margin-bottom: 20px; /* Adjust the margin as needed for spacing */
    }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="custom-spacing"></div>', unsafe_allow_html=True)


# Create expander to upload a dataset
st.markdown("""
<style>
    .upload-dataset-header {
        color: #153D64;
        font-size: 24px;
        font-family: font-family: 'Roboto', sans-serif;; 
    }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="upload-dataset-header">Upload dataset</div>', unsafe_allow_html=True)
with st.expander(""): # Here we set a blank string to the expander title

    # Create widget to upload a dataset
    uploaded_file = st.file_uploader("", type="csv")

    if uploaded_file is not None:

        # If no tmp folder exists, create it
        if not os.path.exists("tmp"):
            os.makedirs("tmp")

        # Dump file in tmp folder
        with open(f"tmp/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Save file name in session state
        st.session_state.file_name = uploaded_file.name

    else:
        # Here we avoid the an error display when the user has not uploaded a file yet
        # The error is because we are trying to access the file name from session state when is not created yet
        st.stop()


# Create expander to preview the dataset
st.markdown("""
<style>
    .preview-dataset-header {
        color: #153D64;
        font-size: 24px;
        font-family: font-family: 'Roboto', sans-serif;; 
    }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="preview-dataset-header">Preview dataset</div>', unsafe_allow_html=True)
with st.expander(""): # Here we set a blank string to the expander title
    
    # Get the file name from session state
    file_name = st.session_state.file_name

    # Read file
    df = pd.read_csv(f"tmp/{file_name}")

    # Render dataframe
    st.table(df.head(10))

    # Store dataframe in session state to avoid reading the file again
    st.session_state.df = df

    # Display text to explain the next steps
    st.markdown("""
    <style>
        .next-steps-header {
            color: #153D64;
            font-size: 18px;
            font-family: font-family: 'Roboto', sans-serif;; 
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="next-steps-header">Please navigate to model section for next steps</div>', unsafe_allow_html=True)