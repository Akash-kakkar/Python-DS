

import numpy as np


# Make a ndarray by using np.arange(120), reshape it into shape of (2,3,4,5) and do the following operation on this new ndarray:
a = np.arange(120).reshape(2, 3, 4, 5)

# 1. Access the value 91 using indexing.
a[1, 1, 2, 1]

# 2. obtain a range of value 35-39 from this ndarray.
np.where(np.logical_and(a>=35, a<=39))

# 3. Make another 1D array from this having values 0 and all multiples of 5.
for i in range(a.shape[-1]):
    if i%5 == 0 and i == 0:
        print(a[...,i].reshape(24))

# 4. obtain mean values on axis-3 elements.
def aim(x):
    yield x/2

np.apply_along_axis(np.mean, axis=3, arr=a)


# Make a numpy ndarray np.linspace(5,20,24), and reshape into shape of (4,6).
 


b = np.linspace(5, 20, 24).reshape(4, 6)
b

#1. Split and stack to make array of shape (4,4) such that it contain elements of first, second ,fourth and sixth column.
np.split(b, 4)
[A, B, C, D] = np.split(b, [1, 2, 4], axis=1)

A

B

C

D

#2. Split and stack to make array of shape (2,2) such that it contain elements of first and fourth row and third and fifth column.
np.split(b, 2)
[E, F, G, H] = np.split(b, [1, 3, 4], axis=1)

E

F

G

H


#Plot a function of log2 and straight line $y = 0.5x - 1$ using matplotlib and find out approximate value at which they intersect. Make sure you have legend in the figure naming the curve.

from matplotlib import pyplot as plt

plt.style.use("ggplot")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = np.log(x)/np.log(2)
plt.plot(x, y, linewidth=4, label="log2(x)")


p = np.linspace(1, 10, 10, dtype=int)
y = 0.5 * p - 1
plt.plot(p, y, linewidth=4, linestyle='--', label="y = (0.5*p -1)")


plt.legend(fontsize='large')

print('intersection point = (8, 3) {approx.}')


