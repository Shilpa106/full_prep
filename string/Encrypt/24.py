# Map every character of one string to another such that all occurrences are mapped to the same character

# Difficulty Level : Basic
# Last Updated : 10 Jun, 2021
# Given two string s1 and s2, the task is to check if characters of the first string can be mapped with the character of the second string such that if a character ch1 is mapped with some character ch2 then all the occurrences of ch1 will only be mapped with ch2 for both the strings.

# Examples: 

# Input: s1 = “axx”, s2 = “cbc” 
# Output: Yes 
# ‘a’ in s1 can be mapped to ‘b’ in s2 
# and ‘x’ in s1 can be mapped to ‘c’ in s2.

# Input: s1 = “a”, s2 = “df” 
# Output: No 
 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: If the lengths of both the strings are unequal then the strings cannot be mapped else create two frequency arrays freq1[] and freq2[] which will store the frequencies of all the characters of the given strings s1 and s2 respectively. Now, for every non-zero value in freq1[] find an equal value in freq2[]. If all the non-zero values from freq1[] can be mapped to some value in freq2[] then the answer is possible else not.