# Convert List to delimiter separated String
# Given List of elements, convert it to delimiter separated String.

# Input : test_list = [7, “Gfg”, “best”, 9], delim = “*”
# Output : 7*Gfg*best*9*
# Explanation : All elements are concatenated with “*” as joiner.

# Input : test_list = [7, “Gfg”, “best”, 9], delim = “#”
# Output : 7#Gfg#best#9#
# Explanation : All elements are concatenated with “#” as joiner.

# M1 Using loop + str()
test_list = [7, "Gfg", "best", 9]
delim = "*"

# res=''
# for ele in test_list:
#     res=res+str(ele)+delim
# print(res)

# M2: using join()+str()
# using map to convert each element to string
# temp=list(map(str,test_list))
temp=map(str,test_list)
print(type(temp))
res=delim.join(temp)

print(res)
