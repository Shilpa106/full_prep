# Different ways of sorting Dictionary by Keys and Reverse sorting by keys

# my_dict={'c':3,'a':1,'d':4,'b':2}
# # print(my_dict)

# # sorting dictionary
# sorted_dict=my_dict.keys()
# print(sorted_dict)
# sorted_dict1=sorted(sorted_dict)
# # print(sorted_dict1)
# for key in sorted_dict1:
#     print(key, ':', my_dict[key])



# my_dict = {2: 'three', 1: 'two', 4: 'five', 3: 'four'}
# print(my_dict.items())
# sorted_dict = sorted(my_dict.items())
# print(sorted_dict)
# for k,v in sorted_dict:
#     print(k,v)

# M2
# sorted_dict = sorted(my_dict.keys())
# print(sorted_dict)

# my_dict = {'red': '#FF0000', 'green': '#008000',
#            'black': '#000000', 'white': '#FFFFFF'}

# sorted_dict=dict(sorted(my_dict.items()))
# # print(sorted_dict)
# for elem in sorted(sorted_dict.items()):
#     # print(elem)
#     print(elem[0], " ::", elem[1])


# # Initialising a dictionary
# my_dict = {'a': 23, 'g': 67, 'e': 12, 45: 90}

# # Sorting dictionary using lambda function
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])

# # Printing sorted dictionary
# print("Sorted dictionary using lambda is : ", sorted_dict)



# # json
# import json
# my_dict={"b":2,"c":3,"a":1,"d":4}
# print(my_dict)
# print("Sorted dictionary is :", json.dumps(my_dict,sort_keys=True))

# pprint 

# import pprint 
# my_dict ={1:2,3:4,4:3,2:1,0:0}
# print("Sorted dictionary is:")
# pprint.pprint(my_dict)


# ordered_dict 
# my_dict={"b":2, "c":3,"a":1, "d":4}
# from collections import OrderedDict
# sorted_dict=OrderedDict(sorted(my_dict.items()))
# # sorted_dict=sorted(my_dict.items())
# print(sorted_dict)

# # sorteddict
# from sortedcontainers import SortedDict
# my_dict={"b":2, "c":3,"a":1, "d":4}
# sorted_dict=SortedDict(my_dict)
# print(sorted_dict)

# # Using class and function
# # Examples:

# # Input:
# # {"b": 2, "c": 3, "a": 1,"d":4}

# # Output:
# # {"a": 1, "b": 2, "c": 3,"d":4}

# class SortedDisplayDict(dict):
#     def __str__(self):
#         return "{" + ",".join("%r: %r" % (key,self[key]) for key in sorted(self)) + "}"

# my_dict=SortedDisplayDict({"b": 2, "c": 3, "a": 1,"d":4})
# print(my_dict)

# Reverse sorting dictionary by keys
# Examples:

# Input:
my_dict = {"b": 2, "c": 3, "a": 1,"d":4}

# Output:
# Sorted dictionary is :
# ['a','b','c','d']

sorted_dict=sorted(my_dict,reverse=True)
print("Sorted dictionary is : ")
for k in sorted_dict:
    print(k,':',my_dict[k])




