# Sum of frequencies of characters of a string present in another string

# Difficulty Level : Medium
# Last Updated : 14 May, 2021
# Given two strings S1 and S2 of lengths M and N respectively, the task is to calculate the sum of the frequencies of the characters of string S1 in the string S2.

# Examples:

# Input: S1 = “pPKf”, S2 = “KKKttsdppfP”
# Output: 7
# Explanation:
# The character ‘p’ occurs twice in the string S2.
# The character ‘P’ occurs once in the string S2.
# The character ‘K’ occurs thrice in the string S2.
# The character ‘f’ occurs once in the string S2.
# Therefore, in total, characters of the string S1 occurs 7 times in the string S2.

# Input: S1 = “geEksFOR”, S2 = “GeEksforgeEKS”
# Output: 7

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Naive Approach: The simplest approach is to iterate over each character of the string S1, count its frequency in the string S2. 

# Time Complexity: O(N2)
# Auxiliary Space: O(1)

# Efficient Approach: The above approach can be optimized by using Hashing. Follow the steps below to solve the problem:

# Initialize an integer count to store the required sum.
# Insert all the characters of string S1 in a Set, say bset.
# Iterate over characters of the string S2 and check if the current character is present in the set, bset, or not. If found to be true, then increment count by one.
# After completing the above steps, print the value of count as the result.
