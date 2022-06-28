# static and class method

class Employee:
    NO_OF_EMPLOYEES=0

    def __init__(self, first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.increment_employees()

    def give_raise(self,amount):
        self.salary += amount


    @classmethod
    def employee_from_full_name(cls, full_name,salary):
        split_name=full_name.split(' ')
        first_name=split_name[0]
        last_name=split_name[1]
        return cls(first_name,last_name,salary)
        

    @classmethod
    def increment_employees(cls):
        cls.NO_OF_EMPLOYEES+=1

    @staticmethod
    def get_employee_legal_obligations_txt():
        legal_obligations="""
        1. An employee must complete 8 hours per working day
        2. ...
        """
        return legal_obligations

employee_1=Employee('Andrew','Brown',85000)
print(f'Number of employees:{Employee.NO_OF_EMPLOYEES}')
print(employee_1.first_name)
print(employee_1.last_name)
print(employee_1.salary)

employee_2=Employee.employee_from_full_name('John Black', 95000)
print(f'Number of employees:{Employee.NO_OF_EMPLOYEES}')

print(employee_2.first_name)
print(employee_2.salary)


# A static method can be accessed directly from the class
print(Employee.get_employee_legal_obligations_txt())

# or from an instance of the class
employee1=Employee('ram','fd',3434)
print(employee1.get_employee_legal_obligations_txt())
