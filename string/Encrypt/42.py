# Sort array of strings after sorting each string after removing characters whose frequencies are not a powers of 2

# Last Updated : 25 Aug, 2021
# Given an array arr[] consisting of N strings, the task is to sort the array in ascending order after modifying each string by removing all characters that are not perfect power of 2 and then sort the modified string in decreasing order.

# Examples:

# Input: arr[] = {“aaacbb”, “geeks”, “aaa”}
# Output: cbb skgee
# Explanation:
# Following are the modified strings in the array arr[]:

# For the string “aaacbb”: The frequency of a is not the power of 2. Therefore, removing ‘a’ modifies the string to “cbb”. Now, sorting the string “cbb” in increasing order of frequency modifies the string to “cbb”.
# For the string “geeks”: The frequency of every character is a power of 2. Now, sorting the string “geeks” in increasing order of frequency modifies the string to “skgee”.
# For the string “aaa”: The frequency of a is not the power of 2. Therefore, removing ‘a’ modifies the string to “”.
# Therefore, sorting the above strings in increasing order gives {“cbb”, “skgee”}.

# Input: S[] = {“c”, “a”, “b”}
# Output: a b c

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: The given problem can be solved by using the Hashing to store the frequencies of all the characters for each string and then perform the given operations. Follow the steps below to solve the problem:

# Traverse the given array of strings arr[] and for each string perform the following operations:
# Store the frequency of each character in a Map.
# Create an empty string, say T, to store the modified string.
# Now traverse the map and append the characters whose frequency is in the power of 2 to the string T.
# Sort the string T in increasing order, and add it to an array of strings res[].
# Sort the array res[] in increasing order.
# After completing the above steps,  print the strings in the array res[] as the result.