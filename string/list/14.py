# Convert list of tuples to list of strings

# Last Updated : 26 Feb, 2019
# The interconversion between datatypes is quite useful utility and many articles have been written to perform the same. This article discusses the interconversion between a tuple of characters to individual strings. This kind of interconversion is useful in Machine Learning in which we need to give the input to train model in a specific format. Let's discuss certain ways in which this can be done.

# Method #1 : Using list comprehension + join()
# The list comprehension performs the task of iterating the entire list of tuples and join function performs the task of aggregating the elements of tuple into a one list.

# output
# The original list is : [('G', 'E', 'E', 'K', 'S'), ('F', 'O', 'R'), ('G', 'E', 'E', 'K', 'S')]
# The list after conversion to list of string : ['GEEKS', 'FOR', 'GEEKS']

tests=[('G', 'E', 'E', 'K', 'S'), ('F', 'O', 'R'), ('G', 'E', 'E', 'K', 'S')]
# print(tests)
t=[]
# s=''
for i in tests:
    # print(i)
    s=''
    for j in i:
        # print(j)
        s+=j
    t.append(s)
# print(s)
print(t)