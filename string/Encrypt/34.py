# Minimum Manhattan distance covered by visiting every coordinates from a source to a final vertex

# Difficulty Level : Medium
# Last Updated : 01 Jun, 2021
# Given an array arr[] of co-ordinate points and a source and final co-ordinate point, the task is to find the minimum manhattan distance covered from the source to the final vertex such that every point of the array is visited exactly once. 
 

# Manhattan Distance = \left | x2 - x1 \right | + \left | y2 - y1 \right |  
 

# Examples: 
 

# Input: source = (0, 0), final = (100, 100) 
# arr[] = {(70, 40), (30, 10), (10, 5), (90, 70), (50, 20)} 
# Output: 200
# Input: source = (0, 0), final = (5, 5) 
# arr[] = {(1, 1)} 
# Output: 10 
 

 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: The idea is to use permutation and combination to generate every possible permutation movements to the co-ordinates and then compute the total manhattan distance covered by moving from the first co-ordinate of the array to the final co-ordinate and If the final distance covered is less than the minimum distance covered till now. Then update the minimum distance covered.
# Below is the implementation of the above approach: