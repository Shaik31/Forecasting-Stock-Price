
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
#import yfinance as yf
import datetime
import streamlit as st
import sys
import model_building as m
import pickle


st.markdown("# Reliance Stock Market Prediction")
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
    plotdf,future_predicted_values,plotdfnew =m.create_model(df)
    df.reset_index(inplace = True)
    st.title('Reliance Stock Market Prediction')
    st.write(df)

    st.markdown("### Original vs predicted close price")
    fig= plt.figure(figsize=(20,10))
    sns.lineplot(data=plotdf)
    st.pyplot(fig)
    
    st.write('select the days to predict')
    bt30 = st.button('30 Days')
    bt60 = st.button('60 Days')
    bt90 = st.button('90 Days')

    if bt30:
         st.write('Forecast')
         df1 = pd.DataFrame(future_predicted_values)
         st.markdown("### Next 30 days forecast")
         df1.rename(columns={0: "Predicted Prices"}, inplace=True)
         st.write(df1)

         st.markdown("Forecasted Price for 30 Days")
         fig= plt.figure(figsize=(20,10))
         sns.lineplot(data=plotdfnew)
         st.pyplot(fig)
    
   
    else:
         st.write('Please select days to predict')



else:
    #displayed when the button is unclicked
 st.write('Please click on the submit button to get the EDA ans Prediction') 
