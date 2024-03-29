
class Employee:

    # this class variable/attribute gets automatically inherited by instances.
    raised_amount = 1.04
    num_of_emp = 0


    # 'initialize'-> it sets up class / attributes automatically
    def __init__(self, first, last, salary, age):
        self.first = first
        self.last = last
        self.salary = salary
        self.age = age
        self.email = f'{first}{last}@mail.com'

        # Important
        # when a new instance of a class is created, '__init__' keeps track
        # number of instances-when '__init__' method is initialized.
        Employee.num_of_emp +=1

    def full_name(self):
        emp_fullname = '{0} {1}'.format(self.first, self.last)
        return emp_fullname

    def apply_raise(self):
        # class attribute 'raise_amount' is automatically inherited.
        # That is why 'self.raise_amount' works.
        montly_salary = self.raised_amount * (self.salary / 12)
        # or
        # annual_salary = Employee.apply_raise * self.salary
        # also can use class 'Employee.raise_amount'.
        return montly_salary

    # class method with decorator
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raised_amount = amount

    @classmethod
    def from_emp_string(cls, emp_str):
        first, last, salary, age, pro_lang= emp_str.split('-')
        new_emp = cls(first, last, salary, age, pro_lang)
        return new_emp

    @staticmethod
    def is_pay_day(date):
        if date.weekday() == 2:
            return True
        return False

class Developer(Employee):

    def __init__(self, first, last, pay, age, pro_lang):
        super().__init__(first, last, pay, age)
        # Employee.__init__(self, first, last, pay, age)

        self.pro_lang = pro_lang

# these are instances of a class --> Employee
emp1 = Developer('Jack', 'Smith', 50000, 33, 'python')
emp2 = Developer('Dan', 'Jackson', 50000, 45, 'C++')

print(emp1.full_name())
print(Employee.full_name(emp2))
print(emp1.email)
print(emp2.email)

# creating instances variable/attributes maually is redundent and bad way
# instead use 'def __init__(self) method'
# emp1.first = 'Jack'
# emp1.last = 'Smith'
# emp1.email = f'{emp1.first}{emp1.last}@mail.com'

# emp2.first = 'Jane'
# emp2.last = 'Does'
# emp2.email = 'jane_does@mail.com'

# instance variables = employee's first_name, last_name, age and so forth ---> these are alll unique and
# and each instance is unique.

# CLASS VARIABLE
# -class variables are shared by each instances,
# which means that each instances get same variable with data attatched to it.
# -instance variables are unique for each instances

print(Employee.num_of_emp)
print('Monthly salary:' + str(emp1.apply_raise()))
Employee.raised_amount = 1.00
print('Monthly salary:' + str(emp1.apply_raise()))

# CLASS METHOD AND STATIC MEHTOD:
emp1.raised_amount = 1.10

# class method
Employee.set_raise_amount(1.05)

print(emp1.raised_amount)
print(emp2.raised_amount)

# class method as constructor
emp3_string = 'Don-Julio-60000-45-JS'
emp3 = Developer.from_emp_string(emp3_string)

print(emp3.first)

# static method
import datetime
date = datetime.date(2022, 11, 23)
pay_date = Employee.is_pay_day(date)
print(pay_date)

# CLASS INHERITANCE
