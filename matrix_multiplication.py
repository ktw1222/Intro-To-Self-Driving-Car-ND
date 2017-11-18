

def get_low(matrix, row):
    return matrix[row]

def get_column(matrix, column_number):

    column = []
    for row in matrix:
        cols = row[column_number]
        column.append(cols)
    return column

def dot_product(vector_one, vector_two):

    result = 0
    for i in range(len(vector_one)):
        v1 = vector_one[i]
        v2 = vector_two[i]
        result += v1 * v2
    return result

def matrix_multiplication(matrixA, matrixB):

    result = []
    for i in range(len(matrixA)):
        result.append([0]*len(matrixB[0]))

    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    for r in result:
        print(r)
