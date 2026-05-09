import pandas as pd

def detect_narratives(df):

    narratives = []

    users = df["User"].unique()

    for user in users:

        user_df = df[df["User"] == user]

        dominant_topic = (
            user_df["Topic"]
            .value_counts()
            .idxmax()
        )

        dominant_sentiment = (
            user_df["Advanced_Sentiment"]
            .value_counts()
            .idxmax()
        )

        narratives.append({
            "User": user,
            "Dominant_Topic": dominant_topic,
            "Dominant_Sentiment": dominant_sentiment
        })

    narrative_df = pd.DataFrame(narratives)

    return narrative_df