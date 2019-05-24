print(min([1,2,3,4]))   # 4
print(min((2,4,-2,9)))  # 9
print(min({1, 3, 5, -1})) # 5
print(min({'c':1, 'ab':2, 'ac':-3})) # c
print(min({'d':1, 'ab':2, 'dc':-3})) # dc
d1 = {'d':1, 'ab':2, 'dc':-3}
print(min(zip(d1.values(), d1.keys())))

def string_len(str):
    return len(str)
print(min('my','name','dictionary', key=string_len))


x1 = [10, 20, 30]
x2 = [5, 15, 40, 25]

print(min(x1, x2, key=len))

ages = {'John': 21,
        'Mike': 52,
        'Sarah': 12,
        'Bob': 43
       }
print(min(zip(ages.values(), ages.keys())))