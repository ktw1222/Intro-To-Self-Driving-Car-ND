def identity_matrix(n):

    result =[]

    for i in range(n):
      row = []
      for j in range(n):
        if i == j:
          row.append(1)
        else:
          row.append(0)
      result.append(row)
    return result



# def identity_matrix(n):
#
#     result = []
#
#     for i in range(n):
#         row = [0]*n
#         row[i] = 1
#         result.append(row)
#
#     return result


# list comprehension
# return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
