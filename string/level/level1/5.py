# Closest Strings 
# Given a list of words followed by two words, the task to find the minimum distance between the given two words in the list of words

# Example 1:

# Input:
# S = ["the", "quick", "brown", "fox", "quick"]
# word1 = "the"
# word2 = "fox"
# Output: 3
# Explanation: Minimum distance between the words "the" and "fox" is 3

# Example 2:
# Input:
# S = ["geeks", "for", "geeks", "contribute", "practice"]
# word1 = "geeks"
# word2 = "practice"
# Output: 2
# Explanation: Minimum distance between the words "geeks" and "practice" is 2

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function shortestDistance() which list of words, two strings as inputs and returns
#  the minimum distance between two words

# Expected Time Complexity: O(|S|)
# Expected Auxiliary Space: O(1)

# Constraints:
# Sum of lengths of words ≤ 105

# Note: word1 and word2 are both in the list.

# s = ["geeks", "for", "geeks", "contribute", "practice"]
s = ["geeks", "for", "geeks", "contribute", "practice","ghf","kjkj","iuyiuy","hjghjg","hjghjghj",'practice']

word1 = "geeks"
word2 = "practice"
# Output: 2

# Approach1
# a=[]
# b=[]
# for i in range(len(s)):
#     # print(s[i])
#     if 'geeks' in s[i]:
#         print(i)
#         a.append(i)


# for i in range(len(s)):
#     if 'practice' in s[i]:
#         # print(i)
#         b.append(i)

# print(a)
# print(b)


# for i in a:
#     for j in b:
#         print((abs(i-j)))


# Approach2
