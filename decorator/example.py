#example.py
from debugly import debug, debugmethods

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
