tests='ABAABBCA'
# OP:4A3B1C
s=set()
res=''
for i in tests:
    s.add(i)
for j in s:
    c=tests.count(j)
    res=res+str(c)+j
print(res)
