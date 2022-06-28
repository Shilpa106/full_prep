
# # Creating a numpy array
# import numpy as np

# # Creating a rank 1 array
# arr=np.array([1,2,3])
# print("Array with Rank 1: \n",arr)
# print(type(arr))

# # Creating a rank 2 array
# arr=np.array([[1,2,3],[4,5,6]])
# print("Array with Rank 2: \n",arr)

# # Creating an array from tuple
# arr=np.array((1,3,2))
# print("Array created using passed tuple:\n",arr)


# Accessing the array index
import numpy as np

# # Initial Array 
arr=np.array([[-1,2,0,4],[4,-0.5,6,10],[2.6,9,7,8],[3,-7,4,2.0]])
# # print("initial array: ",arr)

# # range of array with the use of slice method
# # print(arr[0,0])
# # print(arr[0,1])
# # print(arr[0,2])
# # print(arr[1,1])
# sliced_arr=arr[:2,::2]
# print("Array with first 2 rows and alternate columns(0 and 2):\n",sliced_arr)

# printing elements at specific indices
index_arr=arr[[1,1,0,3],[3,2,1,0]]
print("\nElements at indices (1,3),(1,2),(0,1),(3,0):\n",index_arr)






# n='shilpayadav'
# print(n[::2])
# print(n[:2])
