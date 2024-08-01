import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
import model_building as m

# Set up the Streamlit app
st.markdown("# Reliance Stock Market Prediction")

# Initialize session state for tracking buttons
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False
if 'forecast_days' not in st.session_state:
    st.session_state.forecast_days = None

# Function to handle button clicks and update session state
def handle_forecast_button(days):
    st.session_state.forecast_days = days

user_input = st.multiselect('Please select the stock', ['RELIANCE'])
bt = st.button('Submit')

# Load data and create the model if the Submit button is clicked
if st.button('Submit'):
    # Importing dataset
    data = pd.read_csv('Relaince_stock.csv')
    reliance = data.dropna().reset_index(drop=True)
    reliance['Date'] = pd.to_datetime(reliance['Date'], format='%Y-%m-%d')
    reliance = reliance.set_index('Date')
    df = reliance.copy()

    # Generate and display the model
    plotdf,next_predicted_days_value30,next_predicted_days_value60,next_predicted_days_value90,plotdf30,plotdf60,plotdf90 = m.create_model(df)
    df.reset_index(inplace=True)
    st.session_state.data_loaded = True

    # Display the data and initial plot
    st.title('Reliance Stock Market Prediction')
    st.write(df)

    st.markdown("### Original vs predicted close price")
    fig = plt.figure(figsize=(20, 10))
    sns.lineplot(data=plotdf)
    st.pyplot(fig)

# Display forecast buttons if data is loaded
if st.session_state.data_loaded:
    st.write('Select the number of days to predict:')
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button('30 Days'):
            handle_forecast_button(30)
            st.session_state.forecast_days = 30

    with col2:
        if st.button('60 Days'):
            handle_forecast_button(60)
            st.session_state.forecast_days = 60

    with col3:
        if st.button('90 Days'):
            handle_forecast_button(90)
            st.session_state.forecast_days = 90

    # Display forecast based on session state
    if st.session_state.forecast_days:
        days = st.session_state.forecast_days
        next_predicted_days_value, plotdf = m.create_model(df, days=days)
        st.write(f'Forecast for {days} Days')
        df_forecast = pd.DataFrame(next_predicted_days_value, columns=["Predicted Prices"])
        st.write(df_forecast)

        st.markdown(f"Forecasted Price for {days} Days")
        fig = plt.figure(figsize=(20, 10))
        sns.lineplot(data=plotdf)
        st.pyplot(fig)

else:
    st.write('Please click the submit button to get the EDA and Prediction.')
