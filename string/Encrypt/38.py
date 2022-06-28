# Modify string by replacing characters by alphabets whose distance from that character is equal to its frequency

# Difficulty Level : Basic
# Last Updated : 27 May, 2021
# Given a string S consisting of N lowercase alphabets, the task is to modify the string S by replacing each character with the alphabet whose circular distance from the character is equal to the frequency of the character in S.

# Examples:

# Input: S = “geeks”
# Output: hgglt
# Explanation: 
# The following modifications are done on the string S:

# The frequency of ‘g’ in the string is 1. Therefore, ‘g’ is replaced by ‘h’.
# The frequency of ‘e’ in the string is 2. Therefore, ‘e’ is replaced by ‘g’.
# The frequency of ‘e’ in the string is 2. Therefore, ‘e’ is replaced by ‘g’.
# The frequency of ‘k’ in the string is 1. Therefore, ‘k’ is converted to ‘k’ + 1 = ‘l’.
# The frequency of ‘s’ in the string is 1. Therefore, ‘s’ is converted to ‘s’ + 1 = ‘t’.
# Therefore, the modified string S is “hgglt”.

# Input: S = “jazz”
# Output: “kbbb”

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: The given problem can be solved by maintaining the frequency array that stores the occurrences of each character in the string. Follow the steps below to solve the problem:

# Initialize an array, freq[26] initially with all elements as 0 to store the frequency of each character of the string.
# Traverse the given string S and increment the frequency of each character S[i] by 1in the array freq[].
# Traverse the string S used the variable i and performed the following steps:
# Store the value to be added to S[i] in a variable, add as (freq[i] % 26).
# If, after adding the value of add to S[i], S[i] does not exceed the character z, then update S[i] to S[i] + add.
# Otherwise, update the value of add to (S[i] + add – z) and then set S[i] to (a + add – 1).
# After completing the above steps, print the modified string S.
