import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
#import yfinance as yf
import datetime
import streamlit as st
import sys
import model_building as m
import pickle
import plotly
import plotly.express as px

st.markdown("# Reliance Stock Price Prediction")
user_input = st.multiselect('Please select the stock',['RELIANCE'])
bt = st.button('Submit') 

#adding a button
if bt:

# Importing dataset------------------------------------------------------
    #df = yf.download('RELIANCE.NS', start=START, end=END)
    data= pd.read_csv('Relaince_stock.csv')
    reliance_2=data.dropna().reset_index(drop=True)
    reliance=reliance_2.copy()
    reliance['Date']=pd.to_datetime(reliance['Date'],format='%Y-%m-%d')
    reliance=reliance.set_index('Date')
    df = reliance.copy()
    dfclose= pd.DataFrame(df.Close)
    dfclose = dfclose.reset_index(drop=True)
    
    plotdf,next_predicted_days_value30,next_predicted_days_value60,next_predicted_days_value90,plotdf30,plotdf60,plotdf90= m.create_model(df)
    df.reset_index(inplace = True)
    st.title('Reliance Stock Market Prediction')
    st.write(df)

    st.markdown("### Original vs predicted close price")
    fig = plt. figure(figsize=(20,10))
    sns.lineplot(data=plotdf)
    st.pyplot(fig)
    

    #30 days forecast
    st.write('Forecast')
    df30 = pd.DataFrame(next_predicted_days_value30)
    st.markdown("### Next 30 days forecast")
    df30.rename(columns={0: "Predicted Prices"}, inplace=True)
    st.write(df30)

    st.markdown("Forecasted Price for 30 Days")
    fig= figsize=(15,10)
    fig = px.line(plotdf30)
    st.plotly_chart(fig)


    fulldf30 = pd.concat([dfclose,plotdf30],axis=0,ignore_index=True)
    st.write('Original Close Price and Forecasted 30 days')
    fig = figsize=(15,10)
    fig = px.line(fulldf30, x=fulldf30.index, y=fulldf30.columns)
    st.plotly_chart(fig)


    #60 days forecast
    df60 = pd.DataFrame(next_predicted_days_value60)
    st.markdown("### Next 60 days forecast")
    df60.rename(columns={0: "Predicted Prices"}, inplace=True)
    st.write(df60)

    st.markdown("Forecasted Price for 60 Days")
    fig= figsize=(15,10)
    fig = px.line(plotdf60)
    st.plotly_chart(fig)
    
    fulldf60 = pd.concat([dfclose,plotdf60],axis=0,ignore_index=True)
    st.write('Original Close Price and Forecasted 60 days')
    fig = figsize=(15,10)
    fig = px.line(fulldf60, x=fulldf60.index, y=fulldf60.columns)
    st.plotly_chart(fig)


    #90 days forecast
    df90 = pd.DataFrame(next_predicted_days_value90)
    st.markdown("### Next 90 days forecast")
    df90.rename(columns={0: "Predicted Prices"}, inplace=True)
    st.write(df90)

    st.markdown("Forecasted Price for 90 Days")
    fig= figsize=(15,10)
    fig = px.line(plotdf90)
    st.plotly_chart(fig)

    fulldf90 = pd.concat([dfclose,plotdf90],axis=0,ignore_index=True)
    st.write('Original Close Price and Forecasted 60 days')
    fig = figsize=(15,10)
    fig = px.line(fulldf90, x=fulldf90.index, y=fulldf90.columns)
    st.plotly_chart(fig)
    


else:
    #displayed when the button is unclicked
     st.write('Please click on the submit button to get the Data and Forecasting')
