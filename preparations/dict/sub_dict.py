# create a sub-dictionary containing all keys from dictionary list
# Input : test_list = [{‘gfg’ : 3, ‘is’ : 7}, {‘gfg’ : 3, ‘is’ : 1, ‘best’ : 5}, {‘gfg’ : 8}]

# Output : [{‘is’: 7, ‘best’: None, ‘gfg’: 3}, {‘is’: 1, ‘best’: 5, ‘gfg’: 3}, {‘is’: None, ‘best’: None, ‘gfg’: 8}]

# Explanation : The items with “is” and “best” are added to all lists, wherever missing as None if no values populated.

# Input : test_list = [{‘gfg’ : 3}, {‘gfg’ : 3, ‘best’ : 5}, {‘gfg’ : 8}]

# Output : [{‘best’: None, ‘gfg’: 3}, {‘best’: 5, ‘gfg’: 3}, {‘best’: None, ‘gfg’: 8}]

# Explanation : The items with “best” are added to all lists, wherever missing as None if no values populated.

#  Method #1 : Using set() + chain.from_iterable() + get() + list comprehension
# from itertools import chain
# test_list=[{'gfg':3,'is':7},
#            {'gfg':3,'is':1,'best':5},
#            {'gfg':8}]
# # print(test_list)
# all_keys=set(chain.from_iterable(test_list))

# # print(all_keys)
# res=[dict((key,sub.get(key,"empty")) for key in all_keys) for sub in test_list]
# print(res)



# ex
# for sub in test_list:
#     print(sub)
    # for key in all_keys:
    #     print(key,sub.get(key,None))


# Method #2 : Using set() + chain.from_iterable() + update()

# from itertools import chain
# test_list =[{'gfg':3, 'is':7},
#             {'gfg':3,'is':1,'best':5},
#             {'gfg':8}]

# # print(test_list)
# all_keys=set(chain.from_iterable(test_list))
# print(all_keys)
# for sub in test_list:
#     # print(sub)
#     sub.update({key:None for key in all_keys if key not in sub})
# print(test_list)