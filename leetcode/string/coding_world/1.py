from numpy import sort


# ****Three sum

# logic
# 1.sort
# 2.i, L=i+1, R=last element
# 3.sumtotal=i+(i+1)+R
# sumtotal=0(target)
#     L=L+1
#     R=R-1
# sumtotal<0
#     L=L+1
# sumtotal>0
#     R=R-1

# sumtotal==0
# op.append(nums[i],nums[L],nums[R])


nums=[-1,0,1,2,-1,-4]
res=[]
nums.sort()
# print(nums)
length=len(nums)
for i in range(length-2):
    if i >0 and nums[i]==nums[i-1]:
        continue
    l=i+1
    r=length-1

    while l<r:
        total=nums[i]+nums[l]+nums[r]
        if total<0:
            l=l+1
        elif total>0:
            r=r-1
        else:
            res.append([nums[i],nums[l],nums[r]])
            while l<r and nums[l]==nums[l+1]:
                l=l+1
            while l<r and nums[r]==nums[r-1]:
                r=r-1

            l=l+1
            r=r-1
print(res)