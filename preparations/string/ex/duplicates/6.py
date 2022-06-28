# Count of ways to empty given String by recursively removing all adjacent duplicates

# Difficulty Level : Expert
# Last Updated : 28 Sep, 2021
# Given a string S, in one move it is allowed to remove two adjacent equal characters. After the removal, both endpoints of the removed characters are joined. Calculate the total number of ways to empty the string. 

# Example: 

# Input: S = aabccb
# Output: 3
# Explanation:
# 1. aabccb -> aabb -> aa 
# 2. aabccb -> aabb -> bb
# 3. aabccb -> bccb -> bb
# Hence, there are a total of 3 ways to empty the string after a valid set of moves.

# Input: S = aabbc
# Output: 0
# Explanation: The string is of odd length, so it is not possible to empty the whole string.