# -*- coding: utf-8 -*-
"""
Created on Mon May 30 03:48:08 2022

@author: Hasnain
"""

import pickle
import streamlit as st
#from streamlit_option_menu import option_menu


# loading the saved models

water_model = pickle.load(open('water_test_randomForest_Model.sav', 'rb'))






    
    # page title
st.title('Water Potability')
    
    
    # getting the input data from the user
col1, col2, col3 = st.columns(3)
    
with col1:
    ph = st.text_input('ph Level')
        
with col2:
    Hardness = st.text_input('Hardness')
    
with col3:
    Solids = st.text_input('Solids')
    
with col1:
    Chloramines = st.text_input('Chloramines')
    
with col2:
    Sulfate = st.text_input('Sulfate')
    
with col3:
    Conductivity = st.text_input('Conductivity')
    
with col1:
    Organic_carbon = st.text_input('Organic_carbon')
    
with col2:
    Trihalomethanes = st.text_input('Trihalomethanes')
    
with col3:
    Turbidity = st.text_input('Turbidity')
    
    # code for Prediction
waterPotability_diagnosis = ''
    
    # creating a button for Prediction
    
if st.button('Water Potability Test Result'):
    water_prediction = water_model.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])
        
    if (water_prediction[0] == 1):
        waterPotability_diagnosis = 'Water is consumable'
    else:
        waterPotability_diagnosis = 'Water is not consumable'
        
st.success(waterPotability_diagnosis)



