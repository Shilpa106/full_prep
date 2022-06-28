# Maximise distance by rearranging all duplicates at same distance in given Array

# Difficulty Level : Hard
# Last Updated : 25 Feb, 2022
# Given an array arr[] of N integers. Arrange the array in a way such that the minimum distance among all pairs of same elements is maximum among all possible arrangements. The task is to find this maximum value.

# Examples:

# Input: arr[] = {1, 1, 2, 3}
# Output: 3
# Explanation: All possible arrangements are: 
# {1, 1, 2, 3}, {1, 1, 3, 2}, {1, 2, 1, 3}, {1, 2, 3, 1}, {1, 3, 1, 2}, {1, 3, 2, 1},  
# {2, 1, 1, 3}, {2, 1, 3, 1}, {2, 3, 1, 1}, {3, 1, 1, 2}, {3, 1, 2, 1}, {3, 2, 1, 1}.
# Here the arrangements {1, 2, 3, 1} and {1, 3, 2, 1} gives the answer which is 3.
# As distance = |(index of first 1) – (index of second 1)|

# Input: arr[] = {1, 2, 1, 2, 9, 10, 9}
# Output: 4
# Explanation: One such arrangement is {2, 9, 1, 10, 2, 9, 1}

 
# Approach: The approach to solve this problem is based on the observation that the elements with maximum frequency must have as much distance between them as possible. Follow the steps mentioned below to solve the problem: 

# Find out the element(s) with maximum frequency.
# Suppose m elements have maximum frequency max_freq then conquer m*max_freq positions from the N positions. Now the positions unoccupied are un_pos = N – max_freq*m. 
# Now, group the elements which do not have maximum frequency consecutively in the same order and have an equal interval.
# The greatest interval can be given by interval = un_pos/(max_freq-1) because when all the occurrences of m elements are placed equidistant to each other it will break the arrangement in (max_freq – 1) segments.
# And finally adding m for the highest frequency elements one each we get the answer to the given question as interval + m.
# Below is the implementation of the above approach