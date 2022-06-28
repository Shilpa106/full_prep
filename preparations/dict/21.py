# Find Keys with specific suffix in Dictionary
# he original dictionary : {'geeks': 5, 'freaks': 10, 'are': 8, 'all': 4}
# Filtered dictionary keys are : {'geeks': 5, 'freaks': 10}
# # Initialize suffix


test_suf = 'ks'
res={}
test_dict={'geeks': 5, 'freaks': 10, 'are': 8, 'all': 4}
# for key in test_dict:
#     print(key[-2::1])
#     if key[-2::1]=='ks':
#         res[key]=test_dict[key]

# print("final",res)


# # Method #1 : Using dictionary comprehension + endswith()
# res={key:val for key,val in test_dict.items() if key.endswith(test_suf)}
# print(res)

# Method #2 : Using map() + filter() + items() + endswith()

res=dict(filter(lambda item:item[0].endswith(test_suf),test_dict.items()))
print(res)