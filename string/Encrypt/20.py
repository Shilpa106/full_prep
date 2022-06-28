# Check if frequency of character in one string is a factor or multiple of frequency of same character in other string

# Difficulty Level : Hard
# Last Updated : 30 Mar, 2022
# Given two strings, the task is to check whether the frequencies of a character(for each character) in one string are multiple or a factor in another string. If it is, then output “YES”, otherwise output “NO”.

# Examples: 

# Input: s1 = “aabccd”, s2 = “bbbaaaacc” 
# Output: YES 
# Frequency of ‘a’ in s1 and s2 are 2 and 4 respectively, and 2 is a factor of 4 
# Frequency of ‘b’ in s1 and s2 are 1 and 3 respectively, and 1 is a factor of 3 
# Frequency of ‘c’ in s1 and s2 are same hence it also satisfies. 
# Frequency of ‘d’ in s1 and s2 are 1 and 0 respectively, but 0 is a multiple of every number, hence satisfied. 
# Hence, the answer YES.

# Input: s1 = “hhdwjwqq”, s2 = “qwjdddhhh” 
# Output: NO

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach:  

# Store frequency of characters in s1 in first map STL.
# Store frequency of characters in s2 in second map STL.
# Let the frequency of a character in the first map be F1. Let us also assume the frequency of this character in the second map is F2.
# Check F1%F2 and F2%F1(modulo operation). If either of them is 0, then the condition is satisfied.
# Check it for all the characters.
# Below is the implementation of the above approach:


