# Replace every character of a string by a different character

# Difficulty Level : Medium
# Last Updated : 27 May, 2022
# Given a string str of lowercase alphabets only. The task is to replace every character by some new character. The new character belongs to $a-z$     (small case only) Replacement of str[i] is determined by:
 

# str[i] = Character obtained after traversing ascii(str[i]) no. of characters in ‘a-z’ repeatedly after str[i].

# Examples: 
 

# Input: str = “geeksforgeeks” 
# Output: fbbnddvbfbbnd
# In the above case str = “geeksforgeeks”, 
# the ASCII value of ‘g’ is 103 therefore ‘g’ has been replaced by moving 103 times from ‘g’ in the desired range i.e., a-z. 
# Hence, character ‘g’ is replaced by ‘f’. 
# Similarly, the complete string “geeksforgeeks” becomes “fbbnddvbfbbnd”.
# Input: str = “science” 
# Output: dxjbtxb

 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: 
 

# Traverse the string.
# For every i, find the character that needs to be replaced with str[i].
# Replace str[i] with that character.