import time
import random
from matplotlib import pyplot as plt

L = list(range(1000))
element = 500
num_trials = 1000

start = time.clock()
for _ in range(num_trials):
    element in L
end = time.clock()
secs = end-start
millis = secs * 1000
millis_per_check = millis/num_trials
print("on average, it took", millis_per_check, "ms per membership test")

def avg_millis_to_check_el_in_list(element, target_list, N=20):
    start = time.clock()
    for _ in range(N):
        element in target_list
    end = time.clock()
    return (end-start)*1000 / N

avg_millis = avg_millis_to_check_el_in_list(500, list(range(1000)))
print("on average, it took", avg_millis, "ms per membership test")

=================================
list_size = 100000
L = list(range(list_size))

positions = list(range(0, list_size, 10000))

millis = [avg_millis_to_check_el_in_list(pos, L) for pos in positions]


print("positions checked:", positions)
print("average millis:   ", millis)

X = positions
Y = millis
plt.scatter(X, Y)
plt.title("Membership Test Time\nvs Position in List")
plt.xlabel("Position in List")
plt.ylabel("Average # of millis / test")
plt.show()
