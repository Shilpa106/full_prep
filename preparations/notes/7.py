tests='aaaabbbccz'
# op:4a3b2c1z

i=0
res=''
while i<len(tests):
    # print(i)
    # print(tests[i])
    c=tests.count(tests[i])
    print(c)
    res=res+str(c)+tests[i]
    i+=c
print("resssssssssss",res)
