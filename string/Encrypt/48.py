# Binary string with given frequencies of sums of consecutive pairs of characters

# Difficulty Level : Expert
# Last Updated : 11 Jun, 2021
# Given three integers P, Q, and R, the task is to generate a binary string with P, Q, and R pairs of consecutive characters with sum 0, 1, and 2 respectively.
# Examples: 

# Input: P = 1, Q = 2, R = 2 
# Output: 111001 
# Explanation: 
# Substrings “00”, “10”, “01”, and “11” have sums 0, 1, 1, and 2 respectively. 
# Thus, the following set of substrings { {“11”}, {“11”}, {“10”}, {“00”}, {“01”} } satisfy the given constraints. Hence, the string formed by the substrings is 111001.
# Input: P = 3, Q = 1, R = 0 
# Output: 10000 
 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: In order to solve this problem, we need to follow the following steps:  

# If P and R are non-zero, then there is at least one pair of consecutive characters with sum 1. Thus, if Q provided is 0, in such a case, then no such string can be formed. Hence, return -1.
# If Q is zero, and only one of P and R is non-zero, then append 0 P+1 times if P is non-zero or append 1 R+1 time if R is non-zero.
# If all of them are non-zero: 
# Append 0 and 1 P + 1 and Q + 1 times respectively.
# Append 0 and 1 alternatingly Q – 1 time.