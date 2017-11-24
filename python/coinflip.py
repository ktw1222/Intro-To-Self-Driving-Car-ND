import random as rd

num_trials = 100
heads = 0
tails = 0
p_heads = 0.5

for i in range(num_trials):
    random_number = rd.random()
    if random_number < p_heads:
        heads = heads + 1
    else:
        tails += 1

print("In", num_trials, "trials there were", heads, "heads and", tails, "tails")
print("PERCENT HEADS:", 100 * heads/num_trials, "percent")


# As a function of defining and calling
import random as rd

def simulate_coin_flips(num_trials):
    heads = 0
    tails = 0
    p_heads = 0.5
    for i in range(num_trials):
        random_number = rd.random()
        if random_number < p_heads:
            heads = heads + 1
        else:
            tails += 1
    percent_heads = heads / num_trials
    return percent_heads

percentage = simulate_coin_flips(200)
print(percentage)
