# l = {'a':10, 'b':20}
# # print('{a}, {b}'.format(**l))

# my_list = ['cat', 'dog', 'rat', 'fish']

# index = 0

# for num in range(0, len(my_list)):
#     # print(num)
#     index = num
# # print('{}'.format(my_list[index]))

# def my_func(*args, **kwargs):
#     # print('args:', *args)
#     # print('kwargs:', **kwargs)
#     return
# my_func(my_list)
# my_func('cat', 'dog', 'rat')

# a = 1
# b = 'hello'
# data = None


# try:
#     data = my_list[5]
# except IndexError as e:
#    print(e)
# else:
#     print(data)
# finally:
#     print('Loading data .......')
# else:
#     print("no data")
# # print(is_instance)

# Important-- go back and see video 27
# # Next Video 21 and 30


# PYTHON OOP TUTORIALS
# CLASS AND INSTANCES
# --datas and functions = attributes and methods

# Class definition:
    # class is a blueprint for creating instances.

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

    # class method
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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raised_amount = amount

# these are instances of a class --> Employee
emp1 = Employee('Jack', 'Smith', 50000, 33)
emp2 = Employee('Dan', 'Jackson', 50000, 45)

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

# print(emp1.email)
# print(emp2.email)

# using class method/function to get emp's full name and etc...
print(emp1.full_name())

# using class to get emp's full name
# this is what is happening in the back of python
print(Employee.full_name(emp2))

# CLASS VARIABLE
# -class variables are shared by each instances,
# which means that each instances get same variable with data attatched to it.
# -instance variables are unique for each instances

print(emp1.apply_raise())
print(Employee.num_of_emp)
print(emp1.num_of_emp)
Employee.num_of_emp = 1.05
print('Monthly salary:' + str(emp1.apply_raise()))
print(Employee.num_of_emp)
Employee.raised_amount = 1.00
print('Monthly salary:' + str(emp1.apply_raise()))

# CLASS METHOD AND STATIC MEHTOD:
emp1.raised_amount = 1.10
Employee.set_raise_amount(1.05)

print(emp1.raised_amount)
print(emp2.raised_amount)
