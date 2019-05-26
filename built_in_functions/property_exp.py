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