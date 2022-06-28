# Given a string S, check if it is palindrome or not.

# Example 1:

# Input: S = "abba"
# Output: 1
# Explanation: S is a palindrome
# Example 2:

# Input: S = "abc" 
# Output: 0
# Explanation: S is not a palindrome

# 1
# S = "abba"
# print(S)
# print(S[::-1])
# if S== S[::-1]:
#     print("is palindrome")
# else:
#     print('is not palindrome')



# 2
# def isPalindrome(s):
#     return s==s[::-1]

# s='malayalam'
# ans=isPalindrome(s)
# if ans:
#     print('yes')
# else:
#     print('no')

# function to check string is
# palindrome or not
# def isPalindrome(str):

# 	# Run loop from 0 to len/2
# 	for i in range(0, int(len(str)/2)):
# 		if str[i] != str[len(str)-i-1]:
            
# 			return False
# 	return True

# main function
s = "malayalam"
# ans = isPalindrome(s)

for i in range(0, int(len(str)/2)):
    if str[i] != str[len(str)-i-1]:
        print(str[len(str)-i-1])

# if (ans):
# 	print("Yes")
# else:
# 	print("No")

    


