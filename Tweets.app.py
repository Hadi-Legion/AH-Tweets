import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Set up Streamlit page
st.set_page_config(page_title="Airline Tweet Sentiment Analysis", layout="centered")

st.title("✈️ Airline Tweet Sentiment Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/Hadi-Legion/AH-Tweets/refs/heads/main/Tweets.csv')

tweets = load_data()

st.subheader("Sample of Tweets Data")
st.dataframe(tweets.head())

# Pie Chart: Sentiment Distribution
sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['sentiment', 'count']

st.subheader("Sentiment Distribution of Tweets")
fig_pie = px.pie(sentiment_counts, values='count', names='sentiment', title='Count of Tweets by Sentiment')
st.plotly_chart(fig_pie)

# Bar Chart: Tweet counts by airline using Seaborn
airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

st.subheader("Tweet Counts by Airline")
fig_bar, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='airline', y='count', data=airline_counts, hue='airline', palette='viridis', legend=False, ax=ax)

ax.set_title('Tweet Counts by Airlines')
ax.set_xlabel('Airline')
ax.set_ylabel('Count')

st.pyplot(fig_bar)
