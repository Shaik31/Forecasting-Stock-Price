import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
import model_building as m

# Set up the Streamlit app
st.markdown("# Reliance Stock Market Prediction")
user_input = st.multiselect('Please select the stock', ['RELIANCE'])
bt = st.button('Submit') 

# Check if the submit button is clicked
if bt:
    # Importing dataset
    data = pd.read_csv('Reliance_stock.csv')
    reliance = data.dropna().reset_index(drop=True)
    reliance['Date'] = pd.to_datetime(reliance['Date'], format='%Y-%m-%d')
    reliance = reliance.set_index('Date')
    df = reliance.copy()

    # Generate and display the model
    plotdf = m.create_model(df)
    df.reset_index(inplace=True)
    st.title('Reliance Stock Market Prediction')
    st.write(df)

    st.markdown("### Original vs predicted close price")
    fig = plt.figure(figsize=(20, 10))
    sns.lineplot(data=plotdf)
    st.pyplot(fig)

    # Forecast buttons
    st.write('Select the number of days to predict:')
    bt30 = st.button('30 Days')
    bt60 = st.button('60 Days')
    bt90 = st.button('90 Days')

    # Handle button clicks for forecast prediction
    if bt30:
        next_predicted_days_value30, plotdf30 = m.create_model(df, days=30)
        st.write('Forecast for 30 Days')
        df30 = pd.DataFrame(next_predicted_days_value30, columns=["Predicted Prices"])
        st.write(df30)

        st.markdown("Forecasted Price for 30 Days")
        fig = plt.figure(figsize=(20, 10))
        sns.lineplot(data=plotdf30)
        st.pyplot(fig)

    elif bt60:
        next_predicted_days_value60, plotdf60 = m.create_model(df, days=60)
        st.write('Forecast for 60 Days')
        df60 = pd.DataFrame(next_predicted_days_value60, columns=["Predicted Prices"])
        st.write(df60)

        st.markdown("Forecasted Price for 60 Days")
        fig = plt.figure(figsize=(20, 10))
        sns.lineplot(data=plotdf60)
        st.pyplot(fig)

    elif bt90:
        next_predicted_days_value90, plotdf90 = m.create_model(df, days=90)
        st.write('Forecast for 90 Days')
        df90 = pd.DataFrame(next_predicted_days_value90, columns=["Predicted Prices"])
        st.write(df90)

        st.markdown("Forecasted Price for 90 Days")
        fig = plt.figure(figsize=(20, 10))
        sns.lineplot(data=plotdf90)
        st.pyplot(fig)

else:
    st.write('Please click the submit button to get the EDA and Prediction.')
