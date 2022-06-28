#  Split dictionary keys and values into separate lists

# Method #1: Using built-in functions
ini_dict={'a':'akshat','b':'bhuvan','c':'chandan'}
# print(ini_dict)
# keys=ini_dict.keys()
# values=ini_dict.values()
# print(keys)
# print(values)

# # Method #2: Using zip()
# keys,values = zip(*ini_dict.items())
# print(keys)
# print(values)


# Method #3: Using items()
# keys=[]
# values=[]
# items=ini_dict.items()
# for item in items:
#     keys.append(item[0]), values.append(item[1])

# print(keys)
# print(values)