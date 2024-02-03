import math
import time


class UAV:
   import math
import time


class UAV:
    total_uavs = 0

    def __init__(self, name, start_position, range_limit, battery_percentage):
        UAV.total_uavs += 1
        self.name = name
        self.start_position = start_position
        self.range_limit = range_limit
        self.battery_percentage = battery_percentage
        self.path = {}  # Updated path format: {sensor_id: sensor_location, ...}
        self.sensors_assigned = []
        self.battery_values = [battery_percentage]
        self.distance_travelled_values = [0]  # Initialize with 0
    def calculate_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def update_path(self, path):
        self.path = path

    def find_optimal_path(self, sensors):
        current_position = self.start_position
        remaining_sensors = self.sensors_assigned.copy()  # Use the assigned sensors instead of all sensors
        path = {0: current_position}  # Start position represented as {0: start_position}

        while remaining_sensors:
            nearest_sensor = None
            nearest_distance = float("inf")

            for sensor in remaining_sensors:
                distance = self.calculate_distance(current_position, sensor.location)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_sensor = sensor

            if nearest_sensor:
                path[nearest_sensor.sensor_id] = nearest_sensor.location  # Assign sensor_id as key and location as value
                remaining_sensors.remove(nearest_sensor)
                current_position = nearest_sensor.location

        path[0] = self.start_position  # Return to the starting position
        self.update_path(path)

    def display_details(self):
        print("UAV Name:", self.name)
        print("Start Position:", self.start_position)
        print("Range Limit:", self.range_limit)
        print("Battery Percentage:", self.battery_percentage)
        print("Path:",self.path.keys())

        if self.path:
            for sensor_id in self.path:
                print("Sensor ID:", sensor_id)
        else:
            print("No path assigned.")

        print()

    def navigate(self):
        print(f"{self.name} is navigating.")

        total_distance = 0  # Initialize total distance

        for i in range(len(self.sensors_assigned) - 1):
            start = self.sensors_assigned[i].location
            end = self.sensors_assigned[i + 1].location

            distance = self.calculate_distance(start, end)
            total_distance += distance  # Update total distance

            # Check if the UAV can reach the next location
            if distance * 0.4 > self.battery_percentage:  # updated this line
                print(f"{self.name} needs to recharge.")
                # Perform recharge process here
                time.sleep(5)  # Simulating recharge process
                self.battery_percentage = 100  # Fully recharge the battery
                print(f"{self.name} recharged.")

            self.battery_percentage -= distance * 0.4  # updated this line
            self.battery_values.append(self.battery_percentage)  # Store the battery value
            self.distance_travelled_values.append(total_distance)  # Store the total distance travelled

            print(
                f"{self.name} traveled from {start} to {end}. Battery remaining: {self.battery_percentage}%. Total distance travelled: {total_distance}")

            # Check if the battery percentage is below 10%
            if self.battery_percentage < 10:
                print(f"{self.name} has reached the low battery level. Returning to the charging point.")
                return_distance = self.calculate_distance(end, self.start_position)

                # Check if there is enough battery to return to the charging point
                if return_distance * 0.4 > self.battery_percentage:  # updated this line
                    print(f"{self.name} does not have enough battery to return to the charging point.")
                    return

                # Update the remaining battery percentage after returning to the charging point
                self.battery_percentage -= return_distance * 0.4  # updated this line
                self.battery_values.append(self.battery_percentage)  # Store the battery value
                total_distance += return_distance  # Add the return distance to total distance
                self.distance_travelled_values.append(total_distance)  # Store the total distance travelled

                print(
                    f"{self.name} returned to the charging point. Battery remaining: {self.battery_percentage}%. Total distance travelled: {total_distance}")

        print(f"{self.name} completed navigation.")


    def calculate_total_distance(self):
        total_distance = 0
        path_list = list(self.path.values())
        for i in range(len(path_list) - 1):
            total_distance += self.calculate_distance(path_list[i], path_list[i + 1])
        return total_distance
