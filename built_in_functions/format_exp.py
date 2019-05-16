print('{0}, {1}, {2}'.format('a', 'b', 'c'))   # a, b, c
print('{2}, {1}, {0}'.format('a', 'b', 'c'))   # c, b, a
print('{2}, {1}, {0}'.format(*'fed'))          # d, e, f
print('Coodinators: {latitude} {longitude}'.format(latitude='37.24N', longitude='-115.81W'))  # Coodinators: 37.24N -115.81W
coord = {'latitude':'37.24N', 'longitude':'-115.81W'}
print('Coodinators: {latitude} {longitude}'.format(**coord)) # Coodinators: 37.24N -115.81W
c = 3-5j
print("{0} has real {0.real} and imag {0.imag}".format(c)) # (3-5j) has real 3.0 and imag -5.0

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)
c = Point(3, 4)
print(c)   # Point(3, 4)

coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))

coord = [3, 5]
print('X: {0[0]};  Y: {0[1]}'.format(coord))