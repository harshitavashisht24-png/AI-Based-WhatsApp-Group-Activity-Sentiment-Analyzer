from nlp_ai.hinglish_normalizer import normalize_hinglish
import pandas as pd
import re

# Load CSV file
df = pd.read_csv("output/chat_data.csv")

# Function to clean messages
def clean_message(message):
    
    # Convert to string
    message = str(message)

    # Remove links
    message = re.sub(r'http\S+', '', message)

    # Remove special characters
    message = re.sub(r'[^A-Za-z0-9\s]', '', message)

    # Convert to lowercase
    message = message.lower()
    message = normalize_hinglish(message)

    # Remove extra spaces
    message = message.strip()

    return message

# Apply cleaning function
df["Clean_Message"] = df["Message"].apply(clean_message)

# Save cleaned data
df.to_csv("output/clean_chat_data.csv", index=False)

print(df.head())

print("\nData cleaned successfully!")