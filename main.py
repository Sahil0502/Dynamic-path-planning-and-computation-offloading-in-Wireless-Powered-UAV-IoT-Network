# main.py
from path_planning.dijkstra_algorithm import run_dijkstra
from path_planning.graph_visualization import plot_graph
from computation_offloading.offloading_simulation import run_offloading_simulation
from computation_offloading.offloading_visualization import plot_offloading_simulation
from wireless_power_transfer.wpt_simulation import run_wpt_simulation
from wireless_power_transfer.wpt_visualization import plot_wpt_simulation

def main():
    print("Starting UAV IoT Network Research Project Simulations...")

    # Dynamic Path Planning
    print("\nRunning Dynamic Path Planning (Dijkstra's Algorithm)...")
    graph = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'C': 3, 'D': 4},
        'C': {'A': 5, 'B': 3, 'D': 2, 'E': 3},
        'D': {'B': 4, 'C': 2, 'E': 1},
        'E': {'C': 3, 'D': 1}
    }
    start_node = 'A'
    end_node = 'E'
    distances, shortest_path = run_dijkstra(graph, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path} with distance {distances[end_node]}")
    plot_graph(graph, shortest_path)

    # Computation Offloading
    print("\nRunning Computation Offloading Simulation...")
    initial_energy = 100
    energy_threshold = 30
    energy_levels, offloading_points = run_offloading_simulation(initial_energy, energy_threshold)
    print(f"Energy levels: {energy_levels}")
    print(f"Tasks offloaded at points: {offloading_points}")
    plot_offloading_simulation(energy_levels, offloading_points)

    # Wireless Power Transfer
    print("\nRunning Wireless Power Transfer (WPT) Simulation...")
    max_power = 50  # Max power in watts
    efficiency_constant = 100  # Efficiency constant for WPT
    distances, transferred_powers = run_wpt_simulation(max_power, efficiency_constant)
    print(f"Transferred power over distances: {transferred_powers}")
    plot_wpt_simulation(distances, transferred_powers)

if __name__ == "__main__":
    main()
