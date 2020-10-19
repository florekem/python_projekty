#object-oriented programming

class Employee:             #class
    
    num_of_emps = 0
    raise_amt = 1.04   #class variable
    
    def __init__(self, first, last, pay):   #fist, last, pay = atributes
        self.first = first     #instance variables: are set for each instance of employee that we create
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'    #can be replaced by @property decorator (below)
        
        Employee.num_of_emps += 1 
        
    def fullname(self):    #each method witin a class automaticly takes #instance (eg. emp_1) as a first argument
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)  #class variable call or self.raise_amt
    
    @classmethod  #changes class variables
    def set_raise_amt(cls, amount):   #1st arg is method name
        cls.raise_amt = amount
        
    @classmethod  #alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)   #pass it to __init__ => Employee(first, last, pay)
    
    @staticmethod
    def is_workday(day):    #static methods __do not__ pass instance as first arg
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
        
#    @property    #this way we can replace the self.email from __init__
#    def email(sel):
#        return '{}.{}@email.com'.format(self.first, self.last)
    
    
        
class Developer(Employee): #class that inherits from Employee class all its functionality
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)   #allows to inherit first, last, pay from Employee __init__ method
        # Employee.__init__(self, first, last, pay) will do the same, but super() is better
        self.prog_lang = prog_lang
        
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):  #pass None and change it to a list later, its better than passing changable objects
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []   #if employees are not passed as argument
        else:
            self.employees = employees  #if they are passed as argument
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:  #for emp in mgr_1.employees
            print('-->', emp.fullname())   #dev_1.fullname()
            print('another way -->', Employee.fullname(emp))  # Employee.fullname(dev_1))
            
    
    
    
        
        
        
    
emp_1 = Employee('Corey', 'Schafer', '50000')  #emp_1 is an instance of a class = self
emp_2 = Employee('Test', 'User', '600000')
             
print(emp_1.fullname())           #both are the same thing
print(Employee.fullname(emp_1))

Employee.set_raise_amt(1.05)  #set_raise_amt is a classmethod, it pass itself as first argument

emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(Employee.fullname(new_emp_1))

import datetime
my_date = datetime.date(2018, 10, 29)
dayofwork = Employee.is_workday(my_date)
print(dayofwork)

dev_1 = Developer('Corey', 'Schafer', '50000', 'Python')  #dev_1 is an instance of a class = self
print(dev_1.prog_lang)


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
#mgr_1.add_emp(dev_1)
mgr_1.print_emps()


#print(help(Developer)) #checks order of inheritance



#emp_1.first = 'Corey'        #instance variables
#emp_1.last = 'Schafer'
#emp_1.email = 'Corey.schafer@company.com'
#emp_1.pay = '50000'

#emp_2.first = 'Test'        #instance variables
#emp_2.last = 'User'
#emp_2.email = 'test.user@company.com'
#emp_2.pay = '60000'
