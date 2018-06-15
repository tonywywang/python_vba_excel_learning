#example.py
from debugly import debug, debugmethods, debugattr

@debug(prefix='[Sky Debug]')
def add(x,y):
    return x + y

@debug
def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

@debugmethods
class Spam:
    @debug(prefix='***')
    def a(self):
        pass

    def b(self):
        pass

    #however, the classmethod and staticmethod can not be wrapped
    #@classmethod
    #def grok(cls):
    #    pass
    #@staticmethod
    #def bar():
    #    pass

@debugattr
class AttrExp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
