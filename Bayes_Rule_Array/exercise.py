def bayes(p_A, p_B_given_A, p_notB_given_notA):

    p_notA = (1 - p_A)
    p_B_given_notA = (1 - p_notB_given_notA)

    total = (p_A * p_B_given_A) + (p_notA * p_B_given_notA)

    posterior = (p_A * p_B_given_A) / total

    return posterior

p_A = 0.2
p_B_given_A = 0.9
p_notB_given_notA = 0.5

posterior = bayes(p_A, p_B_given_A, p_notB_given_notA)
print('Your function returned that the posterior is: ' + str(posterior))
