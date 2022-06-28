# Encrypt string with product of number of vowels and consonants in substring of size k

# Difficulty Level : Easy
# Last Updated : 02 Dec, 2021
# Given a string s and a positive integer k. You need to encrypt the given string such that each substring of size k is represented by an integer, which is obtained by the product of number of vowels and number of consonants in the substring.
# Examples: 
 

# Input : s = "hello", k = 2
# Output : 1101
# k = 2, so each substring should be of size 2,
# he, consonants = 1, vowels = 1, product = 1
# el, consonants = 1, vowels = 1, product = 1
# ll, consonants = 1, vowels = 0, product = 0
# lo, consonants = 1, vowels = 1, product = 1
# So, encrypted string is 1101.

# Input : s = "geeksforgeeks", k = 5
# Output : 666446666