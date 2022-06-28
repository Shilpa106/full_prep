# Find element in array with frequency equal to sum of frequencies of other elements

# Last Updated : 19 May, 2021
# Given an integer array arr[], the task is to find an element in the array whose frequency is equal to the sum of frequencies of other elements of the array.

# Examples: 

# Input: arr[] = {1, 2, 2, 3, 3, 3} 
# Output: 3 
# Explanation: 
# Frequencies of elements of the array – 
# Frequency(3) = 3 
# Frequency(2) = 2 
# Frequency(1) = 1 
# Here, the frequency of element 3 is equal to the 
# the sum of frequencies of other elements of the array. 

# Input: arr[] = {1, 2, 3} 
# Output: -1 
# Explanation: 
# In the above-given array, there is no such 
# element whose frequency is equal to the sum of 
# frequencies of other elements of the array. 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: The key observation in the problem is if the length of the array is odd, then there will be no such element, whereas, in the case of an even length array, calculate the frequency of each element of the array and then finally, check for any element of the array that has a frequency equal to the half-length of the array. 