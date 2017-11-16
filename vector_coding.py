def add(vector1, vector2):
    if len(vector1) != len(vector2):
        print("Error! vectors must be the same size to add")
        return

    new_vector = []
    for i in range(len(vector1)):
        value1 = vector1[i]
        value2 = vector2[i]
        new_value = value1 + value2
        new_vector.append(new_value)

    return new_vector

'''
v1 = [1,2]
v2 = [3,4]

v_1_plus_2 = add(v1, v2)

print(v1, "plus", v2, "equals", v_1_plus_2)
'''

def multiply(scalar, vector):
    new_vector = []
    for value in vector:
        new_value = scalar * vector
        new_vector.append(new_value)
    return new_vector

'''
vector = [1,2,3,4,5]
number = 3

product = multiply(number, vector)

print(number, "times", vector, "equals", product)
'''


def dot_product(v1, v2):
    if len(v1) != len(v2):
        print("Error! Vectors must be the same size")

    result = 0
    for i in range(len(v1)):
        value1 = v1[i]
        value2 = v2[i]
        result += value1 * value2
    return result

'''
vector_1 = [7,2,3]
vector_2 = [1, 10, 4]

# should be 39 (7*1 + 2*10 + 3*4)
v1_dot_v2 = dot_product(vector_1, vector_2)


print(vector_1, "dot", vector_2, "equals", v1_dot_v2)
'''
