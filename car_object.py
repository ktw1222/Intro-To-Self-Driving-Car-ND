import numpy as np
import car

%matplotlib inline

# Create a 2D world of 0's
height = 4
width = 6
world = np.zeros((height, width))

initial_position = [0, 0] # [y, x] (top-left corner)
velocity = [0, 1] # [vy, vx] (moving to the right)

# Create a car object with these initial params
carla = car.Car(initial_position, velocity, world)

print('Carla\'s initial state is: ' + str(carla.state))

carla.move()

carla.display_world()

carla.turn_left()
