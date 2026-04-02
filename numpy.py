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

# 
np.zeroes((3,4))
output: -> array([[0.,0.,0.,0.],
                  [0.,0.,0.,0.],
                  [0.,0.,0.,0.]
                  ])
