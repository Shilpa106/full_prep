# Queries to count frequencies of a given character in a given range of indices

# Difficulty Level : Medium
# Last Updated : 02 Feb, 2022
# Given a string S of length N and an array Q[][] of queries in the form {l, r, y}. For each query, the task is to print the number of characters y present in the range [l, r].

# Examples:

# Input: S = “aabv”, Q[][] = {{0, 3, ‘a’}, {1, 2, ‘b’}}
# Output: 2 1
# Explanation:
# Query 1: Number of character ‘a’ present in the range [0, 3] is 2.
# Query 2: Number of character ‘b’ present in the range [1, 2] is 1.

# Input: S = “abcd”, Q[][] = {{1, 3, ‘c’}, {1, 1, ‘b’}}
# Output: 1 1
# Explanation:
# Query 1: Number of character ‘c’ present in the range [1, 3] is 1.
# Query 2: Number of character ‘b’ present in the range [1, 1] is 1.

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Naive Approach: The simplest approach is to traverse the string over the range [l, r] and increment the counter by 1 if the character at index i is equal to y for each query {l, r, y}. After traversing, print the counter for each query. 

# Time Complexity: O(N*Q)
# Auxiliary Space: O(N)

# Efficient Approach: The idea is to pre-compute the number of characters present in the range 1 to i for each character from ‘a’ to ‘z’ where 1 ≤ i ≤ N using Prefix Sum technique. Follow the steps below to solve the problem:

# Initialize an array dp[N+1][26] where dp[i][j] stores the number of characters (i+’a’) present in the range [0, i].
# Now, Precompute the number of each character present in the range [1, i] where 1 ≤ i ≤ N by incrementing dp[i][j] by dp[i – 1][j] where 0 ≤ j < 26 and increment dp[i][S[j] – ‘a’] by 1.
# For each query {l, r, y}, print the value of dp[r][y – ‘a’] – dp[l – 1][y – ‘a’] as the number of characters y present in the range [l, r].
