import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load cleaned chat data
df = pd.read_csv("output/clean_chat_data.csv")

# Combine all messages
text = " ".join(df["Clean_Message"].dropna())

# Generate word cloud
wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color='white'
).generate(text)

# Display word cloud
plt.figure(figsize=(12,6))

plt.imshow(wordcloud, interpolation='bilinear')

plt.axis("off")

plt.title("Most Common Words in Chat")

# Save image
plt.savefig("output/wordcloud.png")

plt.show()

print("\nWord cloud generated successfully!")