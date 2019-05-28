class A:
    def __init__(self):
        self._age = 10
        self._height = 20
    def __repr__(self):
        return "class A __repr__ method"
a1 = A()
print(a1)  # class A __repr__ method