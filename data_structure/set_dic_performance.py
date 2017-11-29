import time
import random
from matplotlib import pyplot as plt

def test_data_structure_speed(data_structure_type, size, N=50):
    if data_structure_type != dict:
        data_structure = data_structure_type(range(size))
    else:
        data_structure = {num: "value" for num in range(size)}
    nonexistent_element = -1

    start = time.clock()
    for _ in range(N):
        nonexistent_element in data_structure
    end = time.clock()

    millis = (end-start) * 1000
    return millis    
