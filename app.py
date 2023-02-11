import streamlit as st
import pandas as pd

df = pd.dataframe({'col1': 1, 'col2':2})


st.head('hello')
st.dataframe(df)