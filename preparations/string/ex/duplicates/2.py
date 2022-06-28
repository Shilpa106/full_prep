# Print a closest string that does not contain adjacent duplicates

# Difficulty Level : Easy

# Given a string S, change the smallest number of letters in S such that all adjacent characters are different. Print the resultant string.
# Examples : 
 

# Input : S = "aab"
# Output: acb
# Explanation :
# Loop will start for i-th character, which 
# is second ‘a’. It’s cannot be ‘b’ since it 
# matches with third char. So output should
# be ‘acb’.

# Input : S = "geeksforgeeks"
# Output: geaksforgeaks
# Explanation :
# Resultant string, after making minimal 
# changes. S = "geaksforgeaks". We made two 
# changes, which is the optimal solution here.
 
# ***************************
# # Approach1
# dS=S = "aab"
# # dS = "geeksforgeeks"
# # dS = "aaccb"
# S=list(dS)
# # print(S)
# for i in range(len(S)):
#     if S[i-1] ==S[i]:
#         S[i]='n' 
# print(S)      

# ***************************