import pandas as pd
from textblob import TextBlob

# We wrap the logic so the Dashboard can call it
def get_sentiment(message):
    analysis = TextBlob(str(message))
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def analyze_all_sentiments(df):
    # Member 2 used a column called 'Clean_Message'
    # If that doesn't exist yet, we'll use the 'Message' column
    column_to_use = "Clean_Message" if "Clean_Message" in df.columns else "Message"
    
    df["Sentiment"] = df[column_to_use].apply(get_sentiment)
    return df