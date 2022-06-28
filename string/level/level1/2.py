# Longest Common Prefix in an Array 
# Lamp 
# Given a array of N strings, find the longest common prefix among all strings present in the array.

# Example 1:

# Input:
# N = 4
# arr[] = {geeksforgeeks, geeks, geek, geezer}
# Output: gee
# Explanation: "gee" is the longest common prefix in all the given strings.
# Example 2:

# Input: 
# N = 2
# arr[] = {hello, world}
# Output: -1
# Explanation: There's no common prefix in the given strings.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function longestCommonPrefix() which takes the string array arr[] and its size N
#  as inputs and returns the longest common prefix common in all the strings in the array. If there's no prefix common in all the strings, return "-1".


# Expected Time Complexity: O(N*max(|arri|)).
# Expected Auxiliary Space: O(max(|arri|)) for result.


# Constraints:
# 1 ≤ N ≤ 103
# 1 ≤ |arri| ≤ 103

s = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
print(s)
s.sort()
print(s)
n=len(s)
min_str=min(len(s[0]),len(s[n-1]))
print(min_str)
i=0
while(i<min_str and s[0][i]==s[n-1][i]):
    i+=1

print(s[0][0:i])