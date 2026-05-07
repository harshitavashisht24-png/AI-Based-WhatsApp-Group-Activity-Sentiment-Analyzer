import re
import pandas as pd

# Open WhatsApp chat file
with open("data/sample_chat.txt", "r", encoding="utf-8") as file:
    chat_data = file.readlines()

# Empty list to store extracted messages
messages = []

# Regex pattern for WhatsApp messages
pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}\s?[ap]m)\s-\s(.*?):\s(.*)"

# Extract data from each line
for line in chat_data:
    match = re.match(pattern, line)

    if match:
        date = match.group(1)
        time = match.group(2)
        user = match.group(3)
        message = match.group(4)

        messages.append([date, time, user, message])

# Create DataFrame
df = pd.DataFrame(messages, columns=["Date", "Time", "User", "Message"])

# Print first 5 rows
print(df.head())

# Save CSV file
df.to_csv("output/chat_data.csv", index=False)

print("\nChat data saved successfully!")