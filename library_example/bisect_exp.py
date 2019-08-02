from bisect import *

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    return i

l = [1, 4, 66, 79, 202, 394]
print(index(l, 0))  # return the index of the new value inserted