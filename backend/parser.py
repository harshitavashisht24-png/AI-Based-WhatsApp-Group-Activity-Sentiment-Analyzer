import re
import pandas as pd

def parse_chat_data(chat_input):

    # Handle uploaded file
    if hasattr(chat_input, "read"):
        text = chat_input.read().decode("utf-8")

    # Handle direct chat text
    elif isinstance(chat_input, str):

        # If it's a file path
        if ".txt" in chat_input:
            with open(chat_input, "r", encoding="utf-8") as f:
                text = f.read()

        # Otherwise raw chat content
        else:
            text = chat_input

    else:
        return pd.DataFrame(columns=["Date", "Time", "User", "Message"])

    # Split lines
    chat_data = text.splitlines()

    messages = []

    # Improved WhatsApp regex
    pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}),\s*(\d{1,2}:\d{2}\s?[ap]m)\s*-\s*(.*?):\s(.*)"

    for line in chat_data:

        # Remove special unicode spaces
        line = line.replace("\u202f", " ")

        match = re.match(pattern, line, re.IGNORECASE)

        if match:
            date = match.group(1)
            time = match.group(2)
            user = match.group(3)
            message = match.group(4)

            messages.append([date, time, user, message])

    df = pd.DataFrame(messages, columns=["Date", "Time", "User", "Message"])

    return df