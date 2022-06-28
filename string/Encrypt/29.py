# Generate string with Hamming Distance as half of the hamming distance between strings A and B

# Last Updated : 02 Mar, 2022
# Given two Binary string A and B of length N, the task is to find the Binary string whose Hamming Distance to strings A and B is half the Hamming Distance of A and B.
# Examples: 
 

# Input: A = “1001010”, B = “0101010” 
# Output: 0001010 
# Explanation: 
# The hamming distance of the string A and B is 2. 
# The hamming distance of the output string to A is 1. 
# The hamming distance of the output string to B is 1.
# Input: A = “1001010”, B = “1101010” 
# Output: Not Possible 
# Explanation: 
# There exist no string which satisfy our condition.
 

 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Naive Approach: A naive approach is to generate all possible binary strings of the length N and the calculate the Hamming Distance of each string with A and B. If the Hamming Distance between the generated string and to the given string A and B is half the Hamming Distance between A and B, then the generated string is the resultant string. Else there is no such string exist.
# Time Complexity: O(2N)
# Efficient Approach: 
 

# Find the Hamming Distance(say a) between the two given string A and B. If a is odd then we can’t generate another string with Hamming Distance (a/2) with the strings A and B.
# If a is even, then choose first (a/2) characters from string A which is not equal to string B and next (a/2) characters from string B which does not equal to string A to make the resulting string.
# Append the equal characters from string A and B to the resultant string.