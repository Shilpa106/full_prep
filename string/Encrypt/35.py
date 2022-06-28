# Character whose frequency is equal to the sum of frequencies of other characters of the given string

# Difficulty Level : Easy
# Last Updated : 22 Mar, 2021
# Given a string str consisting of lowercase English alphabets. The task is to find whether there is any character in the string whose frequency is equal to the sum of the frequencies of other characters of the string. If such character exists then print Yes else print No.
# Examples: 
 

# Input: str = “hkklkwwwww” 
# Output: Yes 
# frequency(w) = frequency(h) + frequency(k) + frequency(l) 
# 4 = 1 + 2 + 1 
# 4 = 4
# Input: str = “geeksforgeeks” 
# Output: No 
 

 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: If the length of the string is odd then the result will always be No. In case of even length string, calculate the frequency of each of the character of the string and for any character if it’s frequency = half of the length of the string then the result will be Yes else No.