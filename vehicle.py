# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:52:22 2022

@author: User
"""

import pandas as pd
import streamlit as st
import pickle

filename = "vehicle.sav"
model = pickle.load(open(filename, "rb"))

st.title("Vehicle Price Prediction App")
st.subheader("This app takes in certain variables to enable the prediction of the price of vehicles")

def userInput():
    Kilometer = st.text_input("What is the distance travelled in Kilometers by the vehicle?", 5000 , 105000)
    Location = st.text_input("What is the location of the vehicle?", 0, 3)
    Maker = st.text_input("Who is the maker of the vehicle?", 0, 50)
    Colour = st.text_input("What is the colour of the vehicle?", 0, 20)
    Type = st.text_input("What type is your vehicle?", 0, 3)
    Year = st.text_input("What year was your vehicle made?", 0, 30)
    
    #'''
    #Kilometer = st.slider("What is the distance travelled in Kilometers by the vehicle?", 5000 , 105000)
    #Location = st.slider("What is the location of the vehicle?", 0, 3)
    #Maker = st.slider("Who is the maker of the vehicle?", 0, 50)
    #Colour = st.slider("What is the colour of the vehicle?", 0, 20)
    #Type = st.slider("What type is your vehicle?", 0, 3)
    #Year = st.slider("What year was your vehicle made?", 0, 30)
#'''
    
    data = {
        "Distance_Km" : Kilometer,
        "Location_cat": Location,
        "Maker_cat": Maker,
        "Colour_cat": Colour,
        "Type_cat": Type,
        "Year_cat": Year
        }
    
    features = pd.DataFrame(data, index = [0])
    return features


Dinput = userInput()

def prediction():
    predict = model.predict(Dinput)
    result = ""
    if predict == 0:
        result = "Not Qualified"
    else:
        result = f"Qualified{predict}"
    return result
#'''


if st.button("Predict"):
#    result = model.predict(Dinput)prediction
      result = prediction()
      st.success(f"Thank you for filling this form. Your car is {result}")

