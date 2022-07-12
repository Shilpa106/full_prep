from xmlrpc.client import Boolean
import numpy as np
list1=[0,1,2,3,4]
# print(list1)
arr1d=np.array(list1)
# print(arr1d)
list1.append(5)
# print(list1)
# print(arr1d+2)


list2=[[1,1,1],[2,2,2],[3,3,3]]
# arr2d=np.array(list2)
# print(arr2d)
# print(type(arr2d))
# print(arr2d.ndim)
# print(arr2d.shape)
# print(arr2d.dtype)
# print(arr2d.size)

arr2d=np.array(list2,dtype='float')
# print(arr2d)
# print(arr2d.astype('int'))
# print(arr2d.astype('str'))
list1.append('6')
# print(list1)
# print(arr2d)
# np2list=arr2d.tolist()
# print(np2list)

# print(arr2d.tostring())
# print(arr2d.tobytes())
# print(list2)
# print(arr2d)

arr2d =arr2d.astype('float')
# print(arr2d)

# print("shape",arr2d.shape)
# print("type",arr2d.dtype)

# print(arr2d.size)
# print(arr1d.size)
# print(arr1d.ndim)
# print(arr2d.ndim)

# print(arr1d)
# arr1d=arr1d*arr1d
# print(arr1d)

# print(arr1d[3])
# print("array2d",arr2d)
# print(arr2d[1][2])

# print(arr2d)
# Boolean=arr2d<3
# print(Boolean)
# print(arr2d[Boolean])

# print(arr2d)
# print(arr2d[::-1])

# print(arr2d[::-1,::-1])

# print(np.nan)
# print(np.inf)
# print(arr2d)
# print(arr2d[0][0])
arr2d[0][0]=np.nan
# print(arr2d)
arr2d[0][1]=np.inf
# print(arr2d)

missing_flag=np.isnan(arr2d)|np.isinf(arr2d)
# print(missing_flag)
# print(np.isnan(arr2d)|np.isinf(arr2d))

# Replace nan and inf with 0
# print(arr2d[missing_flag])
arr2d[missing_flag]=0
# print(arr2d)

# Stastical operations:
# print(arr2d)
# print(np.mean(arr2d,axis=1))
# print(np.max(arr2d,axis=0))
# print(np.min(arr2d,axis=0))
# print(np.min(arr2d,axis=1))
# print(np.var(arr2d,axis=1))
# print(np.sort(arr2d,axis=0))
# print(np.std(arr2d,axis=0))

print(arr2d)



