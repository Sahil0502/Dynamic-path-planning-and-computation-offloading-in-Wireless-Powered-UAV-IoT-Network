# wireless_power_transfer/wpt_simulation.py

import numpy as np

def run_wpt_simulation(max_power, efficiency_constant):
    distances = np.arange(1, 11)
    transferred_powers = max_power * (efficiency_constant / (distances**2))
    return distances, transferred_powers
