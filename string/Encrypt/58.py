# Check whether the frequencies of all the characters in a string are prime or not

# Last Updated : 07 May, 2021
# Given a string str    , the task is to check if the frequencies of all the characters of the string are prime or not. If all the frequencies are prime then print Yes    otherwise print No    .
# Examples: 

# Input: str = “geeksforgeeks” 
# Output: No 
 

# Character	Frequency
# g	2
# e	4
# k	2
# s	2
# f	1
# o	1
# r	1
# It is clear that only the frequencies of g, k and s are prime.
# Input: str = “aabbbccccc” 
# Output: Yes 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
 
# Approach: Find the frequencies of all the characters present in the string and store them in a map. Then check whether all the frequencies are prime or not, if all the frequency are prime then print Yes    else No    .