from random import random

import numpy as np


def create_array():
    """
    Create a 1D NumPy array with values from 0 to 9.

    Returns:
        np.ndarray: A 1D NumPy array with values from 0 to 9.
    """
    return np.arange(10)

def create_array_with_value():
    a= np.array([1,2,3,4,5]) # this is a vector
    print(a)

def create_2d_array():
    print(np.array([[1, 2, 3], [4, 5, 6]])) # this is a matrix

def create_3d_array():
    print(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])) #this is a tensor

def create_array_with_zeros():
    print(np.zeros((3, 4))) # this will create a 3x4 matrix with all elements as 0

def create_array_with_dp():
    print(np.array([1,2,4],dtype=float)) # this will create a 1D array with float data type

def create_array_with_arange():
    print(np.arange(0, 10, 2)) # this will create a 1D array with values from 0 to 10 with step size of 2

def create_array_with_reshape():
    print(np.arange(10).reshape(2, 5)) 
    # this will create a 2x5 matrix with values from 0 to 9,
    # 2 rows and 5 columns
    # the product of rows 2 and columns 5 should be equal to the number of elements in the array 10

def create_array_with_random():
    print(np.random.rand(3, 4)) # this will create a 3x4 matrix with random values between 0 and 1

def create_array_with_linspace():
    print(np.linspace(0, 1, 5)) # this will create a 1D array with 5 values between 0 and 1, equally spaced

def create_array_with_identity():
    print(np.eye(3)) 
    # this will create a 3x3 identity matrix, 
    #diagonal elements are 1 and all other elements are 0

# create_array_with_arange()
def create_array_with_slicing():
    a= np.arange(12).reshape(4, 3)
    print(a)
    print(a[1:3,0:2]) 
    # rows 1 and 2 because the stop index 3 is excluded
    # columns 0 and 1 because the stop index 2 is excluded

def fancy_indexing():
    a= np.arange(24).reshape(6, 4)
    print(a)
    print(a[[0, 2], [1, 2]]) 
    # this will select the elements at (0,1) and (2,2) which are 1 and 8
    print(a[[0, 2], :])
    # this will select the rows 0 and 2 and all columns
    print(a[:, [1, 2]])
    # this will select all rows and columns 1 and 2
    print(a[0,2:4])
    # this will select the elements at row 0 and columns 2 and 3 which are 2 and 3
    print(a[0,2,3])
    # this will select the element at row 0 and column 2 which is 2

def boolean_indexing():
    a= random.randint(1,100,24).reshape(6, 4)
    # this will create a random matrix of numbers between 1 and 100 with 24 elements and shape 6x4
    print()
    print(a)