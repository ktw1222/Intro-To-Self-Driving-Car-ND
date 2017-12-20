def get_derivative(f):
    def f_dot(t):
        return approximate_derivative(f,t)
    return f_dot

# plot 1 of vertical POSITION vs TIME
plot_continuous_function(position_b, 0, 6.12)
plt.show()

# plot 2 of VELOCITY vs TIME
velocity_b = get_derivative(position_b)
plot_continuous_function(velocity_b, 0, 6.12)
plt.show()

# plot 3 of ACCELERATION vs TIME
# Note that the acceleration is a constant value
# of -9.8 m/s/s. That's because gravity always causes
# objects to accelerate DOWNWARDS at that rate.

acceleration_b = get_derivative(velocity_b)
plt.ylim([-11, -9])
plot_continuous_function(acceleration_b, 0, 6.12)
plt.show()

# plot 4 - All 3 plots at once!
plot_continuous_function(position_b, 0, 6.12)
plot_continuous_function(velocity_b, 0, 6.12)
plot_continuous_function(acceleration_b, 0, 6.12)
plt.show()
