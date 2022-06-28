# Convert list of string into sorted list of integer
# ****************************************************************
# Difficulty Level : Basic
# Last Updated : 18 Feb, 2019
# Given a list of string, write a Python program to convert it into sorted list of integer.

# Examples:

# Input: ['21', '1', '131', '12', '15']
# Output: [1, 12, 15, 21, 131]

# Input: ['11', '1', '58', '15', '0']
# Output: [0, 1, 11, 15, 58]

tests=['21', '1', '131', '12', '15']
print(list(sorted(tests)))