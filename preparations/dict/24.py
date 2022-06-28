# convert Dictionary to List by Repeating keys corresponding value times

# Input : test_dict = {'g' : 1, 'f' : 3, 'g' : 1, 'b' : 4, 'e' : 1, 's' : 4, 't' : 3}

# Output : ['g', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'e', 's', 's', 's', 's', 't', 't', 't']

# Explanation : f is added 3 times in list.

# Input : test_dict = {'g' : 1, 'f' : 3, 'g' : 1, 'b' : 4, 'e' : 1}

# Output : ['g', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'e']

# Explanation : f is added 3 times in list.

test_dict = {'g' : 1, 'f' : 3, 'g' : 1, 'b' : 4, 'e' : 1, 's' : 4, 't' : 3}
t=[]
res=[]
for k,v in test_dict.items():
    res.append(k*v)
#     print(k,v)
print(res)
for i in range(len(res)):
    print(res[i])

