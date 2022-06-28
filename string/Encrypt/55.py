# Longest sub-string having frequency of each character less than equal to k

# Difficulty Level : Medium
# Last Updated : 21 May, 2021
# Given a string str of length n. The problem is to find the length of the longest sub-string in str having frequency of each character less than equal to the given value k.
# Examples : 
 

# Input : str = "babcaag", k = 1
# Output : 3
# abc and bca are the two longest
# sub-strings having frequency of each character 
# in them less than equal to '1'.

# Input : str = "geeksforgeeks", k = 2
# Output : 10
 

# Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
# Approach: Create an array freq[] of size 26 implemented as hash table to store the frequency of each character of str. Initialize all of its indexes with value ‘0’. Length of the string is n. Now implement the following algorithm. 
 

# longSubstring(str, k)
#     Initialize start = 0
#     Initialize maxLen = 0
#     Declare ch
    
#     for i = 0 to n-1
#         ch = str[i]
#     freq[ch - 'a']++
#     if k < freq[ch - 'a'] then
#         if maxLen < (i - start) then
#             maxLen = i - start
#         while (k < freq[ch - 'a'])    
#             freq[str[start] - 'a']--
#         start++

#     if maxLen < (n - start) then
#         maxLen = n - start
    
#     return maxLen