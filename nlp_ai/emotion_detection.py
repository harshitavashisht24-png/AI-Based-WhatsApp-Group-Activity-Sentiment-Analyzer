import os

# Disable TensorFlow completely
os.environ["USE_TF"] = "0"

from transformers import pipeline

emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    framework="pt"
)

def detect_emotions(df):

    emotions = []

    for text in df["Clean_Message"]:

        try:

            result = emotion_pipeline(
                str(text[:512])
            )

            emotions.append(
                result[0]["label"]
            )

        except Exception as e:

            print("Emotion Error:", e)

            emotions.append("neutral")

    df["Emotion"] = emotions

    return df