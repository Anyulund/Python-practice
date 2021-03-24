# General form 
def add(x,y):
    total = x + y 
    return total 

# Optimized form 
def add_optimized(x, y):
    return x + y 

# When there is no return statement, the function returns none 
def foo(): 
    pass 

print(foo())

# When return has to value, the function returns None 
def return_none():
    return 

print(return_none())

# Multiple return statements 
def type_of_init():
    if  i % 2 == 0:
        return 'even'
    else:
        return 'odd'

# Multiple return values 
def get_demo_data(object_type):
    if 'str' == object_type:
        return 'test'
    elif 'tuple' == object_type:
        return (1,2,3)
    elif 'list' == object_type:
        return [1,2,3]
    elif 'dict' == object_type:
        return {'1':1, '2':2,'3':3}
    else:
        return None

# Multiple return statements in a single return statement
def return_multiple_values():
    return 1,2,3

print(return_multiple_values())
print(type(return_multiple_values()))

# Return statement with finally block 
def hello():
    try:
        return 'hello try'
    finally: 
        print('finally block')

def hello_new():
    try:
        raise TypeError
    except TypeError as te:
        return 'hello except'
    finally: 
        print('finally block')

print(hello())
print(hello_new())

# If finally has return statement, then it stops at finally 

def hello_return():
    try:
        return 'hello cry'
    finally:
        print('finally block')
        return 'hello from finally'

print(hello_return())

