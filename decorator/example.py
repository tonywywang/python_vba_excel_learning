#example.py
from debugly import debug

@debug
def add(x,y):
    return x + y

@debug
def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y
