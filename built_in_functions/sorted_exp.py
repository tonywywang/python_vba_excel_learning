strlist = ['s', 'q', 'I', 'g', 'w', 'Z', 't']
print(sorted(strlist))                                    # ['I', 'Z', 'g', 'q', 's', 't', 'w']
print(sorted(strlist, key = str.lower))                   # ['g', 'I', 'q', 's', 't', 'w', 'Z']
print(sorted(strlist, key = str.lower, reverse = True))   # ['Z', 'w', 't', 's', 'q', 'I', 'g']

strlist = ['s', 'q', '.', 'I', 'g', '(', '我', 'w', 'Z', 't', ' ', ',']  # [' ', '(', ',', '.', 'I', 'Z', 'g', 'q', 's', 't', 'w', '我']
sorted(strlist)