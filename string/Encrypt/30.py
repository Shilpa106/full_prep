# Minimize replacements to make every element in an array exceed every element in another given array

# Last Updated : 03 Jun, 2021
# Given two arrays A[] and B[] of size N and M respectively, where each element is in the range [0, 9], the task is to make each element of the array A[] strictly greater than or smaller than every element in the array B[] by changing any element from either array to any number in the range [0, 9], minimum number of times.

# Examples:  

# Input: A[] = [0, 1, 0], B[] = [2, 0, 0]
# Output: 2
# Explanation:
# Modifying the array B[] to [2, 2, 2] makes every element in the array A[] strictly less than every element in the array B[].
# Hence, the minimum number of changes required = 2.

# Input: A[] = [0, 0, 1, 3, 3], B[] = [0, 2, 3]  
# Output: 3
# Explanation:
# Modifying the array B[] to [4, 4, 4] makes every element in the array A[] strictly less than every element in the array B[].
# Hence, the minimum number of changes required = 3.

# Approach: The idea to solve the given problem is to use two auxiliary arrays prefix_a[] and prefix_b[] of size 10, where prefix_a[i] and prefix_b[i] stores the number of elements in the array A[] ≤ i and the number of elements in the array B[] ≤ i respectively. Follow the steps below to solve the problem:

# Initialize two arrays, prefix_a[] and prefix_b[] of size 10 with {0}.
# Store the frequencies of every element in the arrays A[] and B[] in arrays prefix_a, and prefix_b respectively.
# Perform the prefix sum on the array prefix_a by iterating in the range [1, 9] using the variable i and update prefix_a[i] as (prefix[i] + prefix_a[i – 1]).
# Repeat the above step for the array prefix_b[].
# Iterate in the range [0, 9] using the variable i
# Store the number of operations to make every element in the array A[] strictly greater than the digit i and make every element in the array B[] less than digit i in a variable, say X.
# Initialize it with prefix_a[i] + M – prefix_b[i].
# Similarly, store the number of operations to make every element in the array B[] strictly greater than digit i and make every element in the array A[] less than digit i in a variable, say Y. 
# Initialize it with prefix_b[i] + N – prefix_a[i].
# Update the overall minimum number of operations as the minimum of X and Y. Store the minimum obtained in a variable, say ans.
# After completing the above steps, print the value of ans as the result.
