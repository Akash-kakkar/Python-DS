#When does operation between two uneven ndarray support in numpy and how?
# 
'''If the arrays have different shapes, then the element-by-element operation is not possible. But, in real-world applications, you will rarely come across arrays that have the same shape. So Numpy also provides the ability to do arithmetic operations on arrays with different shapes. That ability is called broadcasting.

Although you can do arithmetic operations on arrays with wide-ranging shapes, there are a few limitations. So, it helps us to know the broadcasting rules before we look at a few examples. In general, you can do arithmetic operations between two arrays of different shapes, if:
 
The size of each dimension is the same, or
The size of one of the dimensions is one And you can use these rules to perform operations even between a ten-dimensional array and a two-dimensional array. The dimensionality of the arrays does not matter.'''

import numpy as np

A = np.arange(4)
B = np.arange(12).reshape(3, 4)
A + B




