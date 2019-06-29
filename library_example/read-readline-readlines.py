with open("test.txt") as f:
    line = f.read()
    print(type(line))
    print(line)
'''
<class 'str'>
eee
ccc
'''

with open("test.txt") as f:
    line = f.readline()
    print(type(line))
    while line:
        print(line)
        line = f.readline()
'''
<class 'str'>
eee

ccc
'''

with open("test.txt") as f:
    line = f.readlines()
    print(type(line))
    print(line)
'''
<class 'list'>
['eee\n', 'ccc']
'''