from itertools import chain

# res=list(chain('ABC','DEF','GHI','JKL'))
# print(res)


# M2
# str1='Geeks'
# str2='for'
# str3='geeks'
# res=list(chain(str1, str2, str3))
# print(res)
# ans=''.join(res)
# print(ans)



# # chain.from_iterable() function
# li=['ABC','DEF','GHI','JKL']
# # USING CHAIN SINGLE ITERABLE
# res1=list(chain(li))
# # print(res1)
# res2=list(chain.from_iterable(li))
# print(res2)


# Example 6: Now consider a list like the one given below : 

li=['123', '456', '789']
# You are supposed to calculate the sum of the list taking every single digit into account. So the answer should be : 

# 1+2+3+5+6+7+8+9 = 45
res=list(chain.from_iterable(li))
# print(res)
new_res=list(map(int,res))
# print(new_res)
sum_of_li=sum(new_res)
print(sum_of_li)
