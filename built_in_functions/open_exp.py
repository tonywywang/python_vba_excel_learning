with open("test.txt", 'r') as f:  # read mode
    print(f.read())
with open("test.txt", 'a') as f:  # append mode
    f.write('\n')
    f.write('ddd')
with open("test.txt", 'w') as f:  # flush the file and add new content
    f.write('eee')