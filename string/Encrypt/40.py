# Remove characters from given string whose frequencies are a Prime Number

# Last Updated : 11 Jan, 2022
# Given string str of length N, the task is to remove all the characters from the string whose frequencies are prime.

# Examples:

# Input: str = “geeksforgeeks”
# Output: eeforee
# Explanation:
# The frequencies of characters is: { g=2, e=4, k=2,  s=2, f=1, o=1, r=1}
# So, g, k and s are the characters with prime frequencies so, they are removed from the string.
# The resultant string is “eeforee”

# Input: str = “abcdef”
# Output: abcdef 
# Explanation:
# Since all the characters are unique with frequency as 1, so no character is removed.

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Naive Approach: The simplest approach to solve this problem is to find the frequencies of every distinct character present in the string and for each character, check if its frequency is Prime or not. If the frequency is found to be prime, skip that character. Otherwise, append it to the new string formed. 

# Time Complexity: O( N 3/2)
# Auxiliary Space: O(N)

# Efficient Approach: The above approach can be optimized by using the Sieve of Eratosthenes to precompute Prime Numbers. Follow the steps below to solve the problem:

# Using Sieve of Eratosthenes, generate all prime numbers up to N and store them in the array prime[].
# Initialize a Map and store the frequency of each character.
# Then, traverse the string and find out which characters have prime frequencies with the help of the map and prime[] array.
# Ignore all those characters which have prime frequencies and store the rest in a new string.
# After the above steps, print the new string.