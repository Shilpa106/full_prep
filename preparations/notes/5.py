
from imghdr import tests


tests='a4b3c2'
# op:aaaabbbcc
res=''
m=[]
i=1
while(i<len(tests)):
    print("i",tests[i])
    j=i-1
    print("j",tests[j])
    h=tests[j]*int(tests[i])
    # print(h)
    res+=h

    i+=2
   

print(res)



