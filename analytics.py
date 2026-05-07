import pandas as pd

# Load cleaned chat data
df = pd.read_csv("output/clean_chat_data.csv")

# Total messages
total_messages = df.shape[0]

print("\nTOTAL MESSAGES:")
print(total_messages)

# Most active users
print("\nMOST ACTIVE USERS:")
active_users = df["User"].value_counts()

print(active_users)

# Top 10 most common words
all_words = " ".join(df["Clean_Message"].dropna())

word_list = all_words.split()

word_freq = pd.Series(word_list).value_counts().head(10)

print("\nTOP 10 MOST COMMON WORDS:")
print(word_freq)