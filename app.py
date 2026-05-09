import streamlit as st
import pandas as pd

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI WhatsApp Analyzer",
    layout="wide"
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = pd.read_csv("output/final_chat_data.csv")

ai_df = pd.read_csv(
    "output/final_ai_chat_data.csv"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title(
    "AI-Powered WhatsApp Behavioral Intelligence Dashboard"
)

st.markdown("""
This system uses AI and NLP techniques to analyze WhatsApp group behavior, conversational narratives, semantic topics, sentiments, emotions, and interaction communities.
""")

st.divider()

# -----------------------------------
# BASIC ANALYTICS
# -----------------------------------

st.header("Basic Group Analytics")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        label="Total Messages",
        value=df.shape[0]
    )

with col2:

    st.metric(
        label="Unique Users",
        value=df["User"].nunique()
    )

# -----------------------------------
# MOST ACTIVE USERS
# -----------------------------------

st.header("Most Active Users")

active_users = (
    df["User"]
    .value_counts()
)

st.bar_chart(
    active_users.head(10)
)

# -----------------------------------
# BASIC SENTIMENT ANALYSIS
# -----------------------------------

st.header("Basic Sentiment Analysis")

sentiment_counts = (
    df["Sentiment"]
    .value_counts()
)

st.bar_chart(sentiment_counts)

# -----------------------------------
# ADVANCED AI SENTIMENT
# -----------------------------------

st.header("Advanced AI Sentiment Analysis")

advanced_sentiments = (
    ai_df["Advanced_Sentiment"]
    .value_counts()
)

st.bar_chart(advanced_sentiments)

# -----------------------------------
# EMOTION ANALYSIS
# -----------------------------------

st.header("Emotion Detection")

emotion_counts = (
    ai_df["Emotion"]
    .value_counts()
)

st.bar_chart(emotion_counts)

# -----------------------------------
# WORD CLOUD
# -----------------------------------

st.header("Word Cloud")

st.image("output/wordcloud.png")

# -----------------------------------
# ACTIVE USERS GRAPH
# -----------------------------------

st.header("Top Active Users Graph")

st.image("output/active_users.png")

# -----------------------------------
# SENTIMENT GRAPH
# -----------------------------------

st.header("Sentiment Graph")

st.image("output/sentiment_analysis.png")

# -----------------------------------
# SEMANTIC TOPIC MODELING
# -----------------------------------

st.header("Semantic Topic Modeling")

topic_df = pd.read_csv(
    "output/topic_info.csv"
)

st.dataframe(topic_df)

# -----------------------------------
# NARRATIVE DETECTION
# -----------------------------------

st.header("Narrative Detection")

narrative_df = pd.read_csv(
    "output/narratives.csv"
)

st.dataframe(narrative_df)

# -----------------------------------
# COMMUNITY DETECTION
# -----------------------------------

st.header("Community Detection")

community_df = pd.read_csv(
    "output/communities.csv"
)

st.dataframe(community_df)

# -----------------------------------
# AI GENERATED SUMMARY
# -----------------------------------

st.header("AI Generated Summary")

with open(
    "output/ai_summary.txt",
    "r",
    encoding="utf-8"
) as f:

    summary = f.read()

st.success(summary)

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.markdown("""
### Project Features

- AI-Based Sentiment Analysis
- Emotion Detection
- Semantic Topic Modeling
- Narrative Detection
- Community Detection
- Hinglish Text Understanding
- WhatsApp Behavioral Intelligence

### Technologies Used

- Python
- Streamlit
- NLP
- Transformers
- Machine Learning
- Pandas
""")