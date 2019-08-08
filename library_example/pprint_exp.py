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

import json
import pprint
from urllib.request import urlopen

with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

pprint.pprint(project_info)
'''
{'author': 'The Python Packaging Authority',
 'author_email': 'pypa-dev@googlegroups.com',
 'bugtrack_url': None,
 'classifiers': ['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Software Development :: Build Tools'],
 'description': '# A sample Python project\n'
 ...
'''