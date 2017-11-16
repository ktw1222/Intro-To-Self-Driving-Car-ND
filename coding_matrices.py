v = [5, 10, 2, 6, 1]

# 1x5
mv = [
    [5, 10, 2, 6, 1]
]

# 5x1
vT = [
    [5],
    [10],
    [2],
    [6],
    [1]
]

# Assign Matrices to the variable
m = [
    [8, 7, 1, 2, 3],
    [1, 5, 2, 9, 0],
    [8, 2, 2, 4, 1]
]

# change the value
m[1][4] = 5

# Scalar Multiplication
r = []
for i in range(len(m)):
    row = m[i]
    new_row = []
    for j in range(len(row)):
        m_ij = m[i][j]
        r_ij = 5 * m_ij
        new_row.append(r_ij)
    r.append(new_row)
r

# Print out a matrix
def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(matrix[0]):
            m_ij = matrix[i][j]
            print(m_ij, '\t', end="")
        print('\n') #print a new line
    return

m = [
    [8, 7, 1, 2, 3],
    [1, 5, 2, 9, 0],
    [8, 2, 2, 4, 1]
]

matrix_print(m)
