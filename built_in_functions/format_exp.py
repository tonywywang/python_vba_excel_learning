print('{0}, {1}, {2}'.format('a', 'b', 'c'))   # a, b, c
print('{2}, {1}, {0}'.format('a', 'b', 'c'))   # c, b, a
print('{2}, {1}, {0}'.format(*'fed'))          # d, e, f
print('Coodinators: {latitude} {longitude}'.format(latitude='37.24N', longitude='-115.81W'))  # Coodinators: 37.24N -115.81W
coord = {'latitude':'37.24N', 'longitude':'-115.81W'}
print('Coodinators: {latitude} {longitude}'.format(**coord)) # Coodinators: 37.24N -115.81W