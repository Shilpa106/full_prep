# Kth character after replacing each character of String by its frequency exactly X times

# Difficulty Level : Easy
# Last Updated : 06 Sep, 2021
# Given a string S consisting of N digits from [1, 9] and a positive integer K and X. Every day each character of the string is replaced by its frequency and value. The task is to find the Kth character of the string after X days.

# Examples:

# Input: S = “1214”, K = 10, X = 3
# Output: 4
# Explanation:
# 1st day = “12214444”
# 2nd day = “1222214444444444444444”
# 3rd day = “122222222444444444444444444444444444444444444444444444444” 
# So, 10th character after 3rd day is 4.

# Input: S =”123″, K = 6, X = 2 
# Output: 3

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Naive Approach: The simplest approach to solve the problem is to create the string by appending the digits in the string digitX times and find the Kth character of the string.

# Time Complexity: O(∑digit[i]X) for i in range [0, N-1]

# Efficient Approach: The above approach can be optimized further by instead of creating a string add digitX to the sum and check if sum > K. Follow the steps below to solve the problem:

# Initialize a variable, say sum that stores the sum of the character of the string after X days.
# Initialize a variable, say ans that stores the Kth characters after X days.
# Iterate in the range [0, N-1] and perform the following steps:
# Initialize a variable say range as (S[i] – ‘0’)X and add it to the variable sum.
# If sum>=K, return S, modify ans as S[i], and terminate the loop.
# Print the value of ans as the answer.
