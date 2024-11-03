# UAV-IoT Network Research Project

### Dynamic Path Planning, Computation Offloading, and Wireless Power Transfer (WPT) for UAV-IoT Networks

This research project explores advanced algorithms for efficient and sustainable UAV (Unmanned Aerial Vehicle) operations within IoT networks. It implements **Dynamic Path Planning**, **Computation Offloading**, and **Energy-Efficient Wireless Power Transfer (WPT)** using Python. Each component simulates and visualizes critical functions in UAV IoT systems, paving the way for energy-saving, reliable, and high-performance UAV networks.

# 🚀 Features

- **Dynamic UAV Path Planning:** Shortest path optimization using Dijkstra's Algorithm.
- **Computation Offloading:** Adaptive task offloading based on energy thresholds.
- **Wireless Power Transfer (WPT):** Efficient energy transfer simulation using resonant inductive coupling.
- **Interactive Visualizations:** Real-time visualizations for path planning, offloading points, and WPT efficiency.

# 📁 Project Structure

```plaintext
UAV-IoT-Research-Project/
│
├── PROJECT_OVERVIEW.md               # Project overview
├── FEATURES.md                       # Project features
├── INSTALLATION.md                   # Installation instructions
├── USAGE.md                          # Usage guide
├── EXAMPLES.md                       # Example visualizations
├── ACKNOWLEDGMENTS.md                # Acknowledgments
├── LICENSE.md                        # License information
├── requirements.txt                  # Python libraries required
├── main.py                           # Main script to run all simulations
│
├── path_planning/
│   ├── dijkstra_algorithm.py         # Dijkstra's algorithm implementation for path planning
│   └── graph_visualization.py        # Visualization of graph with shortest path
│
├── computation_offloading/
│   ├── offloading_simulation.py      # Computation offloading simulation
│   └── offloading_visualization.py   # Visualization of energy levels and offloading points
│
└── wireless_power_transfer/
    ├── wpt_simulation.py             # Wireless power transfer simulation
    └── wpt_visualization.py          # Visualization of power transfer efficiency

```
---

# ⚙️ Usage
Run the main script to execute all simulations sequentially.

**Individual Module Details**

- **Dynamic Path Planning:**
- Implements Dijkstra's Algorithm to find the shortest path between nodes.
- Output: Path and total distance.
- Visualization: Graph highlighting the shortest path.

- **Computation Offloading:**
- Simulates offloading of tasks based on energy thresholds.
- Output: Energy levels and offloading points.
- Visualization: Graph showing energy depletion and offloading events.

- **Wireless Power Transfer (WPT):**
- Models power transfer efficiency over distance.
- Output: Transferred power levels.
- Visualization: Graph showing power efficiency across distances.


# 🤝 Acknowledgments

- **NetworkX** for graph structure and pathfinding support.
- **Matplotlib** for data visualization and real-time plotting.

# 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
