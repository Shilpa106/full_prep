# Convert a string representation of list into list


# Many times, we come over the dumped data that is found in the string format and we require it to be represented into the actual list format in which
#  it was actually found. This kind of problem of converting a list represented in string format back to list to perform tasks are quite common in web development.
#  Let’s discuss certain ways in which this can be performed.

# Method #1: Using split() and strip()

# initial string [1, 2, 3, 4, 5]
# <class 'str'>
# final list ['1', '2', '3', '4', '5']
# <class 'list'>
tests=[1, 2, 3, 4, 5]
res=[]
for i in tests:
    # print(i)
    res.append(str(i))
print(res)