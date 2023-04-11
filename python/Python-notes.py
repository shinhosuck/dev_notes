# NEXT VIDEO : 4

########
# STRING
########
# Escape \ on string
message = 'bob\'s message.''\n''How cool is this?'

# slicing
s = message[0:5] # from index 0 up to 5, but not including 5.
s1 = message[:5] # from index 0 up to 5, but not including 5.
s2 = message[5:-1] # from 5 up to not including last index
s3 = message[5:] # index 5 to the end

# str methods --> belong to str class.
message_lower = message.lower()
message_upper = message.upper()
message_index = message.index("m")
message_count = message.count("s")
message_find = message.find("me") # gives starting index of "me"
message_replace = message.replace("How cool is this?", "hello world").upper()

greeting = 'Hello' + ' ' + 'world!'
name = "Jack"
g_message = "good moring!"
greeting = name + " " + g_message
greeting = "{0} {1}".format(name, g_message)
greeting = f"{name} {g_message}"

# help() and dir() methods
#print(help(list)) # --> help(class type) or help(str.upper)
#print(dir(name)) # --> dir(object)

########
# NUMBER
########
# Division = 3 / 2
# Floor Division = 3 // 2
# Exponent = 3 ** 2
# Modulus = 3 % 2

# if remainder == 0 then, it is a even number.
# if remainder == 1 then, it is odd number.

abs_num = abs(-10)
round_num = round(31.425, 2)

num = 5
num_type = type(num)
is_instance = isinstance(num, int)

########################
# LIST, TUPLES, AND SETS
########################
list_1 = ["Jack", "Jane", "Matt"]
list_2 = ["Dan", "Jeff"]
# list_1 += list_2
# list_extend = list_1 + list_2
list_1.extend(list_2) # can't set to new variable

