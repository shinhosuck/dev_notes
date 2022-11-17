l = {'a':10, 'b':20}
# print('{a}, {b}'.format(**l))

my_list = ['cat', 'dog', 'rat', 'fish']

index = 0

for num in range(0, len(my_list)):
    # print(num)
    index = num
# print('{}'.format(my_list[index]))

def my_func(*args, **kwargs):
    # print('args:', *args)
    # print('kwargs:', **kwargs)
    return
my_func(my_list)
my_func('cat', 'dog', 'rat')

a = 1
b = 'hello'
data = None


try:
    data = my_list[5]
except IndexError as e:
   print(e)
else:
    print(data)
finally:
    print('Loading data .......')
# else:
#     print("no data")
# # print(is_instance)
# # Next Video 21 and 26
