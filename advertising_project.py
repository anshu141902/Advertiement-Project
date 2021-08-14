# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 18:59:51 2021

@author: 91892
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import pickle
svc_model_pickle = pickle.load(open('svc_model_pickle', 'rb'))

st.title('Advertisement Click Prediction')
st.subheader('by Anshu')
st.markdown('----')
st.balloons()


Daily_Time_Spent_on_Site = int(st.number_input('Enter the Time you spent on site in seconds: '))

Age = int(st.number_input('Enter the Age: '))

Average_Area_Income = int(st.number_input('Enter the Average Area Income: '))

Daily_Internet_Usage = int(st.number_input('Enter the daily internet usage in mb: '))

Gender = int(st.slider('Gender_type: 1 = Male & 0 = Female', 0,1))

inputs=np.array([[Daily_Time_Spent_on_Site, Age, Average_Area_Income, Daily_Internet_Usage, Gender]])

def predict_Strokes(Daily_Time_Spent_on_Site, Age, Average_Area_Income, Daily_Internet_Usage, Gender):
                prediction=svc_model_pickle.predict(inputs)
                return prediction
            
if st.button("Prediction"):
    prediction = predict_Strokes(Daily_Time_Spent_on_Site, Age, Average_Area_Income, Daily_Internet_Usage, Gender)
    if prediction == 1:
                 st.success('Advertisement must be clicked')
    else:
                st.error('Advertisement will not clicked')