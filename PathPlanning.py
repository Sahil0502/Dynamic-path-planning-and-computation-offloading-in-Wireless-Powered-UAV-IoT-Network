import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    path = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            break
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                
    shortest_path = []
    while end:
        shortest_path.append(end)
        end = path[end]
    shortest_path.reverse()
    
    return distances, shortest_path

def plot_graph(graph, shortest_path):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)})
    
    # Highlight shortest path
    path_edges = list(zip(shortest_path, shortest_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2.5)
    plt.title("UAV Path Planning using Dijkstra's Algorithm")
    plt.show()

# Define the graph
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 3, 'D': 4},
    'C': {'A': 5, 'B': 3, 'D': 2, 'E': 3},
    'D': {'B': 4, 'C': 2, 'E': 1},
    'E': {'C': 3, 'D': 1}
}

start_node = 'A'
end_node = 'E'
distances, shortest_path = dijkstra(graph, start_node, end_node)
print(f"Shortest path from {start_node} to {end_node}: {shortest_path} with distance {distances[end_node]}")

# Plot the graph with the shortest path
plot_graph(graph, shortest_path)
