
# Data hiding
# in python we use double underscore (or __) before the attribute name and those attributes will 
# not be directly visible outside.

# class MyClass:
#     # hidden member of myclass
#     __hiddenVariable=0

#     # A member method that changes __hiddenVariable
#     def add(self,increment):
#         self.__hiddenVariable+=increment
#         print(self.__hiddenVariable)

# myObject=MyClass()
# myObject.add(2)
# myObject.add(5)
# print(myObject.__hiddenVariable)



# Access hidden variable
class MyClass:
    __hiddenVariable=10

myObject=MyClass()
print(myObject._MyClass__hiddenVariable)