# Print all characters of string whose frequency is a power of K

# Last Updated : 13 Dec, 2021
# Given string str of size N, the task is to print the characters of string whose frequency is a power of K in a lexicographically sorted order.

# Examples:

# Input: str = “aaacbb” K = 2
# Output: bbc
# Explanation: Frequency of a is 3 which is not the power of 2. Frequency of c is 1 and frequency of b is 2 which are the power of 2. 

# Input: str = “geeksgeekgeeks” K = 3
# Output: eeeeeegggkkk

 
# Naive Approach: The idea is to count frequency for every alphabet of the string, if the frequency is the power of K then add it to a new string. Sort the string and print it.

# Time Complexity: O(N2)
# Auxiliary Space: O(N)

# Efficient Approach: The idea is to use Hashing. Below are the steps:

# Traverse the string and store the frequency of each alphabet in a Map
# Traverse the map and print the alphabets whose frequency is the power of K
