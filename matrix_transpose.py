def transpose(matrix):
#     row = [0 for i in range(len(matrix))]
    matrix_transpose = []

    for i in range(len(matrix[0])):
        matrix_transpose.append([0] * len(matrix))

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            matrix_transpose[i][j] = matrix[j][i]

    return matrix_transpose



# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]
#
# result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
#
# for r in result:
#    print(r)
# or
# [[row[i] for row in matrix] for i in range(4)]

# or
# transposed = []
#     for i in range(matrix[0]):
#         transposed_row = []
#         for row in matrix:
#             transposed_row.append(row[i])
#         transposed.append(transposed_row)
#
#     transposed
