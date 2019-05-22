def to_upper_case(s):
    return str(s).upper()

def print_iter(obj):
    for x in obj:
        print(x, end=' ')
    print("\n")
my_str = map(to_upper_case, 'abc')
print_iter(my_str)  # A B C
my_str = map(to_upper_case, ['a', 'b' ,'c'])
print_iter(my_str)  # A B C
my_str = map(to_upper_case, ['a', 'ab' ,'abc'])
print_iter(my_str)  # A AB ABC
my_list = map(lambda x: x**2, [1, 2, 3, 4])
print_iter(my_list)  # 1 4 9 16

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_list = list(map_iterator)
print(my_list) # [A, B, C]

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_set = set(map_iterator)
print(my_set) # {A, B, C}

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_tuple = tuple(map_iterator)
print(my_tuple) # (A, B, C)