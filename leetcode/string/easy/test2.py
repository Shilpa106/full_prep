# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


s = "abcabcbb"
m=[]
g=''
d=[]
for i in range(0,len(s)):
    # print(i)
    for j in range(i+1, len(s)):
        # print(j)
        # print(j,i,end='')
        for k in range(i,j):
            print(s[k])
        d.append(s[k])
            # print(s[k])
            # b=k
        # d.append(b)
            # g+=str(k)
# print(g)
print(d)
# m.append(d)
# print(m)
        
