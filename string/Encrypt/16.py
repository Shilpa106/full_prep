# Program to find the shortest distance between diagonal and edge skew of a Cube

# Difficulty Level : Medium
# Last Updated : 17 Mar, 2021
# Given an integer A, denoting the length of a cube, the task is to find the shortest distance between the diagonal of a cube and an edge skew to it i.e. KL in the below figure.



# Examples :

# Input: A = 2
# Output: 1.4142
# Explanation:
# Length of KL = A / √2
# Length of KL = 2 / 1.41 = 1.4142

# Input: A = 3
# Output: 2.1213

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: The idea to solve the problem is based on the following mathematical formula:

# Let’s draw a perpendicular from K to down face of cube as Q.
# Using Pythagorean Theorem in triangle QKL,

# KL2 = QK2 + QL2

# l2 = (a/2)2 + (a/2)2 

# l2 = 2 * (a/2)2

# l = a / sqrt(2)