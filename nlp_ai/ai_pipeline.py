import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import pandas as pd

from nlp_ai.advanced_sentiment import (
    analyze_advanced_sentiment
)

from nlp_ai.emotion_detection import (
    detect_emotions
)

from nlp_ai.semantic_topic_modeling import (
    detect_semantic_topics
)

from nlp_ai.narrative_detection import (
    detect_narratives
)

from nlp_ai.community_detection import (
    detect_communities
)

from nlp_ai.ai_summary import (
    generate_ai_summary
)

print("Loading Data...")

df = pd.read_csv(
    "output/clean_chat_data.csv"
)

print("Running Advanced Sentiment...")
df = analyze_advanced_sentiment(df)

print("Running Emotion Detection...")
df = detect_emotions(df)

print("Running Semantic Topic Modeling...")
df, topic_info = detect_semantic_topics(df)

print("Running Narrative Detection...")
narrative_df = detect_narratives(df)

print("Running Community Detection...")
communities = detect_communities(df)

print("Generating AI Summary...")
summary = generate_ai_summary(df)

print(summary)

# Save outputs
df.to_csv(
    "output/final_ai_chat_data.csv",
    index=False
)

topic_info.to_csv(
    "output/topic_info.csv",
    index=False
)

narrative_df.to_csv(
    "output/narratives.csv",
    index=False
)

print("AI NLP PIPELINE COMPLETED SUCCESSFULLY!")