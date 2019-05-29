l1 = [1, 2, 3, 4]
for num in l1:
    print(num)
for num in reversed(l1):
    print(num)
for i in reversed(range(10)):
    print(i)

# reversed only can reverse iterator
def fib(num):
    a, b = 1, 1
    while num >= 0:
        yield a
        a, b = b, a + b
        num = num - 1
        
for num in reversed(fib(5)): # Error: 'generator' object is not reversible
    print(num) 