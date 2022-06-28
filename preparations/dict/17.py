# update a dictionary with the values from a dictionary list

# Input : test_dict = {'Gfg' : 2, 'is' : 1, 'Best' : 3}, dict_list = [{‘for’ : 3, ‘all’ : 7}, {‘and’ : 1, ‘CS’ : 9}] 
# Output : {‘Gfg’: 2, ‘is’: 1, ‘Best’: 3, ‘for’: 3, ‘all’: 7, ‘and’: 1, ‘CS’: 9} 
# Explanation : All dictionary keys updated in single dictionary.

# Input : test_dict = {'Gfg' : 2, 'is' : 1, 'Best' : 3}, dict_list = [{‘for’ : 3, ‘all’ : 7}] 
# Output : {‘Gfg’: 2, ‘is’: 1, ‘Best’: 3, ‘for’: 3, ‘all’: 7} 
# Explanation : All dictionary keys updated in single dictionary. 


# test_dict = {"Gfg" : 2, 'is' : 1, 'Best' : 3}
# dict_list = [{'for' : 3, 'all' : 7}, {'and' : 1, 'CS' : 9}]

# for i in dict_list:
#     test_dict.update(i)
# print("d111111111",test_dict)



# Method #2 : Using ChainMap + ** operator

from collections import ChainMap
 
# initializing dictionary
test_dict = {'Gfg' : 2, "is" : 1, "Best" : 3}


print({**test_dict})
 
# initializing dictionary list
dict_list = [{'for' : 3, 'all' : 7}, {'geeks' : 10}, {'and' : 1, 'CS' : 9}]

# # ** operator extracts keys and re initiates.
# # ChainMap is used to merge dictionary list
print({**dict(ChainMap(*dict_list))})
res = {**test_dict, **dict(ChainMap(*dict_list))}
 
# printing result
print("The updated dictionary : " + str(res))