import string

string.digits             # '0123456789'
string.ascii_letters      # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase    # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase    # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.hexdigits          # '0123456789abcdefABCDEF'
string.octdigits          # '01234567'
string.punctuation        # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.printable          # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
string.whitespace         # ' \t\n\r\x0b\x0c'

'{0}, {1}, {2}'.format('a', 'b', 'c')  # 'a, b, c'
'{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only 'a, b, c'
'{2}, {1}, {0}'.format('a', 'b', 'c')  # 'c, b, a'
'{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence 'c, b, a'
'{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated 'abracadabra'

'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W') #'Coordinates: 37.24N, -115.81W'
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord)      #'Coordinates: 37.24N, -115.81W'

'{:+f}; {:+f}'.format(3.14, -3.14)  # show it always #'+3.140000; -3.140000'
'{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers #' 3.140000; -3.140000'
'{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}' #'3.140000; -3.140000'

# format also supports binary numbers
"int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42) #'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
# with 0x, 0o, or 0b as prefix:
"int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42) #'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

'{:,}'.format(1234567890)   # Using the comma as a thousands separator: '1,234,567,890'

fenzi = 19
fenmu = 21
'{:.2%}'.format(fenzi/fenmu)  # float format