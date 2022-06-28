# 20. Valid Parentheses


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {"(": ")", "[": "]", "{": "}"}
        stack = []
        
        for b in s:
            if not stack:
                if b not in pair:
                    return False
                stack.append(b)
            else:
                if b not in pair and pair[stack[-1]] != b:
                    return False
                if b == pair[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(b)
            
        return not stack

c=Solution()
print(c.isValid('()[]{}'))


# class Solution:
#     def isValid(self, s):
#         stack = []
#         dict = {"]":"[", "}":"{", ")":"("}
#         for char in s:
#             if char in dict.values():
#                 stack.append(char)
#             elif char in dict.keys():
#                 if stack == [] or dict[char] != stack.pop():
#                     return False
#             else:
#                 return False
#         return stack == []