from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd

def detect_semantic_topics(df):

    docs = df["Clean_Message"].astype(str)

    # Convert text into vectors
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=1000
    )

    X = vectorizer.fit_transform(docs)

    # Create topic clusters
    num_topics = 5

    kmeans = KMeans(
        n_clusters=num_topics,
        random_state=42
    )

    df["Topic"] = kmeans.fit_predict(X)

    # Top keywords per topic
    terms = vectorizer.get_feature_names_out()

    topic_keywords = []

    for i in range(num_topics):

        center_terms = (
            kmeans.cluster_centers_[i]
            .argsort()[-5:]
        )

        keywords = [
            terms[index]
            for index in center_terms
        ]

        topic_keywords.append({
            "Topic": i,
            "Keywords": ", ".join(keywords)
        })

    topic_info = pd.DataFrame(topic_keywords)

    return df, topic_info