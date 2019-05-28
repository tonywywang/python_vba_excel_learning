class A:
    def __init__(self):
        self._age = 10
        self._height = 20
    def __repr__(self):
        return "class A __repr__ method"
a1 = A()
print(a1)  # class A __repr__ method

class A1:
    def __init__(self):
        self._age = 10
        self._height = 20
    def __repr__(self):
        return "class A __repr__ method"
    def __str__(self):
        return "Age:" + str(self._age) + " Height:" + str(self._height) 
a2 = A1()
print(a2) # Age:10 Height:20
repr(a2)  # class A __repr__ method