

# program to demonstrate accessing of Counter elements
from collections import Counter
# z=['blue','red','blue','yellow','blue','red']
# col_count=Counter(z)
# print(col_count['blue'])
# col=['blue','red','yellow','green']
# for color in col:
#     print(color,col_count[color])



# # elements
# coun=Counter(a=1,b=2,c=3)
# print(coun)
# print(coun.elements())
# print(list(coun.elements()))


# most_common() :
# coun=Counter(a=1,b=2,c=3,d=120,e=1,f=219)
# # prints 3 most frequent characters 
# for letter,count in coun.most_common(3):
#     print('%s:%d' % (letter,count))

# # WITH SEQUENCE OF ITEMS
# print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# # WITH DICTIONARY
# print(Counter({'A':3,'B':5,'C':2}))

# # WITH KEYWORD ARGS
# print(Counter(A=3,B=5,C=2))

# ex
# coun=Counter()
# coun.update([1,2,3,1,2,1,1,2])
# print(coun)

# coun.update([1,2,4])
# print(coun)

# # ex: program to demonstrate that counts in
# # Counter can be 0 and negative

# c1=Counter(A=4,B=3,C=10)
# c2=Counter(A=10,B=3,C=4)
# c1.subtract(c2)
# print(c1)


#  ex
# from collections import Counter
# x=Counter('geeksforgeeks')
# # print(x.elements)
# for i in x.elements():
#     print(i)


# Code #2: Elements on a variety of Counter Objects with different data-containers  


# a=Counter('geeksforgeeks')
# for i in a.elements():
#     print(i, end='')
# print()

# # ex2
# b=Counter({'geeks':4, 'for':1,'gfg':2,'python':3})

# # print(b.elements())
# for i in b.elements():
#     print(i, end='')
# print()

# c=Counter([1,2,21,12,2,44,5,13,15,5,19,21,5])
# for i in c.elements():
#     print(i, end='')
# print()

# # ex4
# d=Counter(a=2,b=3,c=6,d=1,e=5)
# for i in d.elements():
#     print(i, end='')


# x = Counter ("geeksforgeeks")
 
# # will return a itertools chain object
# # which is basically a pseudo iterable container whose
# # elements can be used when called with a iterable tool
# print(x.elements())



# # ex4
# x = Counter (a = 2, x = 3, b = 3, z = 1, y = 5, c = 0, d = -3)
 
# # printing out the elements
# for i in x.elements():
#     print( "% s : % s" % (i, x[i]), end ="\n")


