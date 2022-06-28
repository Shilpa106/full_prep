# Convert list of strings to list of tuples

# Last Updated : 29 Apr, 2019
# Sometimes we deal with different types of data types and we require to inter convert from one data type to another and hence inter conversion always a useful tool to have knowledge about. The interconversion from tuples to other formats have been discussed earlier. This article deals with the converse case. Let’s discuss certain ways in which this can be done.

# Method #1 : Using map() + split() + tuple()

# This task can be achieved using the combination of these functions. The map function can be used to link the logic to each string, split function is used to split the inner contents of list to different tuple attributes and tuple function performs the task of forming a tuple.

# Output :
# The original list : ['4, 1', '3, 2', '5, 3']
# The list after conversion to tuple list : [(4, 1), (3, 2), (5, 3)]


# notes
# res = tuple(map(int, test_str.split(', ')))

# Convert String to Tuple
# Using eval()
# res = eval(test_str)

test_list= ['4, 1', '3, 2', '5, 3']
# print(tuple(test_list))
t=[]
for i in test_list:
    # print(eval(i))
    t.append(eval(i))
print(t)

