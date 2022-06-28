# Remove all consecutive duplicates from the string

# Difficulty Level : Easy

# Given a string S, remove all the consecutive duplicates. Note that this problem is different from Recursively remove all adjacent duplicates. Here we keep one character and remove all subsequent same characters.

# Examples: 

# Input  : aaaaabbbbbb
# Output : ab

# Input : geeksforgeeks
# Output : geksforgeks

# Input : aabccba
# Output : abcba

s='aaaaabbbbbb'
# print(s)
li=list(s)
# print(li)
for i in range(len(li)+1):
    # print(i)
    # print(len(li))
    # print(li[i])
    if li[i-1]==li[i]:
        # print(li[i])
        li.remove(li[i])
        print(li)