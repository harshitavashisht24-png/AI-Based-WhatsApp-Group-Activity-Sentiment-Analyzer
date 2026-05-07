import pandas as pd
from collections import Counter

# Load chat data
df = pd.read_csv("output/chat_data.csv")

# Store interactions
interaction_pairs = []

# Loop through messages
for i in range(len(df) - 1):

    current_user = df.loc[i, "User"]
    next_user = df.loc[i + 1, "User"]

    # Ignore self replies
    if current_user != next_user:

        pair = (current_user, next_user)

        interaction_pairs.append(pair)

# Count interactions
interaction_counts = Counter(interaction_pairs)

# Top 10 interactions
top_interactions = interaction_counts.most_common(10)

print("\nTOP USER INTERACTIONS:\n")

for pair, count in top_interactions:
    print(f"{pair[0]} → {pair[1]} : {count} times")