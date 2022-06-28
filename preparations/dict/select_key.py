# Input : 
# test_dict = {‘gfg’: {‘geeks’: {‘best’ : 3}}} 
# key_list = [‘best’, ‘geeks’] 
# Output : {‘geeks’: {‘best’: 3}, ‘best’: 3}
# Input : 
# test_dict = {‘gfg’: {‘geek’: {‘good’ : 3}}} 
# key_list = [‘best’, ‘geeks’] 
# Output : {} 
 

def get_vals(test_dict, key_list):
    for i, j in test_dict.items():
        print("13",i,j)
        # print(test_dict.items())
        if i in key_list:
            yield (i, j)
        yield from [] if not isinstance(j, dict) else get_vals(j, key_list)
    
# initializing dictionary
test_dict = {'gfg': {'is': {'best' : 3}}, 'for': {'all' : 4}, 'geeks': 5}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# initializing keys list
key_list = ['best', 'geeks']
 
# Extract selective keys' values [ Including Nested Keys ]
# Using recursion + loop + yield
res = dict(get_vals(test_dict, key_list))
 
# printing result
print("The extracted values : " + str(res))

#  The original dictionary is : {'gfg': {'is': {'best': 3}}, 'for': {'all': 4}, 'geeks': 5}
# The extracted values : {'best': 3, 'geeks': 5}

