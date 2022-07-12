

# Sorting array:There is a simple np.sort method for sorting NumPy arrays.

import numpy as np
a=np.array([[1,4,2],[3,4,6],[0,-1,5]])

# Sorted array
# print("Array element in sorted order",np.sort(a,axis=None))

# Sort array row-wise
# print("Row-wise sorted array:",np.sort(a,axis=1))

# Specific sort algorithm 
# print("Column wise sort by applying merge-sort:", np.sort(a,axis=0,kind='mergesort'))

# sorting of structured array set alias names for dtype .
dtypes=[('name','s10'),('grad_year',int),('cgpa',float)]
# print(dtypes)

# Values to be put in array
values=[('Hrithik',2009,8.5),('Ajay',2008,8.7),('Pankaj',2008,7.9),('Aakash',2009,9.0)]
# print(values) 

# Creating array
arr=np.array(values,dtype=dtypes)
# print("Array sorted by names:",np.sort(arr,order='name'))

print("Array sorted by graduation  year and then cgpa",np.sort(arr,order=['grad_year','cgpa']))

