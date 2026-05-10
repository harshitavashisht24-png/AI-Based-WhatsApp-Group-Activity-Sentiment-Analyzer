from textblob import TextBlob
import pandas as pd

def analyze_all_sentiments(df):

    sentiments = []

    for msg in df["Message"]:

        polarity = TextBlob(str(msg)).sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"

        elif polarity < 0:
            sentiment = "Negative"

        else:
            sentiment = "Neutral"

        sentiments.append(sentiment)

    df["Sentiment"] = sentiments

    return df