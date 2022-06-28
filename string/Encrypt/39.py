# Modify string by sorting characters after removal of characters whose frequency is not equal to power of 2

# Last Updated : 21 Jun, 2022
# Given a string S consisting of N lowercase alphabets, the task is to remove the characters from the string whose frequency is not a power of 2 and then sort the string in ascending order.

# Examples:

# Input: S = “aaacbb”
# Output: bbc
# Explanation: The frequencies of ‘a’, ‘b’, and ‘c’ in the given string are 3, 2, 1. Only the character ‘a’ has frequency (= 3) which is not a power of 2. Therefore, removing ‘a’ from the string S modifies it to “cbb”. Therefore, the modified string after sorting is “bbc”.

# Input: S = “geeksforgeeks”
# Output: eeeefggkkorss

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: The given problem can be solved by using Hashing. Follow the steps below to solve the given problem:

# Initialize an auxiliary array of size 26, say freq[], to store the frequency of each character in the string S such that index 0 represents character ‘a’, 1 represents the character ‘b’, and so on.
# Traverse the given string S and increment the frequency of each character S[i] by 1 in the array freq[].
# Traverse the array freq[] and if the value of freq[i] is a power of 2, then print the character (‘a’ + i), freq[i] number of times.