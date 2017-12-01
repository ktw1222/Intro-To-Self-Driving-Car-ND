import numpy as np

world = np.array([ [0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0],
                   [1, 0, 0, 0, 0] ])

print('The shape of this array is: ' + str(world.shape))
print('Notice that the x and y dimensions are in the opposite order than usual!')
print('It\'s height is: ' + str(world.shape[1]) +
      ', and it\'s length/width is: ' + str(world.shape[0]))


value = world[3][0]
print('\n')
print('Value at index [3, 0] = ' +str(value))

row = 2
column_index = 0
value_left = world[row, column_index]
value_middle = world[row, column_index + 1]
value_right = world[row, column_index + 2]

print('\nThe first three values in row 2 : ' +str(value_left)+', '
                                              +str(value_middle) +', '
                                              +str(value_right) )

compare = world[0][0] == world[0][1]
print('\nDo the first two values match? ' + str(compare))
