# Test if dictionary contains unique keys and values
# Method #1 : Using loops
from matplotlib.pyplot import flag


test_dict = {'Manjeet' : 1, 'Akash' : 2, 'Akshat' : 3, 'Nikhil' : 1}
# flag=False
# hash_val=dict()
# for keys in test_dict:
#     if test_dict[keys] in hash_val:
#         print(test_dict[keys],hash_val)
#         flag=True
#         break
#     else:
#         hash_val[test_dict[keys]]=1
# print(flag)


# Method #2 : Using len() + set() + values()
flag=len(test_dict)!=len(set(test_dict.values()))
print(flag)
