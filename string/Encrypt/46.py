# Sum and Product of Prime Frequencies of Characters in a String

# Last Updated : 20 Feb, 2022
# Given a string str containing only lowercase English alphabets, the task is to find the sum and product of all the prime frequencies of the characters in str.
# Examples: 
 

# Input: str = “geeksforgeeks” 
# Output: 6, 8 
# Only characters ‘g’, ‘k’ and ‘s’ have prime frequencies i.e. 2 + 2 + 2 = 6 and 2 * 2* 2 = 8 
 

# Character	frequency
# g	2
# e	4
# k	2
# s	2
# f	1
# o	1
# r	1
# Input: str = “algorithms” 
# Output: 0, 0 
 

 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
 
# Approach: 
 

# Traverse the string and store the frequencies of all the characters in a hash table.
# Find the frequencies which are prime using Sieve Of Eratosthenes.
# Calculate the sum and product of all of these prime frequencies and finally print the sum and product.
