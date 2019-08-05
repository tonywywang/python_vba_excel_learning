a1 = [1, 2, 3, 4, [100, 1000]]
a2 = a1.copy()
a3 = deepcopy(a1)
a1.append(9)
a2[3] = 100
a2[4][0] = 0
a2.append(6)
a3[3] = 55
a3[4][0] = 10000
a3.append(7)
print(a1)
print(id(a1))
print(a2)
print(id(a2))
print(a3)
print(id(a3))
#[1, 2, 3, 4, [0, 1000], 9]
#2025441023048
#[1, 2, 3, 100, [0, 1000], 6]
#2025441865032
#[1, 2, 3, 55, [10000, 1000], 7]
#2025441044296
# a good illustration for shallow/deep copy
# https://www.python-course.eu/python3_deep_copy.php