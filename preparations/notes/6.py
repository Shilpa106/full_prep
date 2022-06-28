tests='a3z2b4'
# op:aaabbbbzz

res=''
i=1
while(i<len(tests)):
    j=i-1
    print("i",tests[i])
    print("j",tests[j])
    res=res+tests[j]*int(tests[i])
    op=''.join(sorted(res))
    # res+=d
    i+=2
print(op)

