# display keys with same values in a dictionary List
# Input : test_list = [{'Gfg': 5, 'is' : 8, 'best' : 0}, {'Gfg': 5, 'is' : 1, 'best' : 0}, {'Gfg': 5, 'is' : 0, 'best' : 0}] 
# Output : [‘Gfg’, ‘best’] 
# Explanation : All Gfg values are 5 and best has 0 as all its values in all dictionaries.

# Input : test_list = [{'Gfg': 5, 'is' : 8, 'best' : 1}, {'Gfg': 5, 'is' : 1, 'best' : 0}, {'Gfg': 5, 'is' : 0, 'best' : 0}] 
# Output : [‘Gfg’] 
# Explanation : All Gfg values are 5. 
 
test_list = [{'Gfg': 5, 'is' : 8, 'best' : 1}, {'Gfg': 5, 'is' : 1, 'best' : 0}, {'Gfg': 5, 'is' : 0, 'best' : 0}]
# test_list = [{'Gfg': 5, 'is' : 8, 'best' : 0}, {'Gfg': 5, 'is' : 1, 'best' : 0}, {'Gfg': 5, 'is' : 0, 'best' : 0}] 
# keys=list(test_list[0].keys())
# res=[]

# for key in keys:
#     flag=1
#     # print(k)
#     # print(key)
#     for ele in test_list:
#         if test_list[0][key]!=ele[key]:
#             flag=0
#             break

#     if flag:
#         res.append(key)

# print(res)


# Method 2 : Using all(), loop and keys()
keys = list(test_list[0].keys())
res = []
for key in keys:
    flag=all(test_list[0][key] == ele[key] for ele in test_list)
    if flag:
        res.append(key)
print(res)