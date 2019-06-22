import difflib

s1 =  [1, 2, 3, 5, 6, 4]
s2 =  [2, 3, 5, 4, 6, 1]
matched = difflib.SequenceMatcher(None, s1, s2)
print(matched.find_longest_match(0, 6, 0, 6))  # the longest match in S1 starts at index 1, in S2 starts at index 0 length 3 [2, 3, 5]

s1 = ' abcd'
s2 = 'abcd abcd'
matcher = difflib.SequenceMatcher(None, s1, s2)
print(matcher.find_longest_match(0, 5, 0, 9))  # Match(a=0, b=4, size=5)

s1 = ' abcd'
s2 = 'abcd abcd'
matcher = difflib.SequenceMatcher(lambda x:x in ' ', s1, s2)
print(matcher.find_longest_match(0, 5, 0, 9))  # Match(a=1, b=0, size=4)

f = lambda x:x in ' '
f('')   # True
f(' ')  # True
f('1')  # False

s1 = ' abcd 123 321'
s2 = 'abcd abcd 123321'
print('s1 = ', s1)
print('s2 = ', s2)
print('s1 == s2', s1 == s2)
print('')
matcher = difflib.SequenceMatcher(None, s1, s2)
for i in matcher.get_grouped_opcodes(1):
    print(i)
    print(':')
print(matcher)
print('ratio():', matcher.ratio())
print('quick_ratio():', matcher.quick_ratio())
print('real_quick_ratio():', matcher.real_quick_ratio())
'''
s1 =   abcd 123 321
s2 =  abcd abcd 123321
s1 == s2 False

[('delete', 0, 1, 0, 0), ('equal', 1, 2, 0, 1)]
:
[('equal', 4, 5, 3, 4), ('replace', 5, 6, 4, 10), ('equal', 6, 7, 10, 11)]
:
[('equal', 8, 9, 12, 13), ('delete', 9, 10, 13, 13), ('equal', 10, 11, 13, 14)]
:
<difflib.SequenceMatcher object at 0x000001C3B1DFE780>
ratio(): 0.6896551724137931
quick_ratio(): 0.6896551724137931
real_quick_ratio(): 0.896551724137931
'''