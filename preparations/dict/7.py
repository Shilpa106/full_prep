# Test if Values Sum is Greater than Keys Sum in dictionary
# Input : test_dict = {5:3, 1:3, 10:4, 7:3, 8:1, 9:5} 
# Output : False 
# Explanation : Values sum = 19 < 40, which is key sum, i.e false.

# Input : test_dict = {5:3, 1:4} 
# Output : True 
# Explanation : Values sum = 7 > 6, which is key sum, i.e true. 

# # Method #1: Using loop
test_dict = {5:3, 1:3, 10:4, 7:3, 8:1, 9:5}
# key_sum=0
# val_sum=0
# for key in test_dict:
#     key_sum +=key
#     val_sum +=test_dict[key]
#     print(key)
# res=val_sum>key_sum
# print(res)


# Method #2 : Using sum() + values()  + keys()
res=sum(list(test_dict.keys()))<sum(list(test_dict.values()))
print(res)