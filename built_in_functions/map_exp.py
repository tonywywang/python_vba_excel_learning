def to_upper_case(s):
    return str(s).upper()

def print_iter(obj):
    for x in obj:
        print(x, end=' ')
    print("\n")
my_str = map(to_upper_case, 'abc')
print_iter(my_str)
my_str = map(to_upper_case, ['a', 'b' ,'c'])
print_iter(my_str)
my_str = map(to_upper_case, ['a', 'ab' ,'abc'])
print_iter(my_str)