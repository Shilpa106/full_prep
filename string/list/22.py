#  Convert list of tuples to list of list

# Last Updated : 27 Mar, 2019
# This is a quite simple problem but can have a good amount of application due to certain constraints of python language.
#  Because tuples are immutable, they are not easy to process whereas lists are always a better option while processing.
#  Let’s discuss certain ways in which we can convert a list of tuples to list of list.

# Method #1 : Using list comprehension
# This can easily be achieved using the list comprehension. We just iterate through each list converting the tuples to the list.

# The original list of tuples : [(1, 2), (3, 4), (5, 6)]
# The converted list of list : [[1, 2], [3, 4], [5, 6]]

tests= [(1, 2), (3, 4), (5, 6)]
n=[]
for i in tests:
    # print(i)
    # print(type(i))
    m=[]
    for j in i:
        print(j)
        m.append(j)
    n.append(m)
print(n)