# Input: s = "gfg"
# Output: 7
# Explanation: The seven distinct
# subsequences are "", "g", "f", "gf", "fg",
# "gg" and "gfg" 
# [0,1,2,01,12,02,012]
s='gfg'
l=''
for i in range(len(s)+1):
    for j in range(i,len(s)):
        print(s[i:j])
        if s[i] != s[j]:
            l+=s[i:j]
    print(l)
#     print(i)
# for i in s:
#     print(i)