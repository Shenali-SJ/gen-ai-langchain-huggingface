import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt

## Text Inputs

st.write("Let's get to know you !!")
name=st.text_input("Enter your name")

if name:
    st.write("Hello there " + name)

## Slider Input - only for numbers

birthYear=st.slider("When were you born?", 1900, 2025, 1984)

generation=st.select_slider( ## this is a slider with options - discrete values
    "What generation do you belong to?",
    options=['Gen Z', 'Millenial', 'Gen X', 'Boomer', 'Silent']
)

if birthYear:
    age=dt.datetime.now().year - birthYear
    if name:
        st.write(name + ", you are " + str(age) + " years old")

## Select Box

favColor=st.selectbox("What's your favorite color?", ["Blue", "Red", "Black"], accept_new_options=True)
if favColor:
    if name:
        st.write(name + ", your favorite color is " + favColor)
    if favColor=="Black":
        st.write("You have great taste in colors " + name)


## Upload file
files=st.file_uploader("Upload your CSV", type=["csv"])




