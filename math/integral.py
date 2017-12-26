# visualizaing
from matplotlib import pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def show_approximate_integral(f, t_min, t_max, N):
    t = np.linspace(t_min, t_max)
    plt.plot(t, f(t))

    delta_t = (t_max - t_min) / N

    print("Approximating integral for delta_t =",delta_t, "seconds")
    box_t = np.linspace(t_min, t_max, N, endpoint=False)
    box_f_of_t = f(box_t)
    plt.bar(box_t, box_f_of_t,
            width=delta_t,
            alpha=0.5,
            facecolor="orange",
            align="edge",
            edgecolor="gray")
    plt.show()

def f1(t):
    return -1.3 * t**3 + 5.3 * t ** 2 + 0.3 * t + 1

N = 2
show_approximate_integral(f1,0,4,N)
