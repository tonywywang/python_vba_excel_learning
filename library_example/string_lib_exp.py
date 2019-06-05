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
