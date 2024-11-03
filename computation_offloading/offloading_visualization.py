# computation_offloading/offloading_visualization.py

import matplotlib.pyplot as plt

def plot_offloading_simulation(energy_levels, offloading_points):
    plt.figure(figsize=(10, 5))
    plt.plot(energy_levels, label='Energy Level', color='blue')
    plt.scatter(offloading_points, [energy_levels[i] for i in offloading_points], color='red', label='Offloading Points')
    plt.xlabel('Task Number')
    plt.ylabel('Energy Level')
    plt.title('Computation Offloading Simulation')
    plt.legend()
    plt.show()
