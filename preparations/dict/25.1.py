# Remove dictionary from a list of dictionaries if a particular value is present
# Examples:

# test_list = [{"Gfg" : 4, "is" : 8, "best" : 9}, {"Gfg" : 3, "is": 7, "best" : 5}]
K = 7 
# Output : [{‘Gfg’: 4, ‘is’: 8, ‘best’: 9}] 
# Explanation : Resultant dictionary doesn’t contain 7 as any element.

# test_list = [{"Gfg" : 3, "is": 7, "best" : 5}]
# test_list = [{"Gfg" : 4, "is" : 7, "best" : 9},{"Gfg" : 3, "is": 0, "best" : 5}, {"Gfg" : 3, "is": 7, "best" : 5}]
# test_list = [{"Gfg" : 4, "is" : 7, "best" : 9}, {"Gfg" : 3, "is": 7, "best" : 5}]
test_list = [{"Gfg" : 4, "is" : 7, "best" : 9}, {"Gfg" : 3, "is": 7, "best" : 5},{"Gfg" : 3, "is": 0, "best" : 5}]

# K = 7 
# Output : [] 
# Explanation : All contain 7 as element in List. 

t=[]
for i in range(len(test_list)):
    print(test_list[i])
    for key,val in test_list[i].items():
        print(key,val)
        if val ==K:
            print(val)

            
            test_list.remove(test_list[i])
            # del test_list[i]
# #     #         print(j)
                    
print(test_list)
# t.append(test_list)
# print(t)
