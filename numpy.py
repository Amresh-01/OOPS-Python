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

