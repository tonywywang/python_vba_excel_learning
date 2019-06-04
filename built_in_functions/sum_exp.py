listnum = [1, 2, 3, 4, 5]
sum(listnum)     #15
tuplenum = (6, 7, 8, 9, 10)
sum(tuplenum)    #40
dictnum = {'a':1, 'b':2, 'c':2}
sum(dictnum.values()) # 5
dictnum = {'a':1, 'b':2, 'b':2}
sum(dictnum.values())  # 3

def fib(num):
	a, b = 1, 1
	while (num >= 1):
		yield a
		num = num - 1
		a, b = b, a+b

for i in fib(6):
    print(i)  # 1 1 2 3 5 8
      
sum(fib(6))   # 20

n = fib(6)
print(next(n))   # 1
print(next(n))   # 1
print(next(n))   # 2
print(next(n))   # 3
print(next(n))   # 5
print(next(n))   # 8
print(next(n))   # Error: StopIteration