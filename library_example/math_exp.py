from math import *
​
print(ceil(3.000001))
# 4
print(fabs(-3.000001))
# 3.000001 absolute value
print(copysign(-3.0, -0.0))
print(copysign(-3.0, 0.0))
# -3.0  copysign(x, y) return x absolute value and with sign y
# 3.0
print(floor(3.00001))
3

print(fmod(10.4, 3))
# 1.4000000000000004
print(frexp(2.3)) # return (m,  e) val = m*2**e
# (0.575, 2)