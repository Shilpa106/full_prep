# Remove dictionary from a list of dictionaries if a particular value is present
# Examples:

# test_list = [{"Gfg" : 4, "is" : 8, "best" : 9}, {"Gfg" : 3, "is": 7, "best" : 5}]
K = 7 
# Output : [{‘Gfg’: 4, ‘is’: 8, ‘best’: 9}] 
# Explanation : Resultant dictionary doesn’t contain 7 as any element.

# test_list = [{"Gfg" : 3, "is": 7, "best" : 5}]   
# test_list = [{"Gfg" : 4, "is" : 7, "best" : 9},{"Gfg" : 3, "is": 0, "best" : 5}, {"Gfg" : 3, "is": 7, "best" : 5}]
# test_list = [{"Gfg" : 4, "is" : 7, "best" : 9}, {"Gfg" : 3, "is": 7, "best" : 5}]
# test_list = [{"Gfg" : 4, "is" : 7, "best" : 9}, {"Gfg" : 3, "is": 7, "best" : 5},{"Gfg" : 3, "is": 0, "best" : 5}]
test_list = [{"Gfg" : 4, "is" : 7, "best" : 9}, {"Gfg" : 3, "is":7, "best" : 5},{"Gfg" : 3, "is": 9, "best" : 5}, {"Gfg" : 3, "is":7, "best" : 5}]

# K = 7 
# Output : [] 
# Explanation : All contain 7 as element in List. 

K= 7
for i in test_list:
    print("yeeee",i)
    # for key,val in i.items():
        # print(key,val)
        # print(key,val)
    if K in i.values():

        # if val ==K:
        #     print(val)
        test_list.remove(i)
    else:
        print("nooooooooooooo")
#             
print("jj",test_list)

