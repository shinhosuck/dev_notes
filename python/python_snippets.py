
import re
import uuid
import json
from textwrap import dedent
from pathlib import Path

# loads(), dumps(), decode(), encode()
a = {'name':'jack', 'age': 33}

json_string = json.dumps(a) # a gets converted to string dict/json

back_to_json = json.loads(json_string) # back to dict/json

convert_to_bytes = json_string.encode('utf-8') # convert string into bytes

convert_byte_to_string = convert_to_bytes.decode('utf-8') # convert bytes into string

# STRING
# escape
message = 'bob\'s message.''\n''How cool is this?'
escape_quote = 'bob\'s
new_line = 'can\'t do this.\nWhat is the solution?'
tab_line = '\tcan\'t do this.' -> this adds 4 tabs.

# slice
# [start:end]
s = message[0:5] # from index 0 up to 5, but not including 5.
s1 = message[:5] # from index 0 up to 5, but not including 5.
s2 = message[5:-1] # from 5 up to not including last index
s3 = message[5:] # index 5 to the end

# concatenation
greeting = 'Hello' + ' ' + 'world!'
name = "Jack"
g_message = "good moring!"
greeting1 = name + " " + g_message

# methods
lower()
upper()
index()
count()
find()
replace()
''.join()


# LIST
# list methods
split()


# Python built in functions
isinstance()
abs()
round()
type()
extend()
dir()
vars()
set()
f''
'some_variable' in locals()
'some_variable' in globals()
hasattr(obj, 'save')
ord()
chr()
example: allowed_chars = [chr(num) for num in range(ord('a'), ord('z')+1)]
isalpha()
# Regex
re.search()
re.findall()


# UUID
uuid.uuidv4()

# Add comma to numbers
price = 2500
'{0:,}'.format(price)
f'{some_value:,.2f}'

# List methods
extend()

# Dictionary
items()
get()
defaultdict()
setdefault()

# Combine 2 objects:
a = {'name':'jack'}
b = {'age': 33}

a |= b # this combines 2 dict (only the unique keys)

# Create class using type()
"""
Under the hood all classes are created using type:
    - type() class is created using C/cpython
    - python initializes type() instance:
        - type(name, (object,), {'name':'Jack','method1':'get_username'})
        - name=class_name, bases(parent_class/inheritance)=(object,), attrs={'name':'Jack','method1':'get_username'}

    Important Note:
        on type() instance creation, type.__new__(cls, name, bases, attrs) gets called to create/register the class

Builtin object class:
    - object class __new__() as well
    - on class initialization, object's __new__() method gets called to create/register the instance
"""
type('name_of_class':str, ('parent_class'):tuple, {'attributes_and_methods'}:dict)

# Make a module stand alone app:
"""
1. Add shebang:
    #!/usr/bin/python3 -> Python off OS
    #!/usr/bin/env/ python3 -> Python off venv

    -with shebang this module beccomes excutable:
        1. module permission need to be changed:
            -chmod +x mymodule.py
        2. do not need python3 infront of mymodule.py
            -./mymodule.py -> . dot indicates current root dir

2. add name & main:
    if __name__ == '__main__':
        -This line gets run when the module is ran via terminal

3. sample stand alone module/app:

    import sys

    note: when arg is passeds using terminal sys.argv can be use to get the args
        - args = sys.argv -> this gives list [mymodule.py(module name), 'hello'(argument)]
        - data = args[1] -> get only the passed argument

    #!/usr/bin/env python3

    def get_username(username):
        return username

    if __name__ == '__main__':
        username = sys.argv[1]
        name = get_username(username)

"""

# Create file dir using Path class
path = Path(__file__).resolve() #current file absolute path
path = Path(__file__).resolve().parent #use parent to traverse to other dirs.

"""
Example:
    MyProject:
        dir1
            my_file.py
        dir2
            utils.py

path = Path(__file__).resolve() -> current file absolute path
path = Path(__file__).resolove().parent -> my_file.py parent folder path
path = Path(__file__).resolove().parent.parent -> This is the root of the project path
"""






















