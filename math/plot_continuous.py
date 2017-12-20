def constant_position_motion(time):
    position = 20
    return position + 0*time

def constant_velocity_motion(time):
    velocity = 10
    return velocity * time

def constant_acceleration_motion(time):
    acceleration = 9.8
    return acceleration / 2 * time ** 2

plot_continuous_function(constant_position_motion, 0, 20)
plt.show()

plot_continuous_function(constant_velocity_motion, 0, 20)
plt.show()

plot_continuous_function(constant_acceleration_motion, 0, 20)
plt.show()

#EXERCISE - Find the speed of the ball at t = 3.45
#Use a sequence of steps similar to what we just did
#for  t=2t=2  to find the velocity of the ball at  t=3.45t=3.45

FIRST ATTEMPT

# 1. set some relevant parameters
TIME    = 3.45
DELTA_T = 0.02

# 2. The "window" should extend 0.01 to the left and
#    0.01 to the right of the target TIME
t_min = TIME - (DELTA_T / 2)
t_max = TIME + (DELTA_T / 2)

# 3. calculate the value of the function at the left and
#    right edges of our "window"
z_at_t_min = position_b(t_min)
z_at_t_max = position_b(t_max)

# 4. calculate vertical change
delta_z = z_at_t_max - z_at_t_min

# 5. calculate slope
slope = delta_z / DELTA_T

print("speed is",slope, "m/s at t =", TIME)

====
second (better) version
def approximate_derivative(f, t):
    # 1. Set delta_t. Note that I've made it REALLY small.
    delta_t = 0.00001

    # 2. calculate the vertical change of the function
    #    NOTE that the "window" is not centered on our
    #    target time anymore. This shouldn't be a problem
    #    if delta_t is small enough.
    vertical_change = f(t + delta_t) - f(t)

    # 3. return the slope
    return vertical_change / delta_t

deriv_at_3_point_45 = approximate_derivative(position_b, 3.45)
print("The derivative at t = 3.45 is", deriv_at_3_point_45)
