# group keys with similar values in a dictionary
# Input : test_dict = {'Gfg': [5, 6], 'is': [8, 6, 9], 'best': [10, 9], 'for': [5, 2], 'geeks': [19]} 
# Output : [[‘Gfg’, ‘is’, ‘for’], [‘is’, ‘Gfg’, ‘best’], [‘best’, ‘is’], [‘for’, ‘Gfg’]] 
# Explanation : Gfg has 6, is has 6, and for has 5 which is also in Gfg hence, grouped.

# Input : test_dict = {'Gfg': [6], 'is': [8, 6, 9], 'best': [10, 9], 'for': [5, 2]} 
# Output : [[‘Gfg’, ‘is’], [‘is’, ‘Gfg’, ‘best’], [‘best’, ‘is’]] 
# Explanation : Gfg has 6, is has 6, hence grouped. 

test_dict = {'Gfg': [5, 6], 'is': [8, 6, 9], 'best': [10, 9], 'for': [5, 2], 'geeks': [19]} 
# Method : Using loop + any() + len()
res=[]
for key  in test_dict:
    print("key",key)
    chr=[key]
    for ele in test_dict:
        print("ele", ele)
        # check with other keys
        if key!=ele:
            # checking for any match in Values
            print("21",test_dict[key])
            if any(i==j for i in test_dict[key] for j in test_dict[ele]):
                chr.append(ele)
        
    if len(chr)>1:
        res.append(chr)
print(res)

