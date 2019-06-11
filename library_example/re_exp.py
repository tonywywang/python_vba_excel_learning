import re

g = re.search('.', 'abcdef') # '.' (Dot.) In the default mode, this matches any character except a newline. Result 'a'
g = re.search('.', '\n')     # newline symbol, '.' (Dot.) can not match
g = re.search('.', '\n', flags=re.DOTALL)  # with flag DOTALL, '.' (Dot.) can match newline symbol

g = re.search('^B', 'A: line1\nB: line2\nC: line3')         # no match
g = re.search('^B', 'A: line1\nB: line2\nC: line3', flags=re.MULTILINE) # match line 2 start 'B'
g.group(0)  