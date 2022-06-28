# Divisible by 7 

# Given an n-digit large number in form of string, check whether it is divisible by 7 or not. Print 1 if divisible by 7, otherwise 0.


# Example 1:

# Input: num = "8955795758"
# Output: 1
# Explanation: 8955795758 is divisible
# by 7.
# Example 2:

# Input: num = "1000"
# Output: 0
# Explanation: 1000 is not divisible
# by 7.

# Your Task:  
# You don't need to read input or print anything.Your task is to complete the function isdivisible7â€‹() which takes the string num as inputs and returns the answer.


# Expected Time Complexity: O(|num|)
# Expected Auxiliary Space: O(1)


# Constraints:
# 1 ≤ |num| ≤ 105


# num = "8955795758"
num = "1000"
# print(type(num))
number=int(num)
print(number)
print(type(number))
if number%7==0:
    print(1)
else:
    print(0)