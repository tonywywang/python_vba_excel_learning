from collections import *
import builtins
import re

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(ChainMap(adjustments, baseline)))
# A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. It is often much faster than creating a new dictionary and running multiple update() calls.
combined = baseline.copy()
combined.update(adjustments)
print(list(combined))

pylookup = ChainMap(locals(), globals(), vars(builtins))
print(list(pylookup))
print(pylookup['__name__'])  #__main__

c = ChainMap()
print(c)              # ChainMap({})
d = c.new_child()
print(d)              # ChainMap({}, {})
e = c.new_child()
print(e)              # ChainMap({}, {})
f = d.new_child()
print(f)              # ChainMap({}, {}, {})
print(e.maps[0])      # {}
d['x'] = 1
d['y'] = 2            # ChainMap only write or update the first mapping in the chain
print(d)              # ChainMap({'x': 1, 'y': 2}, {})
print(f)              # ChainMap({}, {'x': 1}, {})

d = ChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
d['lion'] = 'orange'
print(d)
# ChainMap({'zebra': 'black', 'lion': 'orange'}, {'elephant': 'blue'}, {'lion': 'yellow'})

class DeepChainMap(ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value
    
    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)
f = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
f['lion'] = 'orange'
f['snake'] = 'red'
del f['elephant']
print(f)
# DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)
print(sorted(cnt.elements()))
print(cnt.values())
# Counter({'blue': 3, 'red': 2, 'green': 1})
# ['blue', 'blue', 'blue', 'green', 'red', 'red']
# dict_values([2, 3, 1])

words = re.findall(r'\w+', open('IPQ40xx-sflash-devreg.patch').read().lower())
Counter(words).most_common(10)
'''
[('security', 104),
 ('0', 95),
 ('define', 91),
 ('p_ctx', 75),
 ('if', 62),
 ('inc', 62),
 ('flash', 61),
 ('ubnt', 52),
 ('return', 51),
 ('target', 46)]
'''
Counter(words).most_common()[:-5-1:-1]   # 5 least common words
# [('mt7623', 1), ('std', 1), ('namespace', 1), ('using', 1), ('378d81b', 1)]
