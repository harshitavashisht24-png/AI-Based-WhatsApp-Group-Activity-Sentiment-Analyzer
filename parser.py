import re
import pandas as pd

def parse_chat_data(chat_content):
    # This pattern is what Member 1 wrote
    pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}\s?[ap]m)\s-\s(.*?):\s(.*)"
    messages = []

    # Member 1 used 'readlines()', we will split the uploaded text into lines
    lines = chat_content.split('\n')

    for line in lines:
        match = re.match(pattern, line)
        if match:
            date = match.group(1)
            time = match.group(2)
            user = match.group(3)
            message = match.group(4)
            messages.append([date, time, user, message])

    df = pd.DataFrame(messages, columns=["Date", "Time", "User", "Message"])
    return df