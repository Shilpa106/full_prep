# Count substrings having frequency of a character exceeding that of another character in a string

# Difficulty Level : Hard
# Last Updated : 29 Jan, 2022
# Given a string S of size N consisting of characters a, b, and c only, the task is to find the number of substrings of the given string S such that the frequency of character a is greater than the frequency of character c.

# Examples:

# Input: S = “abcc”
# Output: 2
# Explanation:
# Below are all the possible substrings of S(= “abcc”) having the frequency of the character greater than the character c:

# “a”: The frequency of a and c is 1 and 0 respectively.
# “ab”: The frequency of a and c is 1 and 0 respectively.
# Therefore, the count of such substrings is 2.

# Input: S = “abcabcabcaaaaabbbccccc”
# Output: 148

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Naive Approach: The simplest approach to solve the given problem is to generate all possible substrings of the given string S and count those substrings having a count of character ‘a’ greater than the count of character ‘c’. After checking for all the substrings, print the value of the total count as the result.