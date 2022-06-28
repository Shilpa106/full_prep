test_list = [{"Gfg" : 4, "is" : 7, "best" : 9}, {"Gfg" : 0, "is":6, "best" : 5}, {"Gfg" : 8, "is":7, "best" : 5}]

a=[dict_data for dict_data in test_list if 7 in dict_data.values()]
print(a)
for i in [dict_data for dict_data in test_list if 7 in dict_data.values()]:
    print('ii',i)
    if i in test_list:
        # print('i2222',i)
        test_list.remove(i)
    print(test_list)
    