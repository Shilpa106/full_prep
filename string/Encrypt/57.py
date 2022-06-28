# XOR of Prime Frequencies of Characters in a String

# Last Updated : 11 May, 2021
# Given a string containing only lowercase english alphabets. The task is to find the bitwise XOR of all the prime frequencies of the characters in the string. If no prime frequency is present, then print -1.
# Examples: 
 

# Input : str = "gggggeeekkkks"
# Output : 6

# Input : str = "aabbbbw"
# Output : -1
 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: 
 

# Traverse the string and store the frequencies of all the characters using map STL.
# Find the frequencies which are prime numbers using Sieve Of Eratosthenes.
# Calculate XOR of all these prime frequencies.
