import streamlit as st
import numpy as np
import pickle
import time

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Page Configurations
st.set_page_config(page_title="Concrete Strength Predictor", page_icon="🏗️", layout="wide")

# Sidebar Title
st.sidebar.title("🔧 Input Parameters")

# Input Sliders
cement = st.sidebar.slider("Cement (kg/m³)", 100, 500, 250)
blast_furnace_slag = st.sidebar.slider("Blast Furnace Slag (kg/m³)", 0, 400, 100)
fly_ash = st.sidebar.slider("Fly Ash (kg/m³)", 0, 300, 50)
water = st.sidebar.slider("Water (kg/m³)", 100, 250, 150)
superplasticizer = st.sidebar.slider("Superplasticizer (kg/m³)", 0, 50, 5)
coarse_aggregate = st.sidebar.slider("Coarse Aggregate (kg/m³)", 700, 1200, 900)
fine_aggregate = st.sidebar.slider("Fine Aggregate (kg/m³)", 500, 1000, 800)
age = st.sidebar.slider("Age (Days)", 1, 365, 28)

# Prepare Input Data
input_data = np.array([[cement, blast_furnace_slag, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age]])
input_data_scaled = scaler.transform(input_data)

# UI Design
st.title("🏗️ Concrete Compressive Strength Prediction")
st.markdown("### Enter the values in the sidebar and click 'Predict' to get results!")

st.image("img.png", use_container_width=True)


if st.button("Predict Strength 🚀"):
    with st.spinner("Calculating Strength..."):
        time.sleep(2)  # Simulate processing time
        prediction = model.predict(input_data_scaled)[0]
        
        # Display results with color formatting
        if prediction < 20:
            st.error(f"🚨 Low Strength: {prediction:.2f} MPa")
        elif 20 <= prediction < 50:
            st.warning(f"⚠️ Medium Strength: {prediction:.2f} MPa")
        else:
            st.success(f"✅ High Strength: {prediction:.2f} MPa")

# Footer
st.markdown("---")
st.markdown("**Developed by Anchal Vishwakarma | 2025**")
