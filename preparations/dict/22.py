# Find dictionary keys present in a Strings List
# The original list is : ['GeeksforGeeks is best for geeks', 'I love GeeksforGeeks']
# The matching keys list : [['best', 'Geeks'], ['love', 'Geeks']]

from shlex import join


test_list = ['GeeksforGeeks is best for geeks', 'I love GeeksforGeeks']
final_list= [['best', 'Geeks'], ['love', 'Geeks']]
test_dict = {'Geeks' : 5, 'CS' : 6, 'best' : 7, 'love' : 10}
res=[]
resu=[]

# a=[[key] for key in test_dict for k in test_list if key in k]
# print(a)
k_l=[]
l=[]
for i in test_list:
    for j in test_dict:
        if j in i:
            # print(j)
            k_l.append(j)
    
    print(k_l)
#     res.append(res1)
#             # print(resu)
#     resu.append(res)

# print(resu)
