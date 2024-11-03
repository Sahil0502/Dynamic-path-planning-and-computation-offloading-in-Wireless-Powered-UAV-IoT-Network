import numpy as np

class UAV:
    def __init__(self, initial_energy, threshold):
        self.energy = initial_energy
        self.threshold = threshold

    def perform_task(self):
        self.energy -= np.random.uniform(5, 15)  # Random energy consumption per task
        return self.energy

    def should_offload(self):
        return self.energy < self.threshold

# Simulation parameters
initial_energy = 100
energy_threshold = 30
uav = UAV(initial_energy=initial_energy, threshold=energy_threshold)

energy_levels = []
offloading_points = []

# Simulate 10 tasks
for task in range(10):
    current_energy = uav.perform_task()
    energy_levels.append(current_energy)
    if uav.should_offload():
        offloading_points.append(task)

# Plot energy levels over tasks
plt.figure(figsize=(10, 5))
plt.plot(energy_levels, label="UAV Energy Level", marker="o", color="blue")
plt.axhline(y=energy_threshold, color="red", linestyle="--", label="Offloading Threshold")
plt.scatter(offloading_points, [energy_levels[i] for i in offloading_points], color="red", label="Offloaded Tasks")
plt.title("Computation Offloading Simulation")
plt.xlabel("Task Number")
plt.ylabel("Energy Level")
plt.legend()
plt.show()
