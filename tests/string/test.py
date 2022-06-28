#1. Rearrange characters in a string such that no two adjacent are same
# Input: aaabc 
# Output: abaca 

# Input: aaabb
# Output: ababa 

# Input: aa 
# Output: Not Possible

# Input: aaaabc 
# Output: Not Possible


s='aaabc'
# s='aaa'
li=list(s)
# lii=set(s)
# print("liiiiiiiiiiiiii",lii)
print(li)


if s.count(s[0])==len(s):
    print("Not Possible")
else:
    c=1
    for i in range(len(s)):
        # space=s.count(s[i])
        # print("spaceeeeeeee",space)

        if s.count(s[i])>1 and s[i-1]==s[i]:
            # space=len(li[i])
            c+=1
            
            # li[i+c]=li[i]
            
        
            # print(li[i])
            
            print()
            print("hellooooo",s[i],end='')
            li2=s.remove(s[i])
            print("43",li2)
    print(c)
    

    # for j in range()

    #         print(li[i],end='')
    # print("")
    # print(li[i])
# for i in range(len(li)):
#     # print(li.count(li[i]))
    
#     elif li[i-1]==li[i] and li.count(li[i])!=len(li):
#         print(li[i],end='')


        
        

#2. Program to find string after removing consecutive duplicate characters in Python
# Input
# "xyyyxxz"
# Output
# z

# s="xyyyxxz"
# for i in range(len(s)):
#     if s[i-1] == s[i]:
#         s.remove(i)
