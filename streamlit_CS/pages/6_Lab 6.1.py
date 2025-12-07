import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

G = nx.Graph()
G.add_edges_from([("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Charlie"), ("Charlie", "Diana"), ("Diana", "Eve"), ("Bob", "Diana"), ("Frank", "Eve"), ("Eve", "Ian"), ("Diana", "Ian"), ("Ian", "Grace"), ("Grace", "Hannah"), ("Hannah", "Jack"), ("Grace", "Jack"), ("Charlie", "Frank"), ("Alice", "Eve"), ("Bob", "Jack")])
fig, ax = plt.subplots()
pos = nx.spring_layout(G)
special_nodes = {"Bob"}
node_colors = ['red' if n in special_nodes else 'lightblue' for n in G.nodes()]
nx.draw_circular(G, with_labels=True, node_color=node_colors, font_weight='bold')
st.pyplot(fig)

degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:")
st.write("Degree Centrality")
for node, score in degree_centrality.items():
    st.write(f"{node}: {score}")

st.write("\n\n")

betweenness_centrality = nx.betweenness_centrality(G, weight='weight')
print("Betweenness Centrality:")
st.write("Betweenness Centrality")
for node, score in betweenness_centrality.items():
    st.write(f"{node}: {score}")

st.write("\n\n")

closeness_centrality = nx.closeness_centrality(G)
print("Closeness Centrality:")
st.write("Closeness Centrality")
for node, score in closeness_centrality.items():
    st.write(f"{node}: {score}")

st.write("\n\n")

communities = greedy_modularity_communities(G)
for i, community in enumerate(communities, 1):
    st.write(f"Community {i}: {list(community)}")

st.write("\n\nIn this graph, there are three primary community groups, with group 1 being made up of Bob, Charlie, Alice, and Frank, group 2 being made up of Ian, Diana, and Eve, and group 3 being made up of Hannah, Grace, and Jack. Bob, Charlie, Diana, and Eve have the highest degree centralities, Bob has the highest betweenness centrality, and Bob also has the highest closeness centrality. Bob is the most influential person in this graph and is depicted in red.")
