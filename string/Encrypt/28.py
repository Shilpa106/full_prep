# Find a string such that every character is lexicographically greater than its immediate next character

# Last Updated : 09 Jun, 2022
# Given an integer N, the task is to find a string(considering only lowercase characters) of length (N+1) such that the character at any position should be lexicographically greater than its immediate next character. 
# Examples: 
 

# Input: 2
# Output: cba
# c is greater than b and
# b is greater than a

# Input: 5
# Output: fedcba
# Approach: Given an integer N, the task is to find a string(considering only lowercase characters) of length (N+1) such that the character at any position should be lexicographically greater than its immediate 
 

# Declare a string with all the alphabets in reverse order.
# Take modulus of the given number with 26. So, if the value is less than 26, run a loop from 26 – (Modulus Value + 1) to 25 and go to that index of the string and print that index.
# Divide the modulus value with 26 if value comesGiven an integer N, the task is to find a string(considering only lowercase characters) of length (N+1) such that the character at any position should be lexicographically greater than its immediate  greater than 0 then run the loop to 0 to 25 and print every element of the string by given the calculated value.
