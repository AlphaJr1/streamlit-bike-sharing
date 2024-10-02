import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Customizing the page and sidebar
st.set_page_config(page_title="Bicycle Rental Dashboard", page_icon="🚲", layout="wide")

# Sidebar for Navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select an analysis view:", ["Overview", "Daily Analysis", "Hourly Analysis", "Weather Analysis"])

# Load Data
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load datasets
day_data = load_data('dashboard/day_clean.csv')
hour_data = load_data('dashboard/hour_clean.csv')

# Overview Section
if option == "Overview":
    st.title("🚲 Bicycle Rental Dashboard - Overview")
    st.markdown("### This dashboard provides insights into bicycle rentals with data analysis based on daily, hourly, and weather conditions.")

    st.markdown("#### Data Preview")
    st.write("**Daily Data Sample**")
    st.dataframe(day_data.head(5))

    st.write("**Hourly Data Sample**")
    st.dataframe(hour_data.head(5))

    # Display Summary Statistics
    st.markdown("#### Summary Statistics")
    daily_stats = day_data.describe()
    hourly_stats = hour_data.describe()
    st.write("**Daily Data Summary**")
    st.dataframe(daily_stats)
    st.write("**Hourly Data Summary**")
    st.dataframe(hourly_stats)

# Daily Analysis Section
elif option == "Daily Analysis":
    st.title("📅 Daily Analysis of Bicycle Rentals")
    st.markdown("#### Analyzing the total bicycle rentals across different days.")

    # Daily Rentals Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(day_data['date'], day_data['total_rentals'], marker='o', linestyle='-', color='b', label='Total Rentals')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Rentals')
    ax.set_title('Total Bicycle Rentals by Day')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(fig)

    # Weekly Rentals Average
    day_data['weekday'] = pd.to_datetime(day_data['date']).dt.day_name()
    weekly_avg = day_data.groupby('weekday')['total_rentals'].mean().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    st.markdown("#### Average Bicycle Rentals by Day of the Week")
    st.bar_chart(weekly_avg)

# Hourly Analysis Section
elif option == "Hourly Analysis":
    st.title("⏰ Hourly Analysis of Bicycle Rentals")
    st.markdown("#### Analyzing the hourly bicycle rental trends.")

    # Average Rentals by Hour Plot
    hourly_avg = hour_data.groupby('hour')['total_rentals'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='hour', y='total_rentals', data=hourly_avg, marker='o', color='g', ax=ax)
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Average Rentals')
    ax.set_title('Average Bicycle Rentals by Hour of the Day')
    st.pyplot(fig)

    # Distribution of Rentals by Hour
    st.markdown("#### Distribution of Rentals by Hour")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(hour_data['hour'], bins=24, kde=True, color='orange', ax=ax)
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Frequency of Rentals')
    ax.set_title('Distribution of Rentals Across Hours of the Day')
    st.pyplot(fig)

# Weather Analysis Section
elif option == "Weather Analysis":
    st.title("☀️🌧️ Weather Analysis of Bicycle Rentals")
    st.markdown("#### Analyzing the impact of weather conditions on bicycle rentals.")

    # Group by Weather Conditions
    weather_summary = day_data.groupby('weather_situation')['total_rentals'].mean().reset_index()
    weather_summary['Weather'] = weather_summary['weather_situation'].map({1: 'Clear', 2: 'Cloudy', 3: 'Rainy', 4: 'Severe Weather'})
    st.markdown("#### Average Rentals by Weather Condition")
    st.bar_chart(weather_summary, x='Weather', y='total_rentals')

    # Rentals by Temperature
    st.markdown("#### Rentals by Temperature")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x='temperature', y='total_rentals', data=day_data, ax=ax, hue='weather_situation', palette='coolwarm', s=100)
    ax.set_xlabel('Temperature (Normalized)')
    ax.set_ylabel('Total Rentals')
    ax.set_title('Scatter Plot of Rentals by Temperature')
    plt.legend(title='Weather Condition', labels=['Clear', 'Cloudy', 'Rainy', 'Severe Weather'])
    st.pyplot(fig)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Created by Adrian Alfajri")