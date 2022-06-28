# Find the N-th character 
# Medium Accuracy: 68.85% Submissions: 8476 Points: 4
# Given a binary string S . Perform R iterations on string S, where in each iteration 0 becomes 01 and 1 becomes 10. Find the Nth character (considering 0 based indexing) of the string after performing these R iterations. (See Examples for better understanding)


# Example 1:

# Input:
# S = 101
# R = 2 
# N = 3
# Output:
# 1
# Explanation : 
# After 1st iteration S becomes 100110.
# After 2nd iteration, S = 100101101001
# Now, we can clearly see that the character
# at 3rd index is 1, and so the output.
# Example

# Input:
# S = 11
# R = 1 
# N = 3
# Output:
# 0
# Explanation: 
# After 1st iteration S becomes 1010.
# Now, we can clearly see that the character
# at 3rd index is 0, and so the output.

# Your task:
# You don't need to read input or print anything. Your task is to complete the function nthCharacter() which takes the string S and integers R and N as input parameters and returns the N-th character of the string after performing R operations on S.
 
# Expected Time Complexity: O(r*len(s))
# Expected Auxilary Space: O(len(s))

# Constraints:
# 1 ≤ String length ≤ 103
# 1 ≤ R ≤ 20
# 0 ≤ N < Length of final string