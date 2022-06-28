
class Employee:
    NO_OF_EMPLOYEE = 0
    def __init__(self,first_name, last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.increment_employee()

    def give_raise(self,amount):
        self.salary+=amount
    
    @classmethod
    def increment_employee(cls):
        cls.NO_OF_EMPLOYEE+=1

    @classmethod
    def full_name_from_employee(cls,full_name,salary):
        split_name=full_name.split(' ')
        first_name=split_name[0]
        last_name=split_name[1]
        return cls(first_name,last_name,salary)
    
    @staticmethod
    def get_oblligations_text():
        legal_obligations="""
        An employee must complete 8 hour per working day
        """
        return legal_obligations
        

    