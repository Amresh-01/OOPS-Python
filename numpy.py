# Ques: What is Numpy?
# Ans: NumPy is the fundamental packege for scientific computing in Python. It is a Python library that provides a multidimenstional
#     data types

# 1. Numpy Arrays have a fixed size at creation,unlike Python lists(which can grow dynamically). Changing the size of an ndarray will create 
# a new Array and delte the original one.

# 2. Same data type and thus will be same size in memory.

# 3. Numpy arrays facilliate advanced mathematical and other types of operations on large numbers of data. Typically,such operations
#     are executed more effficiently and with less code than is possible using python built in sequences.

import numpy as np

# Array initialization
a = np.array([1,2,3,4])


np.zeroes((3,4))    
output: -> array([[0.,0.,0.,0.],
                  [0.,0.,0.,0.],
                  [0.,0.,0.,0.]
                  ])

np.zeroes((3,4))    
output: -> array([[1.,1.,1.,1.],
                  [1.,1.,1.,1.],
                  [1.,1.,1.,1.]
                  ])

np.random.random((3,4)) -> give random no. same array as like above have 

np.linspace(-10,10,10)  -> fixed length generate krega from starting range to end range 

array.ndim -> in 3d array (a,b,c) return krta hai jisme a-> kitne 2D Array hai , b -> kitne row , c-> kitne column 

array.itemsize()    

array.resshape()

array.dtype -> data type btata hai -> int32 , int64, float64

array.astype(np.int32)    -> convert kr diya hai dusre data type mai.

array+2 -> ye sab mai add hoga

# Sigmoid  -> 
def sigmoid(array):
    return 1/(1+np.exp(-(array)))

example: -> a = np.arrayrange(100)  -> ye array ki range hai kha tak chalega array
            sigmoid(a)



# Notes of Numpy


import numpy as np

# From lists
arr = np.array([1, 2, 3])
arr2d = np.array([[1,2],[3,4]])

# Special arrays
np.zeros((3,4))          # 3x4 zeros
np.ones((2,3))           # 2x3 ones
np.full((2,2), 7)        # 2x2 filled with 7
np.eye(5)                # Identity 5x5
np.empty((2,2))          # uninitialized

# Ranges
np.arange(0, 10, 2)      # [0,2,4,6,8]
np.linspace(0, 1, 5)     # [0, 0.25, 0.5, 0.75, 1]
np.logspace(0, 2, 5)     # log spaced

# Random arrays
np.random.rand(3,2)      # uniform [0,1)
np.random.randn(3,2)     # standard normal
np.random.randint(0,10, size=(3,3))
np.random.random((2,2))

# Repetition
np.tile([1,2], 3)        # [1,2,1,2,1,2]
np.repeat([1,2], 3)      # [1,1,1,2,2,2]


arr = np.array([[1,2,3],[4,5,6]])

arr.shape       # (2,3)
arr.size        # 6
arr.ndim        # 2
arr.dtype       # int64
arr.nbytes      # total bytes
arr.itemsize    # bytes per element
arr.T           # transpose

arr = np.array([10,20,30,40,50])
arr[1:4:2]          # [20,40]
arr[::-1]           # reverse

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[0,2]          # 3
arr2d[:2, 1:]       # [[2,3],[5,6]]
arr2d[1, :]         # row 1

# Boolean indexing
arr = np.array([1,2,3,4])
mask = arr > 2
arr[mask]           # [3,4]
arr[arr % 2 == 0]   # [2,4]

# Fancy indexing
arr[[0,2,3]]        # [1,3,4]
arr2d[[0,1], [1,2]] # [2,6] (0,1) and (1,2)


arr = np.arange(12)

# Reshape
arr.reshape(3,4)
arr.reshape(-1, 4)   # auto compute rows

# Flatten
arr.flatten()        # returns copy
arr.ravel()          # returns view (faster)

# Stacking
a = np.array([1,2])
b = np.array([3,4])
np.vstack((a,b))     # [[1,2],[3,4]]
np.hstack((a,b))     # [1,2,3,4]
np.column_stack((a,b))
np.stack((a,b), axis=1)

# Split
arr = np.arange(10)
np.split(arr, [3,7])  # [0-2],[3-6],[7-9]
np.vsplit(mat, 3)
np.hsplit(mat, 2)