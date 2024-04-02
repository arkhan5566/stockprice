import streamlit as st
import yfinance as yf
import streamlit.components.v1 as com
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import datetime
from datetime import date,timedelta
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
st.set_page_config(page_title="Stock Price",layout="wide",page_icon="icon.jpg",)

com.html("""
<H1> Stock Price Prediction using Machine Learning</H1>
         <div class="khansb">
Welcome to our Stock Price Prediction website, where we utilize advanced machine learning techniques to provide accurate and insightful forecasts for stock prices. In an ever-changing and volatile market, staying ahead of the curve is crucial for investors, traders, and financial professionals. Our platform aims to empower users with reliable predictions, enabling informed decision-making and potentially maximizing return  
       <a href="http://google.com">khansb</a>
            </div>
<style>
         
      html
         {
         margin: auto;
         overflow: auto;
    background: linear-gradient( #2d3f4b 38%, #caabab 68%);
         background-attachment: fixed;
          background-size: 400% 400%;
         color:black;
         font-size: large;
               }
H1{
         text-align: center;
}
         </style>
""")
st.image("icon.jpg")
with open('wave.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.sidebar.header('Choose Date from below')
start_date=st.sidebar.date_input('Start date',date (2023,1,1))
end_date=st.sidebar.date_input('End date',date (2024,1,1))
ticker_list= ["AAPL","BWCL"]
ticker=st.sidebar.selectbox('Select the Company',ticker_list)
data = pd.read_csv("python.csv")
st.write('data from',start_date,'to',end_date)
if  ticker == "AAPL":
   st.write(data)

data2 = pd.read_csv("python2.csv")
if  ticker == "BWCL":
   st.write(data2)
com.html(
   """
<h2>Graphical View</h2>
<style>
html{
margin: auto;
         overflow: auto;
    background: linear-gradient( #2d3f4b 38%, #caabab 68%);
         background-attachment: fixed;
          background-size: 400% 400%;
         color:black;
         font-size: large;
         text-align: center;
}

"""
)
if  ticker == "AAPL":
   fig = px.line(data,x='Date',y='Close',title='closing price of the stock')
   st.plotly_chart(fig)
if  ticker == "BWCL":
   fig2 = px.line(data2,x='Date',y='Close',title='closing price of the stock')
   st.plotly_chart(fig2)
