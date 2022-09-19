# Some basic math formulas to unittest

def add(x, y):
    if not isinstance(x, int) and not isinstance(x, float) or not isinstance(y, int) and not isinstance(y, float):
        raise TypeError("Arguments must be an integer or a float")
    return x + y

def subtract(x, y):
    if not isinstance(x, int) and not isinstance(x, float) or not isinstance(y, int) and not isinstance(y, float):
        raise TypeError("Arguments must be an integer or a float")
    return x - y

def divide(x, y):
    if not isinstance(x, int) and not isinstance(x, float) or not isinstance(y, int) and not isinstance(y, float):
        raise TypeError("Arguments must be an integer or a float")
    return x / y

def multiply(x, y):
    if not isinstance(x, int) and not isinstance(x, float) or not isinstance(y, int) and not isinstance(y, float):
        raise TypeError("Arguments must be an integer or a float")
    return x * y

x = 2.4
print(isinstance(x, float))