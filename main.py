import streamlit as st
import plotly.express as px
import sys
import os


st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the "
                                                                 "number of "
                                                                 "Days")
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-25-11", "2022-26-11", "2022-27-11"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
