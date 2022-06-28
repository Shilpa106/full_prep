# Two sum
num=[2,4,11,15,2]
target=6
# num[0]+num[1]=2+7=9
# return [0,1]

# first approach
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j] ==target:
            print(i,j)



# second approach
