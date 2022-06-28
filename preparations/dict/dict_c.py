
# Python - Append Dictionary Keys and Values ( In order ) in dictionary
# Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3}
# Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3]

# test_dict = {"gfg" : 1, 'is' : 2, 'best' : 3}
# res=list(test_dict.keys())+list(test_dict.values())
# # print(res)


# # m2 using chain
# from itertools import chain
# res2=list(chain(test_dict.keys(),test_dict.values()))
# print(res2)


#  Remove duplicate values across Dictionary Values
# Input : test_dict = {‘Manjeet’: [1], ‘Akash’: [1, 8, 9]}
# Output : {‘Manjeet’: [], ‘Akash’: [8, 9]}

# Input : test_dict = {‘Manjeet’: [1, 1, 1], ‘Akash’: [1, 1, 1]}
# Output : {‘Manjeet’: [], ‘Akash’: []}

