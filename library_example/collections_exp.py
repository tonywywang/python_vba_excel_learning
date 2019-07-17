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