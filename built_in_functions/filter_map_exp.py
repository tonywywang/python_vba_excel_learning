def isevennum(x):
    return not (x % 2)
def cube(x):
    return x*x*x
list(filter(isevennum, range(2, 10))) # [2, 4, 6, 8]
list(map(cube, range(2, 10))) # [8, 27, 64, 125, 216, 343, 512, 729]