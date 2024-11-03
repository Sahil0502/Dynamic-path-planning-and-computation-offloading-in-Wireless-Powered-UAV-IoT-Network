# computation_offloading/offloading_simulation.py

import numpy as np

def run_offloading_simulation(initial_energy, energy_threshold):
    energy_levels = [initial_energy]
    offloading_points = []
    
    for i in range(1, 11):
        energy = energy_levels[-1] - np.random.randint(5, 15)
        energy_levels.append(energy)
        
        if energy < energy_threshold:
            offloading_points.append(i)
            energy_levels[-1] = initial_energy  # Recharging after offloading
            
    return energy_levels, offloading_points
