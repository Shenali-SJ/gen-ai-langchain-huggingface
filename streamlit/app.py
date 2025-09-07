import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Toothless!!")

st.write("My toothless is my toothless")

## 1. Create a dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

## 2. Create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['black', 'white', 'yellow']
)

st.line_chart(chart_data) 

## uses streamlit to show the pandas 
