import streamlit as st
import pickle
import numpy as np

st.title("Check the Environment")

carbon_emission = st.number_input("Carbon emission Amount:", min_value=0.0)
energy_output = st.number_input("Energy Output Value:", min_value=0.0)
renewability_index = st.number_input("Renewability Index:", min_value=0.0)
cost_efficiency = st.number_input("Cost efficiency:", min_value=0.0)

# Load trained model
with open("green_tech_model.pkl", "rb") as file:
    model = pickle.load(file)

if st.button("Predict"):
    input_data = np.array([[ 
        carbon_emission,
        energy_output,
        renewability_index,
        cost_efficiency
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Congrats, this environment is sustainable 🌱")
    else:
        st.info("This environment is not sustainable")
