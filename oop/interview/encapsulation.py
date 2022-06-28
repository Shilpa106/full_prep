
# Encapsulation
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental
# modification of data. To prevent accidental change, an object’s variable can only be changed by an 
# object’s method. Those types of variables are known as private variables.


class Base:
    def __init__(self):
        self.a='GeeksforGeeks'
        self.__c='GeeksforGeeks1'
        
    def show(self):
        print("heyyyyyyyyyyyyy",self.__c)
class Derived(Base):
    def __init__(self):
        # Calling constructor of base class
        Base.__init__(self)
        print("Calling private member of base class:")
        print(self.__c)


obj1=Base()
# print(obj1.a)
# print(obj1.show())

obj2=Derived()
print(obj2.a)