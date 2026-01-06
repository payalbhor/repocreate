# import streamlit as st
# import pickle
# import numpy as np
# st.title("Check the Environment")
# #input data
# carbon_emission=st.number_input("Carbon emission Amount:",min_calue=0.0,format="%f")
# energy_output=st.number_input("Energy Output Value:",min_calue=0.0,format="%f")
# renewability_index=st.number_input("Renewability_ Index:",min_calue=0.0,format="%f")
# cost_efficiency=st.number_input("Cost_ efficiency:",min_calue=0.0,format="%f")

# #Model Importing
# with open('green_tech_model.pkl','rb') as file:
#     model=pickle.load(file)
# #predict
# if st.button("Predict"):
#      input_data=np.array([[carbon_emission,energy_output,renewability_index,cost_efficiency]])

#      prediction=model.predict(input_data)
#      #Disply the result
#      if prediction[0]==1:
#         st.success("Congrats,This Environment is sustainable")
#      else:
#         st.info("It is not sustainable")

import streamlit as st
import joblib
import numpy as np

st.title("Check the Environment")

carbon_emission = st.number_input("Carbon emission Amount:", min_value=0.0)
energy_output = st.number_input("Energy Output Value:", min_value=0.0)
renewability_index = st.number_input("Renewability Index:", min_value=0.0)
cost_efficiency = st.number_input("Cost efficiency:", min_value=0.0)

# Load trained model
model = joblib.load("green_tech_model.pkl")

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

