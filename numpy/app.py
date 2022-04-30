from math import dist
import numpy as np
from numpy import random, size

import seaborn as sb
import matplotlib.pyplot as plt

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(arr.dtype)
# print(arr.ndim)
# print(np.__version__)
# print(type(arr))

a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
# print(a.ndim)
b = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 8, 6]]])
# print(b)
# print(b.ndim)

# print(a[0][1])  #or print(a[0,1]) both are same , negative indexing is also allowed

# print(b[0,0,2]) # or print(b[0][0][2]) both are same print(b[-1][-1][-2])

# print(b[1, :2])

# print(b.dtype)


# x = arr.copy()
# arr[0] = 9
# print(x)
# print(arr)

# x = arr.view()
# arr[0] = 9
# print(x)
# print(arr)


# print(arr.reshape(2,3,2))

# for i in np.nditer(b):
#     print(i)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)

r = int(random.rand() * 1000)
# print(r)


# r1 = random.randint(100, size=5)
# print(r1)

# r2 = random.rand(5)
# print(r2)

r3 = random.choice([2, 3, 4, 5], p=[0.1, 0.2, 0.7, 0.0], size=(3, 5))
# print(r3)

# random.shuffle(arr)   # this makes changes in the original array itself
# print(arr)


# returns a re-arranged array (and leaves the original array un-changed)
r4 = random.permutation(arr)
# print(r4)
# print(arr)


# sb.distplot(arr)  #seaborn module
# plt.show()

#normal distribution
# x = random.normal(loc = 1, scale= 2, size=5)
# print(x)

#binomial distribution
# sb.distplot(random.binomial(n= 10, p = 0.5, size=1000), hist=True, kde=False)
# sb.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
# sb.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
# sb.distplot(random.poisson(lam=2, size=1000), kde=False)
# plt.show()

def myadd(x, y):
    return x+y

temp = np.frompyfunc(myadd, 2,1)

print(temp([1,2,3],[4,5,6]))