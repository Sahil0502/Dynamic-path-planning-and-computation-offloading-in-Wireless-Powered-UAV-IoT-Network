# wireless_power_transfer/wpt_visualization.py

import matplotlib.pyplot as plt

def plot_wpt_simulation(distances, transferred_powers):
    plt.figure(figsize=(10, 5))
    plt.plot(distances, transferred_powers, marker='o', color='green')
    plt.xlabel('Distance')
    plt.ylabel('Transferred Power')
    plt.title('Wireless Power Transfer Efficiency')
    plt.show()
