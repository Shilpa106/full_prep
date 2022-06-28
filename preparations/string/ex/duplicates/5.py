# Check if string is palindrome after removing all consecutive duplicates

# Given a string str, the task is to remove all the consecutive duplicates from the string str and check if the final string is palindrome or not.
# Print “Yes” if it is a palindromic else print “No”.
# Examples: 
 

# Input: str = “abbcbbbaaa” 
# Output: Yes 
# Explanation: 
# On removing all consecutive duplicates characters, the string becomes “abcba” which is a palindrome.
# Input: str = “aaabbbaaccc” 
# Output: No 
# Explanation: 
# On removing all consecutive duplicates characters, the string becomes “abac” which is not a palindrome. 
 

str = "abbcbbbaaa" 
li=list(str)
# d=[]
for i in range(len(li)):
    if str[i] == str[i+1]:
        str.remove(str[i])
#     # if i not in d:
#         d.append(i)
# print(d)
print(str)

# print(str[0:len(li)])
# if d[0:len(str)]
