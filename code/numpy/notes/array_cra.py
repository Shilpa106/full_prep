
import numpy as np
# print(np.__version__)

# mylist=[-17,0,4,5,9]
# print(mylist*6)
# mylist=[-1,0,4,5,9]
# # print(mylist)
# my_array_from_list=np.array(mylist)
# # print(my_array_from_list)

# print(my_array_from_list*10)

# my_tuple=(14,-3.54,5+7j)
# my_tuple=(14,-3.54,5)
# print(np.array(my_tuple))
# print(my_tuple*6)
# print(np.array(my_tuple)*6)


# intrinsic numpy array creations

# print(np.arange(7))

# print(np.arange(20,23))

# print(len(np.arange(10,23)))

# my_range_array=np.arange(10,23)
# print(my_range_array.size)

# print(np.arange(10,23).size)

# print(np.arange(10,23,5))

# print(np.arange(10,26,5))

# print(np.arange(26, step=5))

# print(np.arange(1,26, step=5))

# linespace(), zeros(), ones(), and numpy DI.
# print(np.linspace(5,15,9))
# my_linspace=np.linspace(5,15,9,retstep=True)
# print(my_linspace)

# zeros() function
# print(np.zeros(5))


# Ones Function
# print(np.ones(7))

# print(np.zeros(4))
# print(np.zeros(5))
# print(np.zeros((5,4)))
# print(np.zeros((5,4,3)))
# print(np.zeros(11,dtype='int64'))

# numpy indexing slicing arrays boolean mask arrays
# slicing array
my_vector=np.array([-17,-4,0,2,21,37,105])
# print(my_vector)
# print(my_vector[0])
# print(my_vector[-3])
# print(my_vector[305%7])
my_vector[0]=102
# print(my_vector)
# print(my_vector[1])
# print(my_vector.size)
# print(my_vector[305%my_vector.size])



