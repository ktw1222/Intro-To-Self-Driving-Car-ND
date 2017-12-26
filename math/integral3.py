from helpers import process_data, get_derivative_from_data
from matplotlib import pyplot as plt

PARALLEL_PARK_DATA = process_data("parallel_park.pickle")

TIMESTAMPS    = [row[0] for row in PARALLEL_PARK_DATA]
DISPLACEMENTS = [row[1] for row in PARALLEL_PARK_DATA]
YAW_RATES     = [row[2] for row in PARALLEL_PARK_DATA]
ACCELERATIONS = [row[3] for row in PARALLEL_PARK_DATA]

plt.title("Displacement vs Time while Parallel Parking")
plt.xlabel("Time (seconds)")
plt.ylabel("Displacement (meters)")
plt.scatter(TIMESTAMPS, DISPLACEMENTS)
plt.show()

speeds = get_derivative_from_data(DISPLACEMENTS, TIMESTAMPS)

plt.title("Speed vs Time while Parallel Parking")
plt.xlabel("Time (seconds)")
plt.ylabel("Speed (m / s)")
plt.scatter(TIMESTAMPS[1:], speeds)
plt.show()

accels = get_derivative_from_data(speeds, TIMESTAMPS[1:])

plt.title("Acceleration vs Time while Parallel Parking")
plt.xlabel("Time (seconds)")
plt.ylabel("Acceleration (m / s / s)")
plt.scatter(TIMESTAMPS[2:], accels)
plt.show()

# integral
def get_integral_from_data(acceleration_data, times):
    # 1. We will need to keep track of the total accumulated speed
    accumulated_speed = 0.0

    # 2. The next lines should look familiar from the derivative code
    last_time = times[0]
    speeds = []

    # 3. Once again, we lose some data because we have to start
    #    at i=1 instead of i=0.
    for i in range(1, len(times)):

        # 4. Get the numbers for this index i
        acceleration = acceleration_data[i]
        time = times[i]

        # 5. Calculate delta t
        delta_t = time - last_time

        # 6. This is an important step! This is where we approximate
        #    the area under the curve using a rectangle w/ width of
        #    delta_t.
        delta_v = acceleration * delta_t

        # 7. The actual speed now is whatever the speed was before
        #    plus the new change in speed.
        accumulated_speed += delta_v

        # 8. append to speeds and update last_time
        speeds.append(accumulated_speed)
        last_time = time
    return speeds

# 9. Now we use the function we just defined
integrated_speeds = get_integral_from_data(ACCELERATIONS, TIMESTAMPS)

# 10. Plot
plt.scatter(TIMESTAMPS[1:], integrated_speeds)
plt.show()

integrated_displacements = get_integral_from_data(integrated_speeds,
                                                 TIMESTAMPS[1:])
plt.scatter(TIMESTAMPS[2:], integrated_displacements)
plt.show()
