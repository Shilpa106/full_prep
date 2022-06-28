
import numpy as np
my_3d_array=np.arange(0,70)
# print(my_3d_array)
# print(my_3d_array.shape)
my_3d_array.shape=(2,7,5)
# print(my_3d_array)

# shape
# print(my_3d_array.shape)

# no of dimensions
# print(my_3d_array.ndim)

# size ,no of elements
# print(my_3d_array.size)
# print(my_3d_array.dtype)

# print(5*my_3d_array-3)

# left_mat=np.arange(6).reshape((2,3))
# # print(left_mat)
# right_mat=np.arange(15).reshape((3,5))
# print(right_mat)
# print(np.dot(left_mat, right_mat))

# print(np.inner(left_mat, right_mat)) #wrong way


# Operations along asis:
# print(my_3d_array)
# print(my_3d_array.shape)
# print(my_3d_array.sum())

# print((69*70)/2)
# print(my_3d_array)
# print(my_3d_array.sum(axis=0))
# print(my_3d_array.sum(axis=1))
# print(my_3d_array.sum(axis=2))

# # Broadcast rules
# my_2d_array=np.ones(35,dtype='int').reshape((7,5))*3
# print(my_2d_array)

my_random_2d_array=np.random.random((7,5))
# print(my_random_2d_array)
# # print(np.set_printoptions(precision=4))

# print(my_3d_array)
# print(my_3d_array*my_random_2d_array)

my_vector=np.arange(5)*7
# print(my_vector)
# my_vector[0]=-1
# print(my_vector)

# print(my_3d_array/my_vector)
# print(my_3d_array%my_vector)

# Creating structured array
person_data_def=[('name','56'),('height','f8'),('weight','f8'),('age','18')]
# print(person_data_def)

people_array=np.zeros((4))
print(people_array)
