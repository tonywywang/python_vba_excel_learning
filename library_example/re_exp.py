import re

g = re.search('.', 'abcdef') # '.' (Dot.) In the default mode, this matches any character except a newline. Result 'a'
g = re.search('.', '\n')     # newline symbol, '.' (Dot.) can not match
g = re.search('.', '\n', flags=re.DOTALL)  # with flag DOTALL, '.' (Dot.) can match newline symbol

g = re.search('^B', 'A: line1\nB: line2\nC: line3')         # no match
g = re.search('^B', 'A: line1\nB: line2\nC: line3', flags=re.MULTILINE) # match line 2 start 'B'
g.group(0)  
 
g = re.search('2$', 'A: line1\nB: line2\nC: line3')         # no match
g = re.search('2$', 'A: line1\nB: line2\nC: line3', flags=re.MULTILINE) # match line 2 end with '2'
g.group(0)

rule = re.compile('a*')         # repetition of a, 'a', 'aa', 'aaa', 'aa...' matches
g = rule.match('abb a ab')
g.group(0)  # a

rule = re.compile('ab*')         # repetition of b, 'a', ab', 'abb', 'abbb', 'abbb...' matches
g = rule.match('abc a ab')
g.group(0)  # ab

rule = re.compile('ab*')         # repetition of a, 'a', 'aa', 'aaa', 'aa...' matches
g = rule.match('cdeab')
#g.group(0)  # no match None

rule = re.compile('ab*')         # * means repetion 0 or more of 'b' so match 'a'
g = rule.match('abc a ab')
g.group(0)   # a

rule = re.compile('ab+')
g = rule.match('abc a ab')       # * means repetion 1 or more of 'b' so match 'ab'
g.group(0)   # ab

rule = re.compile('ab?')
g = rule.match('c abc ab')       # Search the string from the start
g                                # None
g = rule.search('c a ab')        # Search the whole string
g.group(0)                       # 'a' , the ab? match 'a', 'ab' ? 0 or 1
g = rule.search('abc a ab')
g.group(0)                       # 'ab' substring of 'abc'

rule = re.compile('<.*>')
g = rule.search('<a> b <c>')
g.group(0)                     # '<a> b <c>'  greedy
rule = re.compile('<.*?>')
g = rule.search('<a> b <c>')
g.group(0)                     # '<a>'    non-greedy
