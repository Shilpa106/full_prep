from re import L


tests='a4k3b2'
# op:aeknbd

# print(ord(tests[0]))
# print(chr(99))
i=0
res=''
while i<len(tests):
    if i%2==0:
        res+=tests[i]
        print(res)
    # else:
    j=i+1
    res+=chr(ord(tests[i])+int(tests[j]))
    
    i+=2
print(res)
    