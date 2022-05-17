# import libraries
from email.policy import default
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import nsepy
import streamlit as st

st.title("Stock Trend Prediction")

# import data of User mentioned stock
stock_name = st.text_input("Enter Stock Ticker", 'TATAMOTORS') 
start_date = st.date_input('Enter Start Date', date(2018,1,1))
end_date = st.date_input('Enter End Date', date.today())

data = nsepy.get_history(
    stock_name, start=start_date, end=end_date)

# Get Years of start date and end date
start_year = start_date.year
end_year = end_date.year

# Describing Data
st.subheader('Data from '+str(start_year)+'-'+str(end_year))
st.write(data.describe())

# Visualizations
st.subheader('Closing Pice vs Time Chart')

fig = plt.figure(figsize=[15,6])
plt.plot(data['Close'], label=stock_name + ' stocks price')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Price')
plt.title(stock_name, fontsize=16)

st.pyplot(fig) # show the fig in the app

# Moving Average plots
st.subheader('Closing price vs Time Chart with Moving Average')
window_size = st.slider(label='Window Size', min_value=10, max_value=100)

y_pred_ma = data['Close'].rolling(window_size).mean()

# plot
fig2 = plt.figure(figsize=[15,6])
plt.plot(data['Close'], label=stock_name+' stocks price')
plt.plot(y_pred_ma, label='Moving average of '+stock_name, color='r')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title(stock_name, fontsize=16)
st.pyplot(fig2)