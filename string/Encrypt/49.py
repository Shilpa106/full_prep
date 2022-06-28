# Generate a Number in Decreasing order of Frequencies of characters of a given String

# Difficulty Level : Medium
# Last Updated : 25 Feb, 2022
# Given a string Str of length N, consisting of lowercase alphabets, the task is to generate a number in decreasing order of the frequency of characters in the given string. If two characters have the same frequency, the character with a smaller ASCII value appears first. Numbers assigned to characters {a, b, …., y, z} are {1, 2, …., 25, 26} respectively. 
# Note: For characters having values greater than 9 assigned to it, take its modulo 10.
# Examples: 

# Input: N = 6, Str = “aaabbd” 
# Output: 124 
# Explanation: 
# Given characters and their respective frequencies are: 

# a = 3
# b = 2
# d = 1
# Since the number needs to be generated in increasing order of their frequencies, the final generated number is 124.
# Input: N = 6, Str = “akkzzz” 
# Output: 611 
# Explanation: 
# Given characters and their respective frequencies are: 

# a = 1
# k = 2
# z = 3
# For z, value to assigned = 26 
# Hence, the corresponding digit assigned = 26 % 10 = 6 
# For k, value to assigned = 11 
# Hence, the corresponding digit assigned = 11 % 10 = 1 
# Since the number needs to be generated in increasing order of their frequencies, the final generated number is 611. 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: 
# Follow the steps below to solve the problem: 

# Initialize a Map and store the frequencies of each character.
# Traverse the Map and insert all {Character, Frequency} pairs in a vector of pair.
# Sort this vector in a way such that the pair with higher frequency appears first and among pairs having the same frequency, those with smaller ASCII value come first.
# Traverse this vector and find the digit corresponding to each character.
# Print the final number generated.