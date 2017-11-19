def inverse_matrix(matrix):

    inverse = []
    # formula for a 1x1 matrix and 2x2 matrix
    if len(matrix) != len(matrix[0]):
        raise ValueError('The matrix must be square')

    if len(matrix) > 2:
        raise ValueError('The matrix is too large')

    if len(matrix) == 1:
        inverse.append([1/matrix[0][0]])

    if len(matrix) == 2:
        determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

        return [[matrix[1][1]/determinant, -1*matrix[0][1]/determinant],
                [-1*matrix[1][0]/determinant, matrix[0][0]/determinant]]

    return inverse
