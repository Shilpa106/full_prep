# Count of index pairs (i, j) such that string after deleting ith character is equal to string after deleting jth character

# Last Updated : 03 Dec, 2021
# Given a string str of N characters, the task is to calculate the count of valid unordered pairs of (i, j) such that the string after deleting ith character is equal to the string after deleting the jth character.

# Examples:

# Input: str = “aabb”
# Output: 2
# Explanation: The string after deletion of 1st element is “abb” and the string after deletion of  2nd element is “abb”. Similarly, the string after deletion of 3rd element is “aab” and the string after deletion of  4th element is “aab”. Hence, the number of valid pairs of (i, j) are 2, i.e, (1, 2) and (3, 4).

# Input: str = “aaaaaa”
# Output: 15

 
# Approach: The given problem can be solved using the following observations:

# If Si = Sj, then Si = Si+1 = Si+2 … = Sj must hold true.
# Also if Si = Sj, then str[i] = str[i+1] = str[i+2] … = str[j] must hold true as well.
# Therefore, using the above observations, the two-pointer technique can be used to calculate the intervals (l, r) in the string str such that str[l] = str[l+1] … = str[r], and for each valid (l, r), the count of valid pairs will be r – lC2.