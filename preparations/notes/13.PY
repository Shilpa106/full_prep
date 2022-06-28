# FIND THE NO OF OCCURRENCES OF EACH VOWEL PRESENT IN GIVEN GIVEN STRING
s='GEEKSFORGEEKS'
res=''
vowel=['A','E','I','O','U']
for i in vowel:
    if i in s:
        c=s.count(i)
        res=res+i+str(c)
print(res)