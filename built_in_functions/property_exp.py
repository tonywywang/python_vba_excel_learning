class C:
    def __init__(self):
        print("class C init func\n")
        self._x = None
    def getx(self):
        print("get x value\n")
        return self._x
    def setx(self, value):
        print("set x value to %d\n" % value)
        self._x = value
    def delx(self):
        print("del x\n")
        del self._x
    x = property(getx, setx, delx, "I am 'x' property!")
c1 = C()
print(c1.x)
c1.x = 2
print(c1.x)
del c1.x
#print(c1.x)  Exception Error since there is no x property

class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage
p1 = Parrot()
print(p1.voltage)  # 100000

class C1:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
c1 = C1()
c1.x = 100
print(c1.x)
del c1.x