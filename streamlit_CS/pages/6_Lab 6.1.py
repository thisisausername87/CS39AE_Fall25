import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

G = nx.Graph()
G.add_edges_from([("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Charlie"), ("Charlie", "Diana"), ("Diana", "Eve"), ("Bob", "Diana"), ("Frank", "Eve"), ("Eve", "Ian"), ("Diana", "Ian"), ("Ian", "Grace"), ("Grace", "Hannah"), ("Hannah", "Jack"), ("Grace", "Jack"), ("Charlie", "Frank"), ("Alice", "Eve"), ("Bob", "Jack")])
fig, ax = plt.subplots()
pos = nx.spring_layout(G)
nx.draw_circular(G, with_labels=True, node_color='lightblue', font_weight='bold')
st.pyplot(fig)

degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:")
for node, score in degree_centrality.items():
    print(f"{node}: {score}")

print("\n")

betweenness_centrality = nx.betweenness_centrality(G, weight='weight')
print("Betweenness Centrality:")
for node, score in betweenness_centrality.items():
    print(f"{node}: {score}")

print("\n")

closeness_centrality = nx.closeness_centrality(G)
print("Closeness Centrality:")
for node, score in closeness_centrality.items():
    print(f"{node}: {score}")
