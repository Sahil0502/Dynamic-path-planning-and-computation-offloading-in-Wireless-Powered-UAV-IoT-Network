# path_planning/graph_visualization.py

import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(graph, shortest_path):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)})
    
    # Highlight the shortest path in red
    path_edges = list(zip(shortest_path, shortest_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2.5)
    plt.title("UAV Path Planning using Dijkstra's Algorithm")
    plt.show()
