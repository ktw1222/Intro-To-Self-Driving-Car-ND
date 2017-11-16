def matrix_addition(matrixA, matrixB):

    if len(matrixA) != len(matrixB):
        print("Error! Matrices must be same size")

    matrixSum = []

    row = []

    for i in range(len(matrixA)):
        new_row = []
        for j in range(len(matrixA[i])):
            m_1 = matrixA[i][j]
            m_2 = matrixB[i][j]
            new_m = m_1 + m_2
            new_row.append(new_m)
        row.append(new_row)
    matrixSum.append(row)

    return matrixSum
