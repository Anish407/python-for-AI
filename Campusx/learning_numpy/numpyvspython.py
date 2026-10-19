import numpy as np
import time
import sys

def display_time(function):
    def wrapper(*args, **kwargs):
        t= time.time()
        function()
        c= time.time() - t
        print(f"Time taken: {c}")
        return c
    return wrapper


@display_time
def python_array_performance():
    a= [i for i in range(10000000)]
    b=[i for i in range(10000000,20000000)]
    c=[]
    for i in range(len(a)):
        c.append(a[i] + b[i])

@display_time
def numpy_array_performance():
    a= np.arange(10000000)
    b= np.arange(10000000,20000000)
    c= a + b


def compare_python_numpy_memory():
    python_array= [i for i in range(10000000)]
    numpy_array= np.arange(10000000)
    numpy_int32= np.range(10000000, dtype=np.int32)

    print(f"Memory used by Python array: {sys.getsizeof(python_array)} ")
    print(f"Memory used by Numpy array: {sys.getsizeof(numpy_array)} ")
    print(f"Memory used by Numpy int32 array: {sys.getsizeof(numpy_int32)} ")
    
def check_performance():
    python_timing=python_array_performance()
    numpy_timing=numpy_array_performance()
    print (f"Python array time: {python_timing}")
    print (f"Numpy array time: {numpy_timing}")
    print (f"Numpy is {python_timing/numpy_timing} times faster than Python arrays")

compare_python_numpy_memory()