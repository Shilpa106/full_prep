
# Dictionary Keys whose Values summation equals K
# Input : {'Gfg' : 3, 'is' : 5, 'Best' : 9, 'for' : 8, 'Geeks' : 10}, K = 17
# Output : [‘Best’, ‘for’]
# Explanation : 9 + 8 = 17, hence those keys are extracted.

# Input : {'Gfg' : 3, 'is' : 5, 'Best' : 9, 'for' : 8, 'Geeks' : 10}, K = 19
# Output : [‘Best’, ‘Geeks’]
# Explanation : 9 + 10 = 19, hence those keys are extracted.

my_dict={'Gfg' : 3, 'is' : 5, 'Best' : 9, 'for' : 8, 'Geeks' : 10}
# k=17
# keys=list(my_dict.keys())
# values=list(my_dict.values())

# res=None
# for i in range(len(keys)):
#     for j in range(i+1,len(keys)):
#         if values[i]+values[j]==k:
#             res=[keys[i],keys[j]]
# print(res)


# Method #2 : Using list comprehension 
k=14
keys=list(my_dict.keys())
values=list(my_dict.values())

res=[[keys[i],keys[j]] for i in range(len(keys)) for j in range(i+1,len(keys)) if values[i]+values[j]==k]
print(res)

