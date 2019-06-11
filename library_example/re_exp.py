import re

g = re.search('.', 'abcdef') # '.' (Dot.) In the default mode, this matches any character except a newline. Result 'a'
g = re.search('.', '\n')     # newline symbol, '.' (Dot.) can not match
g = re.search('.', '\n', flags=re.DOTALL)  # with flag DOTALL, '.' (Dot.) can match newline symbol