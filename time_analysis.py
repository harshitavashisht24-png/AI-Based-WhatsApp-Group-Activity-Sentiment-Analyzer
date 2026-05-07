import pandas as pd
import matplotlib.pyplot as plt

# Load chat data
df = pd.read_csv("output/chat_data.csv")

# Extract hour from time column
df["Hour"] = df["Time"].str.extract(r'(\d{1,2})').astype(int)

# Count messages per hour
hourly_activity = df["Hour"].value_counts().sort_index()

# Print activity
print("\nMESSAGES BY HOUR:")
print(hourly_activity)

# Plot graph
plt.figure(figsize=(10,5))

hourly_activity.plot(kind='bar')

plt.title("Hourly Chat Activity")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Messages")

plt.tight_layout()

# Save graph
plt.savefig("output/hourly_activity.png")

plt.show()

print("\nHourly analysis completed!")