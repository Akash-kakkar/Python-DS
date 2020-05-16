#What is difference between aggregate function and universal function in numpy?
# 
#Aggregate functions :- are used to perform some statistical data analysis.
# 
#ufuncs stands for "Universal Functions" :- and they are NumPy functions that operates on the #ndarray object.
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.

#Aggregate function

import numpy as np
a = np.array([10, 20, 30])
np.median(a)

# ufunc

import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
z




