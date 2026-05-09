def generate_ai_summary(df):

    total_messages = len(df)

    top_user = (
        df["User"]
        .value_counts()
        .idxmax()
    )

    top_topic = (
        df["Topic"]
        .value_counts()
        .idxmax()
    )

    top_emotion = (
        df["Emotion"]
        .value_counts()
        .idxmax()
    )

    summary = f"""
AI GROUP SUMMARY

Total Messages: {total_messages}

Most Active User: {top_user}

Most Discussed Topic ID: {top_topic}

Dominant Emotion: {top_emotion}

The AI system detected conversational patterns,
group narratives, and user interaction clusters.
"""

    with open(
        "output/ai_summary.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(summary)

    return summary