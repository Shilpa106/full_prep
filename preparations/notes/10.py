# NO OF OCCURRENCES OF EACH CHARACTER PRESENT IN GIVEN STRING
# A OCCURS 3 TIMES
# B OCCURS 3 TIMES
# C OCCURS 1 TIMES
s='ABBACBA'

b=set()

for i in s:
    b.add(i)
res=''
print(b)
for i in b:
    c=s.count(i)
    res=res+i+str(c)
    # print(c)
print(res)