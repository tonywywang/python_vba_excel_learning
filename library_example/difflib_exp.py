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