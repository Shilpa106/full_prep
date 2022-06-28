test_list = [{"Gfg" : 4, "is" : 8, "best" : 9},
             {"Gfg" : 5, "is": 7, "best" : 1},
             {"Gfg" : 3, "is": 7, "best" : 6}, 
             {"Gfg" : 3, "is": 7, "best" : 5}]
  
# printing original list
print("The original list : " + str(test_list))
  
# initializing K 
K = 7
  
res = []

# M1 
# using loop to check for K element 
# for sub in test_list:
#     print(list(sub.values()))
#     if K not in list(sub.values()):
#         res.append(sub)
  
# # printing result 
# print("Filtered dictionaries : " + str(res))

# M2
dat=[i for i in test_list if 7 not in i.values()]
print(dat)