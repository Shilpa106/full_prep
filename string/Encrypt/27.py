# Replace every character of string by character whose ASCII value is K times more than it

# Difficulty Level : Easy
# Last Updated : 27 May, 2022
# Given string str consisting of lowercase letters only and an integer k, the task is to replace every character of the given string with a character whose ASCII value is k times more than it. If the ASCII value exceeds ‘z’, then start checking from ‘a’ in a cyclic manner.

# Examples:  

# Input: str = “abc”, k = 2 
# Output: cde 
# a is moved by 2 times which results in character c 
# b is moved by 2 times which results in character d 
# c is moved by 2 times which results in character e
# Input: str = “abc”, k = 28 
# Output: cde 
# a is moved 25 times, z is reached. Then 26th character will be a, 27-th b and 28-th c. 
# b is moved 24 times, z is reached. 28-th is d. 
# b is moved 23 times, z is reached. 28-th is e. 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: Iterate for every character in the string and perform the below steps for each character:  

# Add k to the ASCII value of character str[i].
# If it exceeds 122, then perform a modulus operation of k with 26 to reduce the number of steps, as 26 is the maximum number of shifts that can be performed in a rotation.
# To find the character, add k to 96. Hence, the character with ASCII value k+96 will be a new character.
# Repeat the above steps for every character of the given string.