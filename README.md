
# 🚲 Bicycle Rental Dashboard

This repository contains a **Streamlit Dashboard** for analyzing bicycle rental data based on daily, hourly, and weather conditions. The dashboard provides insights into how various factors such as time, day, and weather impact the number of bicycle rentals.

## 📊 Project Overview

The dashboard is structured into multiple sections to give a comprehensive view of the data:

1. **Overview**: Provides an overview of the datasets, a quick data preview, and summary statistics.
2. **Daily Analysis**: Visualizes bicycle rental trends across different days and calculates the average rentals for each day of the week.
3. **Hourly Analysis**: Analyzes bicycle rentals for different hours of the day, showing both the average rentals and distribution of rentals by hour.
4. **Weather Analysis**: Examines the impact of various weather conditions on bicycle rentals, including scatter plots of rentals against temperature.

## 🚀 Features

- **Interactive Navigation**: Use the sidebar to switch between different sections and explore various analyses.
- **Data Visualizations**: Multiple charts including line plots, bar charts, and scatter plots using `matplotlib` and `seaborn`.
- **Responsive Design**: The dashboard is built with a wide layout, making it easy to view data on various screen sizes.

## 📂 Project Structure

The repository is organized as follows:

```
streamlit-bike-rental-dashboard/
│
├── dashboard.py                  # Main Streamlit dashboard script
├── requirements.txt              # Python dependencies for the project
├── dashboard/                    # Folder containing CSV data files
│   ├── day_clean.csv             # Daily bicycle rental data
│   ├── hour_clean.csv            # Hourly bicycle rental data
│
└── README.md                     # Project documentation (this file)
```

## 📦 Setup and Installation

To run the dashboard locally or deploy it on Streamlit Cloud, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/USERNAME/streamlit-bike-rental-dashboard.git
   cd streamlit-bike-rental-dashboard
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then, install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run dashboard.py
   ```

4. **View the dashboard**:
   Open your browser and go to `http://localhost:8501` to view the dashboard.

## 📊 Data Sources

The data used in this dashboard is divided into two datasets:

1. **Daily Data** (`day_clean.csv`): Contains daily bicycle rental counts along with weather and seasonal information.
2. **Hourly Data** (`hour_clean.csv`): Contains hourly bicycle rental counts with additional factors such as temperature and weather conditions.

## 🌟 Insights

Some key insights derived from the dashboard include:

- **Daily Trends**: Bicycle rentals peak on weekends, with lower rentals during weekdays.
- **Hourly Trends**: Most rentals occur during the morning and evening hours, coinciding with commuting times.
- **Weather Impact**: Clear weather results in higher rentals, while rainy and severe weather significantly reduce the number of rentals.

## 💡 Future Improvements

- Implement additional filtering options for users to interact with the data (e.g., filtering by month or year).
- Add predictive modeling to forecast bicycle rentals based on past trends and weather conditions.
- Improve visualizations by adding more interactive charts and maps.

## 🙋‍♂️ Author

- **Adrian Alfajri** - [GitHub](https://github.com/USERNAME) | [LinkedIn](https://www.linkedin.com/in/USERNAME/)

## 🔗 References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
