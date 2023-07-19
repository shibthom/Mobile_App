import streamlit as st
from joblib import load

# Load the trained model
model = load('model.joblib')

st.title('Mobile Price Prediction App')

# Add an image
st.image("mobile.png")  # replace with your own image path



# User inputs on the sidebar
resolution_x = st.sidebar.number_input('Input Resolution X', min_value=0, max_value=5000, value=1080)
resolution_y = st.sidebar.number_input('Input Resolution Y', min_value=0, max_value=5000, value=1920)
processor = st.sidebar.number_input('Input Processor (GHz)', min_value=0, max_value=10, value=2)
ram = st.sidebar.number_input('Input RAM (MB)', min_value=0, max_value=10000, value=4000)

# Predict button
if st.sidebar.button('Predict'):
    inputs = [[resolution_x, resolution_y, processor, ram]]
    prediction = model.predict(inputs)[0]
    st.markdown(f'<h1 style="color: black; text-align: center;">Predicted Price: {prediction}</h1>', unsafe_allow_html=True)