import numpy as np

road = np.array(['r', 'r', 'r', 'r', 'r', 's', 'r'])

length = len(road)
for index in range(0, length):

    value = road[index]

    print('road['+str(index)+'] = '+str(value))

for index in range(0, length):
    print(str(index))
    
    if index == 3:
        print('We\'ve reached the middle of the road and we\'re leaving the loop!')
        break
