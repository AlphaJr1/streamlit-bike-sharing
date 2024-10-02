
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and Introduction
st.title("Data Analysis Project: Bicycle Rentals")
st.markdown("**Created by Adrian Alfajri**")
st.markdown("This dashboard presents an analysis of bicycle rentals based on daily and hourly trends, considering weather and other conditions.")

# Load the datasets
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Load day_clean.csv and hour_clean.csv
day_data = load_data('./dashboard/day_clean.csv')
hour_data = load_data('./dashboard/hour_clean.csv')

# Display data preview
st.subheader("Daily Data Preview")
st.dataframe(day_data.head())

st.subheader("Hourly Data Preview")
st.dataframe(hour_data.head())

# Plot Daily Rentals
st.subheader("Daily Rentals Analysis")
fig1, ax1 = plt.subplots()
ax1.plot(day_data['date'], day_data['total_rentals'], marker='o', linestyle='-', color='b')
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Rentals')
ax1.set_title('Total Rentals by Day')
plt.xticks(rotation=45)
st.pyplot(fig1)

# Plot Hourly Rentals by Time of Day
st.subheader("Hourly Rentals Analysis")
hourly_avg = hour_data.groupby('hour')['total_rentals'].mean().reset_index()
fig2, ax2 = plt.subplots()
ax2.plot(hourly_avg['hour'], hourly_avg['total_rentals'], marker='o', linestyle='-', color='g')
ax2.set_xlabel('Hour of the Day')
ax2.set_ylabel('Average Rentals')
ax2.set_title('Average Rentals by Hour of Day')
st.pyplot(fig2)

# Display rental trends by weather condition
st.subheader("Rental Trends by Weather Condition")
weather_summary = day_data.groupby('weather_situation')['total_rentals'].mean().reset_index()
st.bar_chart(weather_summary, x='weather_situation', y='total_rentals')

# Conclusion
st.markdown("**Conclusion**: This dashboard provides an overview of bicycle rental trends based on day and hour data. You can explore further by filtering specific time frames and weather conditions.")
