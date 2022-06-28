# Unique value keys in a dictionary with lists as values

# # Method #1 : Using loop + count()
test_dict={'Gfg':[6,5],'is':[6,10,5],'best':[12,6,5]}
# temp=[sub for ele in test_dict.values() for sub in ele]
# print("temp",temp)
# res=[]
# for key, vals in test_dict.items():
#     for val in vals:
#         if temp.count(val)==1:
#             print("val",val)
#             res.append(key)
#             break
# print(res)

# Method #2 : Using list comprehension + any() + count()
res = [key for key, vals in test_dict.items() if any([ele for sub in test_dict.values()
       for ele in set(sub)].count(idx) == 1 for idx in vals)]
  
# printing result 
print("The unique values keys are : " + str(res)) 
