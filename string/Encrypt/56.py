# Last remaining character after repeated removal of the first character and flipping of characters of a Binary String

# Difficulty Level : Basic
# Last Updated : 06 May, 2021
# Given a Binary string str of length N, the task is to find the last character removed from the string by repeatedly removing the first character of the string and flipping all the characters of the string if the removed character is ‘0’.

# Examples:

# Input: str = “1001” 
# Output: ‘0’ 
# Explanation: 
# Removing str[0] from the string modifies str to “001”. 
# Removing str[0] from the string modifies str to “10”. 
# Removing str[0] from the string modifies str to “0”. 
# Since the last character removed was ‘0’, the required output is ‘0’.

# Input: str = “10010” 
# Output: ‘0’

# Naive Approach: The simplest approach to solve this problem is to iterate over the characters of the string. For every character encountered, remove the first character of the string and check if the removed character was ‘0’ or not. If found to be true, then flip all the characters of the string. Finally, print the character which was removed in the last iteration. Follow the steps below to solve the problem: 

# Time Complexity: O(N2) 
# Auxiliary Space: O(1)

# Efficient Approach: The above approach can be optimized based on the following observation:

# Case 1: 
# Suppose str = “XXXXXXX0X”, where X is either ‘0’ or ‘1’. 
# If the character str[N – 2] is flipped, then str[N – 1] must be flipped. 
# Therefore, if str[N – 2] is ‘0’, then last removed character will be (‘1’ – str[N – 1] + ‘0’).
# Case 2: 
# Suppose str = “XXXXXXX1X”, where X is either ‘0’ or ‘1. 
# If the character str[N – 2] is flipped, then str[N – 1] must be flipped. 
# Therefore, if str[N – 2] is ‘1’, then the last removed character will be str[N – 1]. 
 

# Follow the steps below to solve the problem:

# If N is equal to 1 then answer is str[0] itself, Otherwise. 
# Check if str[N – 2] (For N>=2) is ‘1’ or not. If found to be true, then print str[N – 1].
# Otherwise, print (‘1’ –  str[N – 1] + ‘0’).