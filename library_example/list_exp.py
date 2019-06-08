l1 = [1, 2, 3, 4]
#del l1[1:3]
l1[1:3] = [5, 5]   # slice need to be assigned with iterable obj [1, 5, 5, 4]
del l1[1:3]        # [1, 4]
l2 = [1, 2, 3, 4, 6, 7, 8, 9]
l2[1:5:2]  # [2, 4]        1: start 5: end 2: interval
l2[1:5:1]  # [2, 3, 4, 6]  1: start 5: end 1: interval