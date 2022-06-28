# Construct a graph using N vertices whose shortest distance between K pair of vertices is 2

# Last Updated : 18 Aug, 2021
# Given two positive integers N and K, the task is to construct a simple and connected graph consisting of N vertices with the length of each edge as 1 unit, such that the shortest distance between exactly K pairs of vertices is 2. If it is not possible to construct the graph, then print -1. Otherwise, print the edges of the graph.

# Examples:

# Input: N = 5, K = 3 
# Output: { { 1, 2 }, { 1, 3}, { 1, 4 }, { 1, 5 }, { 2, 3 }, { 2, 4 }, { 2, 5 } } 
# Explanation: 
# The distance between the pairs of vertices { (3, 4), (4, 5), (3, 5) } is 2. 
 



# Input: N = 5, K = 8 
# Output: -1

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: Follow the steps below to solve the problem:

# Since the graph is simple and connected, Therefore, the maximum possible count of edges, say Max is ((N – 1) * (N – 2)) / 2.
# If K is greater than Max, then print -1.
# Initialize an array, say edges[], to store the edges of the graph.
# Otherwise, first connect all the vertices with 1 and store it in edges[], then connect all the pairs of vertices (i, j) such that i >= 2 and j > i and store it in edges[].
# Finally, print the first ((N – 1) + Max – K ) elements of edges[] array.
