# Sort words separated by Delimiter


# Given string of words separated by some delimiter. The task is to sort all the words given in the string

# Input : test_str = 'gfg:is:best:for:geeks', delim = "*" 
# Output : best*for*geeks*gfg*is 
# Explanation : Words sorted after separated by delim.

# Input : test_str = 'gfg:is:best', delim = "*" 
# Output : best*gfg*is 
# Explanation : Words sorted after separated by delim. 


test_str = 'gfg:is:best:for:geeks'
delim = "*" 
# Output : best*for*geeks*gfg*is
p=test_str.split(':')
print(p)
d=[]
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i][0]<p[j][0]:
            d.append(p[i])
print(d)
    # print(p[i])