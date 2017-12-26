def integral(f, t1, t2, dt=0.1):
    # area begins at 0.0
    area = 0.0

    # t starts at the lower bound of integration
    t = t1

    # integration continues until we reach upper bound
    while t < t2:

        # calculate the TINY bit of area associated with
        # this particular rectangle and add to total
        dA = f(t) * dt
        area += dA
        t += dt
    return area

def f1(t):
    return t**2

integral(f1, 2, 4)

show_approximate_integral(f1,2,4,20)
=======
def f2(t):
    return 3 * t**3 - 4*t

integral(f2, -2, 2, 0.0001)

=======
from math import sqrt, pi

def f3(t):
    coeff    = 1.0 / sqrt(2 * pi * 0.2)
    exponent = -(t-5)**2 / (2*0.2)
    return coeff * np.exp(exponent)

integral(f3, 3, 7, 0.001)
