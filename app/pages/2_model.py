import json

import pandas as pd
import streamlit as st

from src.machine_learning.PreProcessing import PreprocessingStep
from src.machine_learning.Imputation import ImputationStep


# Initialize session state variables
# We need to initialize session state variables before we use them, otyherwise it will raise an error

if "is_data_available" not in st.session_state:
    st.session_state.is_data_available = False

if "selected_models" not in st.session_state:
    st.session_state.selected_models = None

if "execute_model" not in st.session_state:
    st.session_state.execute_model = False


# Page title
st.markdown("""
<style>
    .model-title {
        color: #153D64;
        font-size: 36px;
        font-family: font-family: 'Roboto', sans-serif;; 
    }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="model-title">Models</div>', unsafe_allow_html=True)

# Add spadding (space)
st.markdown("""
<style>
    .custom-spacing {
        margin-bottom: 20px; /* Adjust the margin as needed for spacing */
    }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="custom-spacing"></div>', unsafe_allow_html=True)


try:

    # Check if the dataset is uploaded
    if st.session_state.df is not None:

        # Create session state variable to tell the app is ok to continue
        st.session_state.is_data_available = True

        pass

except Exception:
    st.warning("Please upload a dataset first")
    pass


# Here we call the is_data_available session state variable, we do this to avoid nesting the code inside the try context and if statement
if st.session_state.is_data_available:

    # Create multibox select to choose the ML model
    st.markdown("""
    <style>
        .list-ml-subheader {
            color: #153D64;
            font-size: 24px;
            font-family: font-family: 'Roboto', sans-serif;; 
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="list-ml-subheader">Select Model</div>', unsafe_allow_html=True)

    # Read input parameters <models>
    file_path = "src/input_params/models.json"
    with open(file_path, 'r') as file:
        # Load the JSON data from file
        data = json.load(file)
        models_list = list(data.values())

    selected_models = st.multiselect(
        "",
        options=models_list,
        help="Select one or more models to use"
    )

    # Store the selected models in session state
    st.session_state.selected_models = selected_models


# Check if the user has selected a model
if st.session_state.selected_models:
    
    st.markdown("""
    <style>
        .model-params-subheader {
            color: #153D64;
            font-size: 24px;
            font-family: font-family: 'Roboto', sans-serif;; 
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="model-params-subheader">Input parameters</div>', unsafe_allow_html=True)


    # Create label for the input parameters
    st.markdown("""
    <style>
        .training-percentage-text-subheader {
            color: #153D64;
            font-size: 18px;
            font-family: font-family: 'Roboto', sans-serif;; 
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="training-percentage-text">Select the training dataset percentage</div>', unsafe_allow_html=True)

    # Create layout for the input parameters
    col1, col2, col3 = st.columns(3)

    with col1:

        # Create button to input the training %
        training_percentage = st.number_input(
            label="",
            min_value=0.1,
            max_value=.95,
        )

        # Create button to start the modelling
        st.write("") # add padding
        if st.button("Start modelling"):

            # Load the dataset
            df = st.session_state.df

            pass