from matplotlib import pyplot as plt

t = [0,1,2,3,4]
x = [0,2,4,6,8]

plt.scatter(t,x)
plt.show()

# Demonstration of continuous plotting

import numpy as np

t = np.linspace(0, 4)
x = position(t)

plt.plot(t, x)
plt.show()

def position_b(time):
    return -4.9 * time ** 2 + 30 * time

t = np.linspace(0, 6.12)
z = position_b(t)

plt.plot(t, z)
plt.show()

def plot_continuous_function(function, t_min, t_max):
    t = np.linspace(t_min, t_max)
    x = function(t)
    plt.plot(t,x)

plot_continuous_function(position_b, 0, 6.12)
plt.show()
