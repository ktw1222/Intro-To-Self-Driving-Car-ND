from math import sin, cos, tan, pi
from matplotlib import pyplot as plt
import numpy as np

print(sin(60))

def deg2rad_solution(theta):
    # Converts degrees to radians
    return theta * pi / 180

def plot_cosine_solution(min_theta, max_theta):
    angles_degrees = np.linspace(min_theta, max_theta)
    angles_radians = deg2rad_solution(angles_degrees)
    values = np.cos(angles_radians)
    X = angles_degrees
    Y = values
    plt.plot(X,Y)
    plt.show()

def plot_sine(min_theta, max_theta):
    angles_degrees = np.linspace(min_theta, max_theta)
    angles_radians = deg2rad(angles_degrees)
    values = np.sin(angles_radians)
    X = angles_degrees
    Y = values
    plt.plot(X,Y)
    plt.show()
