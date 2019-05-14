#compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')
exec(codeObejct)

codeInString = '100+1000'
codeObejct = compile(codeInString, 'single expression', 'eval')
print(eval(codeObejct))

codeInString = 'if 1:\n\tprint(1)\nelse:\n\tprint(0)'
codeObejct = compile(codeInString, 'if-else single expression', 'single')
exec(codeObejct)