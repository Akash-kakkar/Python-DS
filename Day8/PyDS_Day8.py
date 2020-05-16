#What is difference between vstack and hstack method?
# 
#Horizontal Stack
# 
# With hstack you can appened data horizontally.
# 
# Vertical Stack
# 
# With vstack you can appened data vertically.

# Horizontal Stack

import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])

print('Horizontal Append:', np.hstack((f, g)))

# Vertical Stack

import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])

print('Vertical Append:', np.vstack((f, g)))

