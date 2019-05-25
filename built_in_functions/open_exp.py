with open("test.txt", 'r') as f:  # read mode
    print(f.read())
with open("test.txt", 'a') as f:  # append mode
    f.write('\n')
    f.write('ddd')
with open("test.txt", 'w') as f:  # flush the file and add new content
    f.write('eee')
    f.write('\n')
    f.write('ccc')
with open("test.txt", 'rb') as f:  # read mode
    print(f.read())         # b'eee\r\nccc'
with open("test.txt", 'r') as f:  # read by line
    for line in f:
        print(line)