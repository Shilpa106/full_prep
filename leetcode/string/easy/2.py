# 14. Longest Common Prefix
# Easy

# 8299

# 3056

# Add to List

# Share
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

# strs = ["flower","flow","flight"]
# for i in range(len(strs)): 
#     print(strs[i][i])
    # if strs[i].startswith('fl0'):
    #     print('yes')
    # # for j in i:
    # #     print(j)



class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return '' 
        res = ''
        strs = sorted(strs)
        # print(strs)
        for i in strs[0]:
            print(i)
            if strs[-1].startswith(res+i):
                print("58",strs[-1])
                res += i
            else:
                break
        return res

c=Solution()
strs = ["flower","flow","flight"]
print(c.longestCommonPrefix(strs))
