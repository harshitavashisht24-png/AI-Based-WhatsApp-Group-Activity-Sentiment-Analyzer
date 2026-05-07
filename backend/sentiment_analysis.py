import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load cleaned chat data
df = pd.read_csv("output/clean_chat_data.csv")

# Function to analyze sentiment
def get_sentiment(message):

    analysis = TextBlob(str(message))

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"

    elif polarity < 0:
        return "Negative"

    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Clean_Message"].apply(get_sentiment)

# Count sentiments
sentiment_counts = df["Sentiment"].value_counts()

print("\nSENTIMENT ANALYSIS:")
print(sentiment_counts)

# Plot graph
plt.figure(figsize=(6,6))

sentiment_counts.plot(kind='pie', autopct='%1.1f%%')

plt.title("Sentiment Distribution")

plt.ylabel("")

# Save graph
plt.savefig("output/sentiment_analysis.png")

plt.close()
# Save updated CSV
df.to_csv("output/final_chat_data.csv", index=False)
print("Final CSV saved successfully!")