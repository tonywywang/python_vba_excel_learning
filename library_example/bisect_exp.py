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