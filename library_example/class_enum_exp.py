from enum import Enum

class Colour(Enum):
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    RED = 4

print(Colour.GREEN)
print(repr(Colour.GREEN))

for elem in Colour:
    print(repr(elem))

color = Colour.YELLOW   # if color is set to 3, color == Colour.YELLOW is false
if color == Colour.YELLOW:
    print(color)

'''
Colour.GREEN
<Colour.GREEN: 1>
<Colour.GREEN: 1>
<Colour.BLUE: 2>
<Colour.YELLOW: 3>
<Colour.RED: 4>
Colour.YELLOW
'''