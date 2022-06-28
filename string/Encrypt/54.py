# Modify a string by circularly shifting each character to the right by respective frequencies

# Last Updated : 28 May, 2021
# Given a string S consisting of lowercase English alphabets, the task is to right shift each character of the given string S circularly by its frequency.

# Circular shifting of characters refers to shifting character ‘z’ to ‘a’, as its next character.

# Examples:

# Input: S = “geeksforgeeks”
# Output: iiimugpsiiimu 
# Explanation:
# Following changes are made on the string S:

# Frequency of ‘g’ is 2. Therefore, shifting the character ‘g’ by 2 becomes ‘i’.
# Frequency of ‘e’ is 4. Therefore, shifting the character ‘e’ by 4 becomes ‘i’.
# Frequency of ‘k’ is 2. Therefore, shifting the character ‘k’ by 2 becomes ‘m’.
# Frequency of ‘s’ is 2. Therefore, shifting the character ‘s’ by 2 becomes ‘u’.
# Frequency of ‘f’ is 1. Therefore, shifting the character ‘f’ by 1 becomes ‘g’.
# Frequency of ‘o’ is 1. Therefore, shifting the character ‘o’ by 1 becomes ‘p’.
# Frequency of ‘r’ is 1. Therefore, shifting the character ‘r’ by 1 becomes ‘s’.
# After the above shifting of characters, the string modifies to “iiimugpsiiimu”.

# Input: S = “aabcadb”
# Output: ddddded

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: The idea to solve this problem is to traverse the string and find the frequency of occurrence of each character in the string and then increment each of the characters by its frequency. Follow the steps below to solve the problem:

# Initialize an array, say frequency[] that stores the occurrences of each character in the string S.
# Traverse the given string S and perform the following steps:
# Find the frequency of the current character S[i].
# Increment the current character by its frequency and update the value of S[i] to its updated character.
# After completing the above steps, print the string S as the resultant modified string.
