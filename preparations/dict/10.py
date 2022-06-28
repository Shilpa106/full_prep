# Assign values to initialized dictionary keys
# # Method #1 : Using dict() + zip()
test_dict = {'gfg' : '', 'is' : '', 'best' : ''} 
  
# # Initializing list 
test_list = ['A', 'B', 'C']
# res=dict(zip(test_dict, test_list))
# print(res)

# Method #2 : Using loop + zip()
for key,val in zip(test_dict,test_list):
    test_dict[key] = val
print(test_dict)

