x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
# list(zipped)  # [(1, 4), (2, 5), (3, 6)]  however after this zipped can not be unpacked

x2, y2 = zip(*zipped)
print(x2)
print(y2)