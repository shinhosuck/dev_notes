

def some_func(a, *args, **kwargs):
    arg = args
    return kwargs


a = "snake"
b = "elephant"
c =  b=a

data = some_func(a, b, c)
print(data)
