# Construct dictionary Key-Value pairs separated by delimiter

# Given a String with key-value pairs separated by delim, construct a dictionary.

# Input : test_str = ‘gfg#3, is#9, best#10’, delim = ‘#’ 
# Output : {‘gfg’: ‘3’, ‘is’: ‘9’, ‘best’: ’10’} 
# Explanation : gfg paired with 3, as separated with # delim.
# Input : test_str = ‘gfg.10’, delim = ‘.’ 
# Output : {‘gfg’: ’10’} 
# Explanation : gfg paired with 10, as separated with . delim. 
 

# Method #1 : Using split() + loop

# In this, we perform a split on comma, to get key value pairs, and again a split on custom delim to get key value pairs separated.
#  Then assigned to dictionary using loop.

test_str = 'gfg#3, is#9, best#10'

res=dict(item.split("#") for item in test_str.split(", "))
#  dict(item.split("=") for item in test_str.split(", "))
print(res)

