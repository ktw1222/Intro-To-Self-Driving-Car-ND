def predict_state(state, dt):

    x = state[0]
    velocity = state[1]

    new_x = x + velocity*dt

    predicted_state = [new_x, velocity]
    return predicted_state


# Initialize matrix objects
import matrix

initial_position = 0
velocity = 50

initial_state = matrix.Matrix([ [initial_position], [velocity] ])

# Transformation matrix
dt = 1
tx_matrix = matrix.Matrix([ [1, dt],
                            [0, 1 ] ])

print(tx_matrix)

# Modify the predict state function to use matrix multiplication
def predict_state_mtx(state, dt):

    predicted_state = 0

    return predicted_state

# Test cell

    # initial state variables
initial_position = 10 # meters
velocity = 30 # m/s

    # Initial state vector
initial_state = matrix.Matrix([ [initial_position],
                                [velocity] ])


print('The initial state is: ' + str(initial_state))


    # after 2 seconds make a prediction using the new function
state_est1 = predict_state_mtx(initial_state, 2)

print('State after 2 seconds is: ' + str(state_est1))
