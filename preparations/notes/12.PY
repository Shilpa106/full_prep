tests='ABAABBCA'
# OP:A4B3C1
d=[]
c=1
for i in tests:
    d.append(i)
    if i in d:
        c+=1
    print(c)
