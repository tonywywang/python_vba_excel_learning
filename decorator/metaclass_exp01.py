class mytype(type):
    def __new__(cls, name, bases, clsdict):
        print("new function")
        if len(bases) > 1:
            raise TypeError("NO")
        return super().__new__(cls, name, bases, clsdict)
    
class Base(metaclass=mytype):
    def __init__(self, name):
    	print("init function")
    	self.name = name

class A(Base):
    pass

class B(Base):
    pass

#since C inherits from A and B, the metaclass len(bases) > 1 meets
#class C(A,B):
#    pass

ins_a = A("ClassInstance")