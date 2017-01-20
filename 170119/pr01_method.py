def my_func():
    global param
    param = 'Modified by my_func'
    print(param)
    print(id(param))

param = 'Create from outside'

my_func()

print(param)
print(id(param))