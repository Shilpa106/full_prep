# Python program to convert a list of strings with a delimiter to a list of tuple


# Given a List containing strings with a particular delimiter. The task is to remove the delimiter and convert the string to the list of tuple.

# Examples:

# Input : test_list = ["1-2", "3-4-8-9"], K = "-" 
# Output : [(1, 2), (3, 4, 8, 9)] 
# Explanation : After splitting, 1-2 => (1, 2).
 

# Input : test_list = ["1*2", "3*4*8*9"], K = "*" 
# Output : [(1, 2), (3, 4, 8, 9)] 
# Explanation : After splitting, 1*2 => (1, 2). 

test_list = ["1-2", "3-4-8-9"]
K = "-" 
l=[]
for i in test_list:
    m=i.replace(K,",")
    j=eval(m)
    l.append(j)
print(l)