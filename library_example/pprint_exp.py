import pprint

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
pp = pprint.PrettyPrinter(width=1)
pp.pprint(stuff)
# ['spam',
#  'eggs',
#  'lumberjack',
#  'knights',
#  'ni']

pp = pprint.PrettyPrinter(width=1, indent=4)
pp.pprint(stuff)
# [   'spam',
#     'eggs',
#     'lumberjack',
#     'knights',
#     'ni']