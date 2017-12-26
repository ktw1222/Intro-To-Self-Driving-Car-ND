from helpers import process_data
from matplotlib import pyplot as plt

PARALLEL_PARK_DATA = process_data("parallel_park.pickle")

PARALLEL_PARK_DATA[:5]

timestamps    = [row[0] for row in PARALLEL_PARK_DATA]
displacements = [row[1] for row in PARALLEL_PARK_DATA]

plt.title("Displacement vs Time while Parallel Parking")
plt.xlabel("Time (seconds)")
plt.ylabel("Displacement (meters)")
plt.scatter(timestamps, displacements)
plt.show()

print(timestamps[20:22])
print(displacements[20:22])

delta_x = displacements[21] - displacements[20]
delta_t = timestamps[21] - timestamps[20]
slope   = delta_x / delta_t

print(slope)

==============

def get_derivative_from_data(position_data, time_data):
    
    # 1. Check to make sure the input lists have same length
    if len(position_data) != len(time_data):
        raise(ValueError, "Data sets must have same length")

    # 2. Prepare empty list of speeds
    speeds = []

    # 3. Get first values for position and time
    previous_position = position_data[0]
    previous_time     = time_data[0]

    # 4. Begin loop through all data EXCEPT first entry
    for i in range(1, len(position_data)):

        # 5. get position and time data for this timestamp
        position = position_data[i]
        time     = time_data[i]

        # 6. Calculate delta_x and delta_t
        delta_x = position - previous_position
        delta_t = time - previous_time

        # 7. Speed is slope. Calculate it and append to list
        speed = delta_x / delta_t
        speeds.append(speed)

        # 8. Update values for next iteration of the loop.
        previous_position = position
        previous_time     = time

    return speeds

# 9. Call this function with appropriate arguments
speeds = get_derivative_from_data(displacements, timestamps)

# 10. Prepare labels for a plot
plt.title("Speed vs Time while Parallel Parking")
plt.xlabel("Time (seconds)")
plt.ylabel("Speed (m / s)")

# 11. Make the plot! Note the slicing of timestamps!
plt.scatter(timestamps[1:], speeds)
plt.show()
