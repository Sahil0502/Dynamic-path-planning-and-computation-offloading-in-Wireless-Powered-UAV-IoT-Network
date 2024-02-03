(* // Python Jupiter Notebook File *)

import json
import random
import time
import threading
import tkinter as tk
from tkinter import ttk
# from UAV import UAV
from enum import Enum
import matplotlib.pyplot as plt

# Load configuration file
with open('config.json') as config_file:
    config_data = json.load(config_file)


class SensorType(Enum):
    TYPE_1 = 0
    TYPE_2 = 1
    TYPE_3 = 2
    TYPE_4 = 3
    TYPE_5 = 4


class Sensor:
    sensor_range_values = [20, 22, 28, 25, 35]
    sensor_id_counter = 0

    def __init__(self, sensor_type, battery_percentage):
        self.sensor_type = sensor_type
        self.battery_percentage = battery_percentage
        self.sensor_range = self.sensor_range_values[sensor_type.value]
        self.location = self.generate_location()
        self.sensor_id = self.generate_sensor_id()

    def generate_location(self):
        x = random.randint(0, 100)  # Change range to 0-100
        y = random.randint(0, 100)  # Change range to 0-100
        return x, y

    def generate_sensor_id(self):
        Sensor.sensor_id_counter += 1
        return Sensor.sensor_id_counter

    def display_details(self):
        print("Sensor ID:", self.sensor_id)
        print("Sensor Type:", self.sensor_type)
        print("Battery Percentage:", self.battery_percentage)
        print("Sensor Range:", self.sensor_range)
        print("Location:", self.location)
        print()


class EventType(Enum):
    TYPE_1 = 0
    TYPE_2 = 1
    TYPE_3 = 2
    TYPE_4 = 3
    TYPE_5 = 4


class Event:
    event_range_values = [10, 12, 8, 5, 15]
    event_duration_values = [9, 10, 6, 15, 11]
    total_events = 1  # Initialize total_events to

    def __init__(self, event_type, time_interval, event_time):
        self.event_id = Event.total_events
        self.event_type = event_type
        self.event_range = self.event_range_values[event_type.value]
        self.event_duration = self.event_duration_values[event_type.value]
        self.time_interval = time_interval
        self.start_time = event_time
        self.end_time = self.start_time + self.event_duration
        Event.total_events += 1
        self.event_name = f"Event{Event.total_events}"
        self.location = self.generate_location()
    def generate_location(self):
        x = random.randint(0, 100)  # Change range to 0-100
        y = random.randint(0, 100)  # Change range to 0-100
        return x, y

    def display_details(self):
        print("Event Type:", self.event_type)
        print("Event Range:", self.event_range)
        print("Location:", self.location)
        print("Time Interval:", self.time_interval)
        print("Event Duration:", self.event_duration)
        print()

    def run(self):
        time.sleep(self.event_duration)
        # Event completed

    def generate_next(self):
        time.sleep(self.time_interval)
        new_event_type = random.choice(list(EventType))
        new_event_time = self.end_time + self.time_interval  # Use end_time instead of event_time
        new_event = Event(new_event_type, self.time_interval, new_event_time)
        event_details.append(new_event)
        new_event.run()
        new_event.generate_next()


# Function to calculate distance between two points
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Assign sensors to UAVs based on distance and number of sensors
def assign_sensors_to_uavs(uavs, sensors):
    remaining_sensors = sensors.copy()

    for sensor in sensors:
        distances = [calculate_distance(uav.start_position, sensor.location) for uav in uavs]
        min_distance = min(distances)

        if distances.count(min_distance) == 1:
            uav_index = distances.index(min_distance)
            uavs[uav_index].sensors_assigned.append(sensor)
        else:
            uav1_index = distances.index(min_distance)
            uav1 = uavs[uav1_index]
            uav2_index = distances.index(min_distance, uav1_index + 1)
            uav2 = uavs[uav2_index]

            if len(uav1.sensors_assigned) < len(uav2.sensors_assigned):
                uav1.sensors_assigned.append(sensor)
            else:
                uav2.sensors_assigned.append(sensor)

        # Remove the assigned sensor from remaining_sensors once
        remaining_sensors.remove(sensor)


# Define sensor details
num_sensors = config_data["num_sensors"]
sensor_details = []
for _ in range(num_sensors-1):
    sensor_type = random.choice(list(SensorType))
    battery_percentage = random.randint(50, 100)
    sensor = Sensor(sensor_type, battery_percentage)
    sensor_details.append(sensor)

# Display sensor details
print("Sensor Details:")
for sensor in sensor_details:
    sensor.display_details()

# Define event details
event_type = random.choice(list(EventType))
event_time = 0
event1 = Event(event_type, 5, event_time)
event_details = [event1]

# Generate events during simulation time
num_events = config_data["num_events"]
event_start_times = []
event_end_times = []
event_names = []
for _ in range(num_events-1):
    event_type = random.choice(list(EventType))
    if event_end_times:
        event_time = event_end_times[-1] + 5  # end time of last event + time interval
    else:
        event_time = 0
    event = Event(event_type, 5, event_time)
    event_start_times.append(event.start_time)
    event_end_times.append(event.end_time)
    event_names.append(event.event_name)
    event_details.append(event)

# Create UAVs
num_uavs = config_data["num_uavs"]
uavs = []
for i in range(num_uavs):
    uav = UAV(f"UAV{i + 1}", (random.randint(0, 100), random.randint(0, 100)), random.randint(500, 1000), random.randint(80, 100))  # Example range_limit and battery_percentage values
    uavs.append(uav)

# Assign sensors to UAVs
assign_sensors_to_uavs(uavs, sensor_details)

# Calculate optimal paths for UAVs
for uav in uavs:
    uav.find_optimal_path(sensor_details)

# Display UAV details and path
print("UAV Details:")
for uav in uavs:
    uav.display_details()

# Start UAV navigation
for uav in uavs:
    uav.navigate()

# Display UAV details and assigned sensors
print("UAV Details:")
for uav in uavs:
    print(f"Assigned Sensors for {uav.name}:")
    for sensor in uav.sensors_assigned:
        sensor.display_details()

def run_event(event):
    time.sleep(event.event_time)
    event.run()

def run_events(events):
    for i in range(len(events)):
        run_event(events[i])
        if i < len(events) - 1:  # If this is not the last event
            time.sleep(events[i + 1].event_time)  # Wait for the time interval before the next event starts

# Create a Tkinter application
class UAVSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UAV Simulation")

        # Create a Notebook widget for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.sensor_tab = ttk.Frame(self.notebook)
        self.event_tab = ttk.Frame(self.notebook)
        self.uav_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.sensor_tab, text="Sensor")
        self.notebook.add(self.event_tab, text="Event")
        self.notebook.add(self.uav_tab, text="UAV")

        # Create tables for Sensor and Event tabs (same as before)
        self.create_sensor_table()
        self.create_event_table()

        # Create sub-tabs for UAV tab
        self.uav_notebook = ttk.Notebook(self.uav_tab)
        self.uav_notebook.pack(fill=tk.BOTH, expand=True)

        # Create a tab for each UAV
        for uav in uavs:
            uav_tab = ttk.Frame(self.uav_notebook)
            self.uav_notebook.add(uav_tab, text=f"{uav.name}")
            self.create_uav_table(uav, uav_tab)

        self.uav_table = None
        self.current_uav = None

    def create_sensor_table(self):
        # Create a Treeview widget for the Sensor tab
        columns = ["Sensor ID", "Sensor Type", "Battery Percentage", "Sensor Range", "Location"]
        self.sensor_table = ttk.Treeview(self.sensor_tab, columns=columns, show='headings')
        for col in columns:
            self.sensor_table.heading(col, text=col)
            self.sensor_table.column(col, width=100)

        # Populate the sensor table
        for sensor in sensor_details:
            self.sensor_table.insert("", "end", values=(sensor.sensor_id, sensor.sensor_type.name,
                                                       sensor.battery_percentage, sensor.sensor_range,
                                                       sensor.location))

        self.sensor_table.pack(expand=True, fill='both')

    def create_event_table(self):
        # Create a Treeview widget for the Event tab
        columns = ["Event ID", "Event Type", "Event Range", "Location", "Time Interval", "Event Duration", "Start Time",
                   "End Time"]
        self.event_table = ttk.Treeview(self.event_tab, columns=columns, show='headings')
        for col in columns:
            self.event_table.heading(col, text=col)
            self.event_table.column(col, width=100)

        # Populate the event table
        for event in event_details:
            self.event_table.insert("", "end", values=(event.event_id, event.event_type.name, event.event_range,
                                                       event.location, event.time_interval, event.event_duration,
                                                       event.start_time, event.end_time))

        self.event_table.pack(expand=True, fill='both')

    def create_uav_table(self, uav, tab):
        # Create a Treeview widget for each UAV tab
        columns = ["Sensor ID", "Sensor Type", "Battery Percentage", "Sensor Range", "Location"]
        uav_table = ttk.Treeview(tab, columns=columns, show='headings')
        for col in columns:
            uav_table.heading(col, text=col)
            uav_table.column(col, width=100)

        # Make a copy of the battery_values list for plotting
        battery_values_copy = uav.battery_values.copy()

        # Populate the UAV table for the given UAV
        for sensor in uav.sensors_assigned:
            if len(battery_values_copy) > 0:
                battery_percentage = battery_values_copy.pop(0)
                # Check if the battery percentage is a number before formatting
                if isinstance(battery_percentage, (int, float)):
                    formatted_battery_percentage = "{:.2f}%".format(battery_percentage)
                else:
                    formatted_battery_percentage = battery_percentage  # Use the string value directly
            else:
                formatted_battery_percentage = "N/A"  # Show "N/A" if there are no more battery values

            uav_table.insert("", "end", values=(sensor.sensor_id, sensor.sensor_type.name,
                                                formatted_battery_percentage,
                                                sensor.sensor_range,
                                                sensor.location))

        # Display total distance travelled by the UAV
        total_distance = uav.calculate_total_distance()
        total_distance_label = tk.Label(tab, text=f"Total Distance Travelled: {total_distance:.2f}")
        total_distance_label.pack()

        uav_table.pack(expand=True, fill='both')
        self.uav_table = uav_table  # Store the uav_table as a class attribute
        self.current_uav = uav  # Store the current uav as a class attribute
        uav.uav_table = self.uav_table  # Set the uav_table attribute for the UAV instance

    def plot_battery_remaining(self):
        # Create a figure and axis
        fig, ax = plt.subplots()

        # Plot battery remaining for each UAV
        for uav in uavs:
            battery_values_copy = uav.battery_values.copy()
            x_values = list(range(len(battery_values_copy)))
            y_values = battery_values_copy
            ax.plot(x_values, y_values, label=f"{uav.name}")

        # Set labels and title
        ax.set_xlabel("Time")
        ax.set_ylabel("Battery Remaining (%)")
        ax.set_title("Battery Remaining for UAVs")

        # Add a legend
        ax.legend()

        # Show the plot
        plt.show()

    def plot_events_vs_time(self):
        # Create a list to store the active events during each second
        active_events = [0] * (event_end_times[-1] + 1)

        # Mark each second where an event is active
        for event in event_details:
            for i in range(event.start_time, event.end_time + 1):
                active_events[i] += 1

        # Create a figure and axis
        fig, ax = plt.subplots()

        # Plot the events as a step plot
        ax.step(range(event_end_times[-1] + 1), active_events, where='post')

        # Set labels and title
        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("Events")
        ax.set_title("Events vs. Time")

        # Show the plot
        plt.show()

    def plot_total_distance_travelled(self):
        # Create a figure and axis
        fig, ax = plt.subplots()

        # Plot total distance travelled for each UAV
        for uav in uavs:
            distance_values_copy = uav.distance_travelled_values.copy()
            x_values = list(range(len(distance_values_copy)))
            y_values = distance_values_copy
            ax.plot(x_values, y_values, label=f"{uav.name}")

        # Set labels and title
        ax.set_xlabel("Time")
        ax.set_ylabel("Total Distance Travelled")
        ax.set_title("Total Distance Travelled for UAVs")

        # Add a legend
        ax.legend()

        # Show the plot
        plt.show()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = UAVSimulationApp(root)
    root.mainloop()
    app.plot_battery_remaining()
    app.plot_events_vs_time()
    app.plot_total_distance_travelled()
    print("Event Details:")
    for i in range(len(event_names)):
        print("Event Name:", event_names[i])
        print("Start Time:", event_start_times[i])
        print("End Time:", event_end_times[i])
        print()

    print("Simulation Details:")
    print("Start Time:", 0)
    print("End Time:", event_end_times[-1])
