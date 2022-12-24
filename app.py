# Import libraries
import numpy as np
import pandas as pd
import streamlit as st
from pickle import load
from PIL import Image
from datetime import datetime

# Load necessary files
rf = load(open("random_forest.pkl","rb"))
image = Image.open("overhead-aerial-shot-beautiful-ocean-cliffs-water-splashing-them.jpg")

# Title
st.markdown("<h1 style='text-align: center;'>Prediksi Pasang Surut Ancol Jakarta</h1>",unsafe_allow_html=True)
st.image(image)
st.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;"/>""",unsafe_allow_html=True)

# Input time
st.header("Input Time")
current_time = datetime.now()

col1,col2 = st.columns(2)
with col1:
    year = st.number_input("Year",value=current_time.year)
    month = st.number_input("Month",value=current_time.month,min_value=1,max_value=12)
    day = st.number_input("Day",value=current_time.day,min_value=1,max_value=31)
with col2:
    hour = st.number_input("Hour",value=current_time.hour,min_value=0,max_value=23)
    minute = st.number_input("Minute",value=current_time.minute,min_value=0,max_value=59)

st.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;"/>""",unsafe_allow_html=True)

# Predict waterfall
st.header("Prediction")

input_time = [year,month,day,hour,minute]
pred = rf.predict(np.array([input_time]))[0]

new_date = [str(year)]
for i in [month,day,hour,minute]:
    if len(str(i)) == 1:
        i = f"0{i}"
        new_date.append(i)
    else:
        i = str(i)
        new_date.append(i)

if st.button("Click here to predict waterfall"):
    st.success(f"The predicted waterfall on {new_date[2]}-{new_date[1]}-{new_date[0]} at {new_date[3]}:{new_date[4]} is {round(pred,2)}")