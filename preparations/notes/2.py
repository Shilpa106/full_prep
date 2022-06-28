
test='one two three four five six'
# op:one owt three ruof five xis

c=test.split()
print(c)
op=[]
for i in range(len(c)):
    if i%2==0:
        print(c[i])
        op.append(c[i][::-1])
    else:
        op.append(c[i])
print(op)

