# print character present at even and odd index separately for the given string.

a='hello world geeks for geeks'
c=a.split()
print(c)
even=''
odd=''
for i in range(len(c)):
    # print(i)
    if i%2==0:
        even+=c[i]
    else:
        odd+=c[i]

print("even value",even)
print("odd value",odd)
     
