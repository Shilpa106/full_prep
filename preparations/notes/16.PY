s1='abcdefg'
s2='xyz'
s3='12345'
# op:ax1,by2,cz3,d4,e5,f,/g

res=''
i=j=k=0
while (i<len(s1) or j<len(s2) or k<len(s3)):

    if i<len(s1):
        res=res+s1[i]
        i=i+1
    if j<len(s2):
        res=res+s2[j]
        j=j+1
    if k<len(s3):
        res=res+s3[k]
        k=k+1
print(res)