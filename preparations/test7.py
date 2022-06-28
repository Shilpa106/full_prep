
s='aaaabcdd'
for i in range(len(s)-1):
    for j in range(len(s)):
        if s[i] == s[j]:
            i+=1
            