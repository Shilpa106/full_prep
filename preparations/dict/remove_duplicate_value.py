
# ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}

# print("initial_dictionary", str(ini_dict))

# rev_dict = {}

# for key, value in ini_dict.items():
#     # print(key,value)
# # a 1
# # b 2
# # c 3
# # d 2
# 	rev_dict.setdefault(value, set()).add(key)
#     # print(key,value)

# # print(rev_dict)


# result = [value for key, value in rev_dict.items()
# 							if len(value) > 1]

# # # printing result
# print("duplicate values", str(result))



# m2
# ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}
  
# # printing initial_dictionary
# print("initial_dictionary", str(ini_dict))
  
# # finding duplicate values
# # from dictionary using flip
# flipped = {}
  
# for key, value in ini_dict.items():
#     if value not in flipped:
#         flipped[value] = [key]
#     else:
#         flipped[value].append(key)
  
# # printing result
# print("final_dictionary", str(flipped))


# Removing duplicate dicts in list
# i/p: [{'Akash': 1}, {'Kil': 2}, {'Akshat': 3}, {'Kil': 2}, {'Akshat': 3}]

# o/p: [{'Akash': 1}, {'Kil': 2}, {'Akshat': 3}]


# test_list = [{"Akash" : 1}, {"Kil" : 2}, {"Akshat" : 3}, {"Kil" : 2}, {"Akshat" : 3}]
  
# # printing original list 
# print ("Original list : " + str(test_list))

# res_list = []
# for i in range(len(test_list)):
#   
#     if test_list[i] not in test_list[i + 1:]:
#         res_list.append(test_list[i])
  
# # printing resultant list
# print ("Resultant list is : " + str(res_list))


# Using list comprehension
# test_list = [{"Akash" : 1}, {"Kil" : 2}, {"Akshat" : 3}, {"Kil" : 2}, {"Akshat" : 3}]

# res_list = [i for n, i in enumerate(test_list) if i not in test_list[n + 1:]]
  
# # printing resultant list
# print ("Resultant list is : " + str(res_list))


# Method #3 : Using frozenset

# test_list=[{"Akash":1},{"kill":2},{"Akshat":3},{"kill":2},{"Akshat":3}]
# # print(test_list)
# res_list={frozenset(item.items()):item for item in test_list}.values()
# print(res_list)


# Remove duplicate values in dictionary
# The original dictionary is : {‘gfg’: 10, ‘for’: 10, ‘geeks’: 20, ‘is’: 15, ‘best’: 20}
# The dictionary after values removal : {‘gfg’: 10, ‘geeks’: 20, ‘is’: 15}
# test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
# # print(test_dict)
# v=[]
# k={}
# for key, value in test_dict.items():
#     if value not in v:
#         v.append(value)
#         k[key]=value
# print(k)
  
# # m2 Using dictionary comprehension
# test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
# # print(test_dict)
# temp={val : key for key, val in test_dict.items()}
# # print(temp)
# res={val:key for key,val in temp.items()}
# print(res)



# from collections import Counter
  
# # initializing dictionary
# test_dict = {'Manjeet' : [1, 4, 5, 6],
#             'Akash' : [1, 8, 9],
#             'Nikhil': [10, 22, 4],
#             'Akshat': [5, 11, 22]}
  
# # printing original dictionary
# print("The original dictionary : " + str(test_dict))
  
# # Remove duplicate values across Dictionary Values
# # Using Counter() + list comprehension
# cnt = Counter()

# # print(test_dict.values())
# for idx in test_dict.values():
#     print(idx)
#     cnt.update(idx)

# print(cnt)
# res = {idx: [key for key in j if cnt[key] == 1] 
#                for idx, j in test_dict.items()}
  
# # printing result 
# print("Uncommon elements records : " + str(res)) 