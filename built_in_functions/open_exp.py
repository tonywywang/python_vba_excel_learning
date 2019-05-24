with open("test.txt", 'r') as f:  # read mode
    print(f.read())
with open("test.txt", 'a') as f:  # append mode 'w' only will clear the original content
    f.write('\n')
    f.write('ddd')