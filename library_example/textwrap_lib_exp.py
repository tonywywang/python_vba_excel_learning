import textwrap

text1 = '''1. aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
2. bbbbbbbbbbbbbbbbbbbbbbbbb
3. ccccccccccccccccccccccccc
'''
print(textwrap.wrap(text1, width=10))
# ['1. aaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaa', 'aa 2. bbbb', 'bbbbbbbbbb', 'bbbbbbbbbb', 'b 3. ccccc', 'cccccccccc', 'cccccccccc']
print(textwrap.wrap(text1, width=70))
# ['1. aaaaaaaaaaaaaaaaaaaaaaaaaaaaa 2. bbbbbbbbbbbbbbbbbbbbbbbbb 3.', 'ccccccccccccccccccccccccc

print(textwrap.fill(text1, width=10))
'''
1. aaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aa 2. bbbb
bbbbbbbbbb
bbbbbbbbbb
b 3. ccccc
cccccccccc
cccccccccc
'''
# fill function works same as "\n".join(wrap(text, ...))

textwrap.shorten("Hello  world!", width=12)
# 'Hello world!'
textwrap.shorten("Hello  world!", width=11)
# 'Hello [...]'
textwrap.shorten("Hello world", width=10, placeholder="...")
# 'Hello...'

s = '''
    hello
      world
    '''
print(s)
print(textwrap.dedent(s)) # This can be used to make triple-quoted strings 
                          # line up with the left edge of the display, 
                          # while still presenting them in the source code in indented form.
'''

    hello
      world
    

hello
  world

'''

s = "hello\n\n \nworld"
print(s)
print(textwrap.indent(s, "+ ", lambda line: True))
'''
hello

 
world
+ hello
+ 
+  
+ world
'''
wrapper1 = textwrap.TextWrapper()
wrapper1.initial_indent = "<>"
wrapper1.width =5
s = "hello\nworld\n"
print(wrapper1.wrap(s))
#['<>hel', 'lo', 'world'] every line is at most width 5
print(wrapper1.fill(s))
'''
<>hel
lo
world
'''