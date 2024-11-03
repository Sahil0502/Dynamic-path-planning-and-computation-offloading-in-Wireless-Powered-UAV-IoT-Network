# Wireless Power Transfer (WPT)
class WPT:
    def __init__(self, max_transfer_power, efficiency_constant):
        self.max_transfer_power = max_transfer_power
        self.efficiency_constant = efficiency_constant

    def calculate_power_transfer(self, distance):
        efficiency = self.efficiency_constant / (distance ** 2)
        transferred_power = self.max_transfer_power * efficiency
        return max(transferred_power, 0)

# Simulation parameters
max_power = 50  # Max power (W)
efficiency_constant = 100  # Efficiency constant for simulation
distances = np.linspace(1, 20, 50)  # Distance range from 1 to 20 meters

# Calculate power transferred over distance
wpt = WPT(max_transfer_power=max_power, efficiency_constant=efficiency_constant)
transferred_powers = [wpt.calculate_power_transfer(d) for d in distances]

# Plot power transfer efficiency
plt.figure(figsize=(10, 5))
plt.plot(distances, transferred_powers, color="green", label="Power Transferred")
plt.title("Wireless Power Transfer Efficiency over Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Power Transferred (W)")
plt.legend()
plt.show()
