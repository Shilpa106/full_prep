# Form a palindrome 
# Medium Accuracy: 53.0% Submissions: 19351 Points: 4
# Lamp
# This problem is part of GFG SDE Sheet. Click here to view more.   
# Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
# For Example:
# ab: Number of insertions required is 1. bab or aba
# aa: Number of insertions required is 0. aa
# abcd: Number of insertions required is 3. dcbabcd


# Example 1:

# Input: str = "abcd"
# Output: 3
# Explanation: Inserted character marked
# with bold characters in dcbabcd
# Example 2:

# Input: str = "aa"
# Output: 0
# Explanation:"aa" is already a palindrome.

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function countMin() which takes the string str as inputs and returns the answer.

# Expected Time Complexity: O(N2), N = |str|
# Expected Auxiliary Space: O(N2)

# Constraints:
# 1 ≤ |str| ≤ 103
# str contains only lower case alphabets.

