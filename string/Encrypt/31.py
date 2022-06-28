# Divide every element of one array by other array elements

# Difficulty Level : Easy
# Last Updated : 26 Feb, 2021
# Given two arrays and the operation to be performed is that the every element of a[] should be divided by all the element of b[] and their floor value has to be calculated.
# Examples : 
 

# Input : a[] = {5, 100, 8}, b[] = {2, 3}
# Output : 0 16 1
# Explanation :
# Size of a[] is 3.
# Size of b[] is 2.
# Now 5 has to be divided by the elements of array b[]
# i.e. 5 is divided by 2, then the quotient obtained 
# is divided by 3 and the floor value of this is 
# calculated. The same process is repeated for the other
# array elements.
 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# First Approach : This solution is of complexity O(n * m) where size of a[] is n and size of array b[] is m. In this solution we fix the elements of array a[] and iterate it with the elements of array b[].
# Second Approach : In this method we have used simple maths. We first find product of array B and then divide it by each array element of a[] 
# The complexity of this solution is O(n).