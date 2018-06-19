#Class Definition 1st version:
#class Stock:
#    def __init__(self, name, shares, price):
#        self.name = name
#        self.shares = shares
#        self.price = price
#
#class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#class Address:
#    def __init__(self, hostname, port):
#        self.hostname = hostname
#        self.port = port
#
#Is there a way to simplify the class definition especially for setting attr in __init__ function
#See the improved version below
class Structure:
    _fields = []
    def __init__(self, *args):
        for name, val in zip(self._fields, args):  #zip(list1, list2) = [(list1[0], list2[0]), (list1[1], list2[1]), ...]
            setattr(self, name, val)  #setattr(object, name, val) equals object.name = val

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

class Address(Structure):
    _fields = ['hostname', 'port']
