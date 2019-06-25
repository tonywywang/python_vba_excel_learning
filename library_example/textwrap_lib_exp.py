import textwrap

text1 = '''1. aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
2. bbbbbbbbbbbbbbbbbbbbbbbbb
3. ccccccccccccccccccccccccc
'''
print(textwrap.wrap(text1, width=10))
# ['1. aaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaa', 'aa 2. bbbb', 'bbbbbbbbbb', 'bbbbbbbbbb', 'b 3. ccccc', 'cccccccccc', 'cccccccccc']
print(textwrap.wrap(text1, width=70))
# ['1. aaaaaaaaaaaaaaaaaaaaaaaaaaaaa 2. bbbbbbbbbbbbbbbbbbbbbbbbb 3.', 'ccccccccccccccccccccccccc']