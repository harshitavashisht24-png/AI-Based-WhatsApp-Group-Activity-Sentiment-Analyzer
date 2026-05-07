import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("output/final_chat_data.csv")

# Page title
st.title("WhatsApp Chat Analyzer")

# Total messages
st.header("Total Messages")

st.write(df.shape[0])

# Most active users
st.header("Most Active Users")

active_users = df["User"].value_counts()

st.bar_chart(active_users.head(10))

# Sentiment Analysis
st.header("Sentiment Analysis")

sentiment_counts = df["Sentiment"].value_counts()

st.write(sentiment_counts)

# Display Word Cloud
st.header("Word Cloud")

st.image("output/wordcloud.png")

# Display Active Users Graph
st.header("Top Active Users Graph")

st.image("output/active_users.png")

# Display Sentiment Graph
st.header("Sentiment Graph")

st.image("output/sentiment_analysis.png")