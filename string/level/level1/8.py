# Equal point in a string of brackets 

# Given a string S of opening and closing brackets '(' and ')' only. The task is to find an equal point. An equal point is an index such that the number of 
# closing brackets on right from that point must be equal to number of opening brackets before that point.


# Example 1:

# Input: str = "(())))("
# Output: 4
# Explanation:# After index 4, string splits into (()) and ))(. Number of opening brackets in the first part is equal to number of closing brackets in the second part.
# Example 2:
# Input : str = "))"
# Output: 2
# Explanation:
# As after 2nd position i.e. )) and "empty" string will be split into these two parts: So, in this number of opening brackets i.e. 0 in the first part is equal to number of
# closing brackets in the second part i.e.
# also 0.

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function findIndex() which takes the string S as 
# inputs and returns the occurrence of the equal point in the string.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)


# Constraints:
# 1 ≤ S ≤ 106
# String can be unbalanced

# Method to find an equal index
# def findIndex(str):
str = "(()))(()()())))"
l = len(str)
open = [0] * (l + 1)
close = [0] * (l + 1)
index = -1

open[0] = 0
close[l] = 0
if (str[0]=='('):
    open[1] = 1
if (str[l - 1] == ')'):
    close[l - 1] = 1

# Store the number of opening brackets at each index
for i in range(1, l):
    if (str[i] == '('):
        open[i + 1] = open[i] + 1
        print("open1",open[i + 1])
    else:
        open[i + 1] = open[i]
        print("open2",open[i + 1])

# Store the number of closing brackets at each index
for i in range(l - 2, -1, -1):
    if ( str[i] == ')'):
        close[i] = close[i + 1] + 1
        print('close1',close[i])
    else:
        close[i] = close[i + 1]
        print('close2',close[i])
[0, 0, 0, 0, 0, 0]
# check if there is no opening or closing brackets
# if (open[l] == 0):
# 	return len
# if (close[0] == 0):
# 	return 0

# check if there is any index at which both brackets are equal
for i in range(l + 1):
    if (open[i] == close[i]):
        print("resssssssssssss",open[i],close[i])
        index = i

	# return index
print("index",index)
	
# Driver Code
# str = "(()))(()()())))"
# print(findIndex(str))

