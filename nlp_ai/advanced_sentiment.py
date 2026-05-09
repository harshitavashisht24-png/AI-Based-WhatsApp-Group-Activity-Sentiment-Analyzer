import os

# Disable TensorFlow completely
os.environ["USE_TF"] = "0"

from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-xlm-roberta-base-sentiment",
    framework="pt"
)

def analyze_advanced_sentiment(df):

    sentiments = []

    for text in df["Clean_Message"]:

        try:

            result = sentiment_pipeline(
                str(text[:512])
            )[0]

            sentiments.append(
                result["label"]
            )

        except Exception as e:

            print("Sentiment Error:", e)

            sentiments.append("neutral")

    df["Advanced_Sentiment"] = sentiments

    return df