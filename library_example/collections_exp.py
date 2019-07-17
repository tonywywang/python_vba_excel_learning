from collections import *
import builtins
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
print(d)              # ChainMap({'x': 1}, {})
print(f)              # ChainMap({}, {'x': 1}, {})