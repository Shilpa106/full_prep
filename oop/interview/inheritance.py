
# class Person(object):
#     def __init__(self,name):
#         self.name = name
    
#     # to get name
#     def getName(self):
#         return self.name

#     # to check if this person is an employee

#     def isEmployee(self):
#         return False
    

# class Employee(Person):
#     def isEmployee(self):
#         return True 

# emp=Person('Geeks1')
# print(emp.getName(),emp.isEmployee())

# emp1=Employee('Geeks2')
# print(emp1.getName(),emp1.isEmployee())


# task2

# class Person(object):
#     def __init__(self, name,idnumber):
#         self.name = name
#         self.idnumber = idnumber

#     def display(self):
#         print(self.name)
#         print(self.idnumber)


# class Employee(Person):
#     def __init__(self, name,idnumber,salary,post):
#         self.salary = salary
#         self.post = post

#         Person.__init__(self, name, idnumber)

# # creating of  an object variable or an instance
# a=Employee('Rahul',3434,3434,'intern')
# a.display()


# Multiple inheritance

class Base1(object):
    def __init__(self):
        self.str1='Geeks1'
        print('Base1')

class Base2(object):
    def __init__(self):
        self.str2='Geeks2'
        print('Base2')

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print('Derived')

    def printStrs(self):
        print(self.str1, self.str2)

ob=Derived()
ob.printStrs()


