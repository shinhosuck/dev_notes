
import re
import uuid


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
