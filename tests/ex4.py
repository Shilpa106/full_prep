def toString(List):
    return ''.join(List)


def permute(a, l, r):
    if l==r:
        print (toString(a))
    else:
        for i in range(l,r):#0,3
            print("10",i, l, r)
            a[l], a[i] = a[i], a[l]
            print(a[l],a[i])
            print("hiiiiiiiiii")
            permute(a, l+1, r)
            print("14",i,l,r)
            a[l], a[i] = a[i], a[l] 
            print(a[l],a[i])
            print("heyyyyyyyyyyy")
            
 

string = "ABC"
n = len(string)
a = list(string)
print("222",a)
permute(a, 0, n)