# find the sum of dictionary keys

# Examples:

# test_dict = {3 : 4, 9 : 10, 15 : 10, 5 : 7} 
# Output : 32 
# Explanation : 3 + 9 + 15 + 5 = 32, sum of keys.

test_dict = {3 : 4, 9 : 10, 15 : 10} 
# Output : 27 
# Explanation : 3 + 9 + 15 = 27, sum of keys. 

key_sum=0
for k in test_dict:
    # print(k)
    key_sum+=k

print(key_sum)