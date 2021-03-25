import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
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

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        determinant_value = 0
        if self.h == 1:
            determinant_value = self.g[0][0]
        return determinant_value
    
        
            
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
            determinant_value = (a*d) - (b*c) 
            
        return determinant_value
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        trace_value = 0
        for i in range(len(self.g)):
            for j in range(len(self.g[0])):
                if i == j:
                    trace_value = trace_value + self[i][j]
        
        return trace_value
            
            
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        
        inverse_value = []
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        if self.h == self.w == 1:
            inverse_value.append([1/self.g[0][0]])
            return Matrix(inverse_value)
        elif self.h == self.w == 2:
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise ValueError('The matrix is not invertible.')
            
            else:
                inverse_value = zeroes(self.w, self.h)
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
                
                # Define determinant and initialize the inverse
                #det = self.determinant()
                
                
                """
                factor = 1/determinant()
                inverse_value = [[-d, b],[c, -a]]
                for i in range(len(inverse_value)):
                    for j in range(len(inverse_value[0])):
                        inverse_value[i][j]= factor * inverse_value[i][j]
                """
                #if self.determinant() == 0 : 
                #raise ValueError(' The matrix is not invertible')
                
                
                inverse_value[0][0] = (1/(a*d - b*c)) * d
                inverse_value[0][1] = (1/(a*d - b*c)) * -b
                inverse_value[1][0] = (1/(a*d - b*c)) * -c
                inverse_value[1][1] = (1/(a*d - b*c)) * a
        return inverse_value
        
        
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        
        Transpose = zeroes(self.w,self.h)
        for i in range(self.w):
            #new_row = []
            for j in range(self.h):
                Transpose[j][i] = self.g[i][j]
                #new_row.append(self.g[j][i])
            #Transpose.append(new_row)
        return Transpose
        
        
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        # creating an empty list
        addition = []
        
        # adding the states together
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])
            addition.append(row)
        
        return Matrix(addition)
        
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negative = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self[i][j])
            negative.append(row)
        
        return Matrix(negative)
        
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        # creating an empty list
        sub_grid = zeroes(self.h,self.w)
        
        # subtracting the states together
        for i in range(self.h):
            for j in range(self.w):
                sub_grid[i][j] = self.g[i][j] - other.g[i][j]
            
        
        return sub_grid

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        # creating new matrix with zero() function
        
        new_grid = zeroes(self.h,other.w)
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    new_grid[i][j] += self.g[i][k] * other.g[k][j]
        
        return new_grid

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            new_matrix = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other*self[i][j])
                new_matrix.append(row)
            return Matrix(new_matrix)
            