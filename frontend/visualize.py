import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("output/clean_chat_data.csv")

# -----------------------------
# MOST ACTIVE USERS GRAPH
# -----------------------------

active_users = df["User"].value_counts().head(5)

plt.figure(figsize=(8,5))
active_users.plot(kind='bar')

plt.title("Top 5 Most Active Users")
plt.xlabel("Users")
plt.ylabel("Message Count")

plt.tight_layout()

# Save graph
plt.savefig("output/active_users.png")

plt.show()

# -----------------------------
# TOP WORDS GRAPH
# -----------------------------

all_words = " ".join(df["Clean_Message"].dropna())

word_list = all_words.split()

word_freq = pd.Series(word_list).value_counts().head(10)

plt.figure(figsize=(8,5))
word_freq.plot(kind='bar')

plt.title("Top 10 Most Common Words")
plt.xlabel("Words")
plt.ylabel("Frequency")

plt.tight_layout()

# Save graph
plt.savefig("output/top_words.png")

plt.show()

print("\nGraphs generated successfully!")