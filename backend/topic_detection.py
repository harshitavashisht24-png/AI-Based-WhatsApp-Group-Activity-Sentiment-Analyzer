import pandas as pd
from collections import Counter

# Load cleaned chat data
df = pd.read_csv("output/clean_chat_data.csv")

# Combine all cleaned messages
text = " ".join(df["Clean_Message"].dropna())

# Split into words
words = text.split()

# Remove small/common words
stop_words = [
    "the", "is", "and", "to", "in", "of",
    "for", "on", "at", "a", "an", "it",
    "this", "that", "i", "you", "we",
    "are", "was", "be", "with", "have"
]

filtered_words = [
    word for word in words
    if word not in stop_words and len(word) > 2
]

# Count word frequencies
word_counts = Counter(filtered_words)

# Get top topics
top_topics = word_counts.most_common(15)

print("\nTOP DISCUSSION TOPICS:\n")

for word, count in top_topics:
    print(f"{word} : {count}")