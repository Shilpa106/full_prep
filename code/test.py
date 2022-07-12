# # perimeter of a given hexagon


# def findPerimeterofhexagon(a):
#     return (6*a)

# side = 50
# print(findPerimeterofhexagon(side))

# ***************************************
# i/p:
# s = "Geeky"
# s = "Geeky"

# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         for k in range(i,j):
#             print(s[k], end=" ")
#         print()



# o/p:
# G
# Ge
# Gee
# Geek
# Geeky
# e
# ee
# eek
# eeky
# e
# ek
# eky
# k
# ky
# y

# ******************************************

# Print all subsequences of a string
# Input : abc
# Output : a, b, c, ab, bc, ac, abc

# Input : aaa
# Output : a, aa, aaa



s='abcd'
for i in range(len(s)):
    for j in range(len(s)+1):
        print(s[i:j])
        # for k in range(i,j):
        #     print(s[k], end=' ')
    print()
    



# o/p

# abcd
# abc
# abd
# ab
# acd
# ac
# ad
# a
# bcd
# bc
# bd
# b
# cd
# c
# d

# 1234
# 123
# 124
# 12
# 134
# 13
# 14
# 1
# 234
# 23
# 24
# 25
# 2
# 34
# 3
# 4