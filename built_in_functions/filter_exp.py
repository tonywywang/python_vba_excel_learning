def isevennum(x):
    return not (x % 2)
list(filter(isevennum, range(2, 20)))