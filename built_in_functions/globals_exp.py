def F():
    global x
    x = 1
    print(x)
def G():
    x = 2
    globals()["x"] = 100
    print(globals()["x"])
def H():
    x = 3
    print(x)
    print(globals()["x"])
F()  # 1
G()  # 100
H()  # 3 100

x = 100
def foo():
	# x = 2   if this is uncommented, y = 3 locals variable is used
    y = eval("x + 1", globals(), locals())
    print("y=", y) # should be 3
foo()  # 101

class C:
    def __init__(self, x):
        self.x = x
        print("x = ", self.x)
def call(str):
    return globals()[str](4)

c = call('C')
print(c.x)