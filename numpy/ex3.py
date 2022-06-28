import numpy as np

# Creating array object
# arr=np.array([[1,2,3],[4,2,5]])
# print(type(arr))

# printing array dimensions(axes)
# print(arr.ndim)

# Printing shape of array 
# print(arr.shape)

# Printing size total no of elements in array.
# print(arr.size)

# printing type of elements in array
# print(arr.dtype)


# array creation techniques

import numpy as np
# a=np.array([[1,2,4],[5,8,7]],dtype='float')
# print("Array created using passed list",a)

# Creating array from tuple
# b=np.array((1,3,2))
# print("Array created using passed tuple:",b)

# Creating a 3*4 array with all zeros
# c=np.zeros((3,4))
# print("Array initialized with all zeros",c)

# Create a constant value array of complex type
# d=np.full((3,3),6, dtype='complex')
# print("Array initialized with all 6s where array type is complex",d)

# create an array with random values
# e=np.random.random((2,2))
# print("A random array",e)

# create a sequence of integers from 0 to 30 with steps of 5
# f=np.arange(0,30,5)
# print("A sequential array with steps of 5",f)

# create a sequence of 10 values in range 0 to 5
# g=np.linspace(0,5,10)
# print("A sequential array with 10 vlaues between 0 and 5 ",g)

# Reshaping 3*4 array to 2*2*3 array
# arr=np.array([[1,2,3,4],[5,2,4,2],[1,2,0,1]])
# newarr=arr.reshape(2,2,3)
# print("Original array:",arr)
# print("Reshaped array:",newarr)

# # Flatten array
# arr=np.array([[1,2,3], [4,5,6]])
# flarr=arr.flatten()
# print("original array",arr)
# print("flattened array",flarr)

# Array indexing in numpy arrays
import numpy as np

# An example array
# arr=np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])

# # Slicing array
# temp=arr[:2,::2]
# print("Array with first 2 row and alternate column:",temp)

# integer array with indexing example
# temp=arr[[0,1,2,3],[3,2,1,0]]
# print("Element at indices (0,3),(1,2),(2,1),(3,0):", temp)

# boolean array indexing example
# cond=arr>0# cond is a boolean array
# # print(cond)
# temp=arr[cond]
# print('Element greater than 0',temp)


# Basic operations
# Operations on single array:
import numpy as np
a=np.array([1,2,5,3])

# add 1 to every element
# print("Adding 1 to every element:",a+1)

# # substract 3 from each element
# print("Subtracting 3 from each element:",a-3)

# Multiply each element by 10
# print("Multiplying each element by 10:",a*10)

# Square each element 
# print("Squaring each element:",a**2)

# modify existing arrays
# a*=2
# print("doubled each element of original array:",a)

# transpose of array
# a=np.array([[1,2,3],[3,4,5],[9,6,10]])
# print("Original array:",a)
# print("Transposed array:",a.T)


# Unary ooperators in numpy
import numpy as np
# arr=np.array([[1,5,6],[4,7,2],[3,1,9]])

# maximum element of array
# print("largest element is:", arr.max())
# print("Row wise maximum element is:", arr.max(axis=1))

# Minimum element of array
# print("Column wise minimum element is:", arr.min(axis=0))

# Sum of array elements
# print("Sum of all array elements:", arr.sum())

# cumulative sum along each row
# print("Cumulative sum along each row:", arr.cumsum(axis=1))

# Binary operators in numpy
# a=np.array([[1,2],[3,4]])
# b=np.array([[4,3],[2,1]])

# Add arrays
# print("Array sum:",a+b)

# print("Array multiplication:",a*b)

# matrix multiplication

# print("Matrix multiplication:",a.dot(b))


# All the operations we did above using overloaded operators can be done using ufuncs like np.add, np.subtract, np.multiply, np.divide, np.sum, etc. 
# Universal function(np.ufunc)

# Create an array of sine values 
# a=np.array([0,np.pi/2,np.pi])
# print("since values of array elements:",np.sin(a))

# Exponential values
a=np.array([0,1,2,3])
# print("Exponent of array elements:",np.exp(a))

# Square root of array vlaues
# print("Square root of array elements:",np.sqrt(a))




