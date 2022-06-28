
# 13. Roman to Integer
# Easy

# 4476

# 309

# Add to List

# Share
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


# class Solution(object):
#    def romanToInt(self, s):

#       roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
#       i = 0
#       num = 0
#       print("leennn",len(s))
#       while i < len(s):
#          if i+1<len(s) and s[i:i+2] in roman:
#             num+=roman[s[i:i+2]]
#             i+=2
#          else:
#             #print(i)
#             num+=roman[s[i]]
#             i+=1
#       return num
# ob1 = Solution()
# print(ob1.romanToInt("III"))
# print(ob1.romanToInt("CDXLIII"))

# # M2: 

# def romanToInt(s: str) -> int:
#     # Dictionary of roman numerals
#     roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     # Length of the given string
#     n = len(s)
#     # This variable will store result
#     num = roman_map[s[n - 1]]
#     print("nummm",num)
#     # Loop for each character from right to left
#     for i in range(n - 2, -1, -1):
#         # Check if the character at right of current character is bigger or smaller
#         if roman_map[s[i]] >= roman_map[s[i + 1]]:
#             num += roman_map[s[i]]
#         else:
#             num -= roman_map[s[i]]
#     return num


# print(romanToInt('MCMXCIV'))
