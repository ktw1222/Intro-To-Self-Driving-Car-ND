import math
from math import sqrt
import numbers

def zeroes(height, width):
    g = [[0.0 for _ in range(width)] for __ in range(height)]

    return Matrix(g)

def identity(n):

    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0

    return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])


    def determinant(self):

        #determinant of a 1x1 or 2x2 matrix.
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

        if self.h == 2:
            determinant = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]

            return determinant

    def trace(self):

        #the trace of a matrix (sum of diagonal entries).
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        result = 0
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    result += self.g[i][j]
        return result

        #list comprehension
        # sum(self.g[i][i] for i in range(self.h))


    def inverse(self):

        #inverse of a 1x1 or 2x2 Matrix.
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        inverse = []

        if self.h == 1:
            inverse.append([1/self.g[0][0]])

        if self.h == 2:
            determinant = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]

            return Matrix([[self.g[1][1]/determinant, -1*self.g[0][1]/determinant],
                [-1*self.g[1][0]/determinant, self.g[0][0]/determinant]])

        return Matrix(inverse)

    def T(self):

        #transposed copy of this Matrix.

        #transposed = []
        #for i in range(self.w):
         #   for j in range(self.h):
          #      transposed[i][j] = self.g[j][i]

        #return transposed

        num_rows = self.w
        num_cols = self.h
        new_matrix = zeroes(num_rows, num_cols)
        for i in range(self.h):
            for j in range(self.w):
                untransposed_value = self.g[i][j]
                new_matrix[j][i] = untransposed_value
        return new_matrix

    #list comprehension
    #return Matrix([[self.g[j][i] for j in range(self.h)] for i in range(self.w)])

    def is_square(self):
        return self.h == self.w


    #Operator Overloading
    def __getitem__(self,idx):

        return self.g[idx]

    def __repr__(self):

        # Defines the behavior of calling print on an instance of this class.

        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):

        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")

        added = []

        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                v1 = self.g[i][j]
                v2 = other.g[i][j]
                new_v = v1 + v2
                new_row.append(new_v)
            added.append(new_row)

        return Matrix(added)

    def __neg__(self):

        #neg_grid = []

        #for i in range(self.h):
         #   new_row = []
          #  for j in range(self.w):
           #     new_row.append(-self.g[i][j])
            #neg_grid.append(new_row)

        #return neg_grid

        new_grid = []
        for row in self.g:
            new_row = []
            for value in row:
                new_value = -1 * value
                new_row.append(new_value)
            new_grid.append(new_row)
        return Matrix(new_grid)


    def __sub__(self, other):

        #substracted = []
        #row = []

        #for i in range(self.h):
         #   new_row = []
          #  for j in range(self.w):
           #     v1 = self.g[i][j]
           #    v2 = other.g[i][j]
            #    new_v = v1 - v2
             #   new_row.append(new_v)
            #row.append(new_row)
        #substracted.append(row)

        #return Matrix(substracted)
        return self + -other

    def __mul__(self, other):

        result = []
        for i in range(self.h):
            result.append([0]*other.w)

        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    result[i][j] += self.g[i][k] * other.g[k][j]

        return Matrix(result)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            new_g = []
            for row in self.g:
                new_row = []
                for val in row:
                    new_row.append(val * other)
                new_g.append(new_row)
            return Matrix(new_g)

            pass
