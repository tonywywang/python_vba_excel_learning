print(max([1,2,3,4]))   # 4
print(max((2,4,-2,9)))  # 9
print(max({1, 3, 5, -1})) # 5
print(max({'c':1, 'ab':2, 'ac':-3})) # c
print(max({'d':1, 'ab':2, 'dc':-3})) # dc

def string_len(str):
    return len(str)
print(max('my','name','dictionary', key=string_len))

x1 = [10, 20, 30]
x2 = [5, 15, 40, 25]

print(max(x1, x2, key=len))

ages = {'John': 21,
        'Mike': 52,
        'Sarah': 12,
        'Bob': 43
       }
print(max(zip(ages.values(), ages.keys())))