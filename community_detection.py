import networkx as nx
import community.community_louvain as community_louvain
import pandas as pd

def detect_communities(df):

    G = nx.Graph()

    for i in range(len(df)-1):

        user1 = df.iloc[i]["User"]
        user2 = df.iloc[i+1]["User"]

        if user1 != user2:

            G.add_edge(user1, user2)

    partition = community_louvain.best_partition(G)

    community_df = pd.DataFrame({
        "User": list(partition.keys()),
        "Community": list(partition.values())
    })

    community_df.to_csv(
        "output/communities.csv",
        index=False
    )

    return partition