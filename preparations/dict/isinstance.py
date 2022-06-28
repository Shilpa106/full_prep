test_int=5
test_list=[1,2,3]

# # testing with isinstance
# print("is test_int integer?:" +str(isinstance(test_int,int)))
# print("is test_int string?:" +str(isinstance(test_int, str)))
# print("is test_list integer?:"+str(isinstance(test_list,int)))
# print("is test_list list?:" +str(isinstance(test_list,list)))

# # testing with tuple
# print("is test_int integer or list or string?:" +str(isinstance(test_int,(list, int))))


# # Example 2: Demonstrating the use of isinstance() with objects 

# class gfg1:
#     a=10

# # inherited class
# class gfg2(gfg1):
#     string='GeeksforGeeks'

# # initializing object
# obj1=gfg1()
# obj2=gfg2()

# # checking instance
# print("is obj1 instance of gfg1:" + str(isinstance(obj1, gfg1)))
# print("is obj1 instance of gfg2:" + str(isinstance(obj1, gfg2)))
# print("is obj2 instance of gfg2:" + str(isinstance(obj2, gfg2)))

# # check inheritance case return true 
# print("is obj2 instance of gfg1?:" +str(isinstance(obj2, gfg1)))


# # Example 3: Python isinstance array
# test_list=[1,2,3]
# print("Is test_list list? : " +str(isinstance(test_list,list)))


# # Example 4: Python isinstance string
# test_str='GeeksforGeeks'
# print("is test_str? : " +str(isinstance(test_str,str)))

# # Example 4: Python isinstance dict
# test_dict={'apple':1,'ball':2}
# print("is test_str dictionary?: " + str(isinstance(test_dict,dict)))


# Example 4: Python isinstace class methods 
class geeks:
    course='DSA'

    def purchase(obj):
        return obj.course

geeks.purchase=classmethod(geeks.purchase)
print(str(isinstance(geeks.purchase(),str)))


