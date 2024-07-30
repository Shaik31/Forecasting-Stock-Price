
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
    user_input = st.multiselect('Please select the stock',['RELIANCE'])

    # user_input = st.text_input('Enter Stock Name', "ADANIENT.NS")
    #st.markdown("### Choose Date for your anaylsis")
    #START = st.date_input("From",datetime.date(2015, 1, 1))
    #END = st.date_input("To",datetime.date(2023, 2, 28))
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
    plotdf, future_predicted_values =m.create_model(df)
    df.reset_index(inplace = True)
    st.title('Reliance Stock Market Prediction')
    st.write(df)

    st.title('Original Close Price vs Date')
    plt.plot(df['Close'],label='Original Data')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    st.pyplot()


   
    st.markdown("### Original vs predicted close price")
    fig= plt.figure(figsize=(20,10))
    sns.lineplot(data=plotdf)
    st.pyplot(fig)
    

    st.write('Forecast')
    df1 = pd.DataFrame(future_predicted_values)
    st.markdown("### Next 30 days forecast")
    df1.rename(columns={0: "Predicted Prices"}, inplace=True)
    st.write(df1)


    

else:
    #displayed when the button is unclicked
 st.write('Please click on the submit button to get the EDA ans Prediction') 
