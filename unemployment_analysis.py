import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import requests

# URL for Unemployment in India dataset
url = "https://raw.githubusercontent.com/amankharwal/Website-data/master/unemployment.csv"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    # Fetching data
    response = requests.get(url, headers=headers)
    df = pd.read_csv(io.StringIO(response.text))
    
    # Cleaning column names
    df.columns = df.columns.str.strip()
    
    # Task Requirement: Exploratory Data Analysis (EDA)
    print("Average Unemployment Rate by Region:")
    print(df.groupby('Region')['Estimated Unemployment Rate (%)'].mean())

    # Visualization 1: Line Plot (Trends over time)
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
    plt.title('Unemployment Rate Analysis by Region')
    plt.legend(bbox_to_anchor=(1, 1))
    plt.xticks(rotation=45)
    plt.show()

    # Visualization 2: Bar Plot (Region impact)
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x='Region', y='Estimated Unemployment Rate (%)')
    plt.title('Regional Average Unemployment Rate')
    plt.xticks(rotation=90)
    plt.show()

except Exception as e:
    print(f"Error: {e}")