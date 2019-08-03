from bisect import *

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    return i

l = [1, 4, 66, 79, 202, 394]
print(index(l, 0))  # return the index of the new value inserted

# This example uses bisect() to look up a letter grade for an exam score (say) based on a set of ordered numeric breakpoints: 90 and up is an ‘A’, 80 to 89 is a ‘B’, and so on/
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]

[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
# ['F', 'A', 'C', 'C', 'B', 'A', 'A']

data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])
keys = [r[1] for r in data]
data[bisect_left(keys, 0)] # ('black', 0)
data[bisect_left(keys, 1)] # ('blue', 1)
data[bisect_left(keys, 2)] # ('red', 5)
data[bisect_left(keys, 3)] # ('red', 5)
data[bisect_left(keys, 4)] # ('red', 5)
data[bisect_left(keys, 5)] # ('red', 5)
data[bisect_left(keys, 6)] # ('yellow', 8)
data[bisect_left(keys, 7)] # ('yellow', 8)
data[bisect_left(keys, 8)] # ('yellow', 8)