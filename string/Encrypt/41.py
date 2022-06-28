# Maximum length prefix such that frequency of each character is atmost number of characters with minimum frequency

# Last Updated : 02 Jun, 2022
# Given a string S, the task is to find the prefix of string S with the maximum possible length such that frequency of each character in the prefix is at most the number of characters in S with minimum frequency.

# Examples: 

# Input: S = ‘aabcdaab’ 
# Output: aabcd 
# Explanation: 
# Frequency of characters in the given string – 
# {a: 4, b: 2, c: 1, d: 1} 
# Minimum frequency in 1 and the count of minimum frequency is 2, 
# So frequency of each character in the prefix can be at most 2.

# Input: S = ‘aaabc’ 
# Output: aa 
# Explanation: 
# Frequency of characters in the given string – 
# {a: 3, b: 1, c: 1} 
# Minimum frequency in 1 and the count of minimum frequency is 2, 
# So frequency of each character in the prefix can be at most 2. 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: 

# Initialize a hash-map to store the frequency of the characters.
# Iterate over the string and increment the frequency of the character in the hash-map.
# Find the minimum occurred character in the string and the count of such characters whose frequency is minimum.
# Initialize another hash-map to store the frequency of the characters of the possible prefix string.
# Finally, Iterate over the string from start and increment the count of the characters until the frequency of any characters is not greater than the count of the minimum frequency.
