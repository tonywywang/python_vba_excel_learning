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