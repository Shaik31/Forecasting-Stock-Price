
'''import pandas as pd
import pickle
#import seaborn as sns
#import matplotlib.pyplot as plt
import streamlit as st


model = pickle.load(open('lstm_model.pkl','rb'))

st.title('Relaince Stock Price Prediction')
user_input = st.multiselect('Please select the stock',['RELIANCE'])
bt = st.button('Submit') 

if bt:
    st.subheader("Raw Data")
    df = pd.read_csv('C:/Users/Admin/Relaince_stock.csv')
    st.dataframe(df)
    st.subheader("plotting the data")
    st.pyplot(df['Date'],df['Close'])'''


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
#import yfinance as yf
import datetime
import streamlit as st
import sys
import model_building as m
import pickle


with st.sidebar:
    st.markdown("# Reliance Stock Market Prediction")
    user_input = st.multiselect('Please select the stock',['RELIANCE.NS'],['RELIANCE.NS'])

    # user_input = st.text_input('Enter Stock Name', "ADANIENT.NS")
    #st.markdown("### Choose Date for your anaylsis")
    #START = st.date_input("From",datetime.date(2015, 1, 1))
    #END = st.date_input("To",datetime.date(2023, 2, 28))
    bt = st.button('Submit') 

#adding a button
if bt:

# Importing dataset------------------------------------------------------
    #df = yf.download('RELIANCE.NS', start=START, end=END)
    df = pd.read_csv('Relaince_stock.csv')
    plotdf, future_predicted_values =m.create_model(df)
    df.reset_index(inplace = True)
    st.title('Reliance Stock Market Prediction')
    st.header("Data We collected from the source")
    st.write(df)

    reliance_1=df.drop([["Adj Close","Open","High","Volume","Low"]],axis=1).reset_index(drop=True)
    reliance_2=reliance_1.dropna().reset_index(drop=True)

    reliance=reliance_2.copy()
    reliance['Date']=pd.to_datetime(reliance['Date'],format='%Y-%m-%d')
    reliance=reliance.set_index('Date')
    st.title('EDA')

    
    st.write(reliance)
    df1 = pd.DataFrame(future_predicted_values)
    st.markdown("### Next 30 days forecast")
    df1.rename(columns={0: "Predicted Prices"}, inplace=True)
    st.write(df1)

    

    st.markdown("### Original vs predicted close price")
    fig= plt.figure(figsize=(20,10))
    sns.lineplot(data=plotdf)
    st.pyplot(fig)
else:
    #displayed when the button is unclicked
 st.write('Please click on the submit button to get the EDA ans Prediction') 
