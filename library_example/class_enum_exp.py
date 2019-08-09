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

class Mood(Enum):
    HAPPY = 1
    ANGRY = 2
    
    def describe(self):
        return self.name, self.value
    def __str__(self):
        return 'my custom str! {0}'.format(self.value)
    @classmethod
    def favorite_mood(cls):
        # cls here is the enumeration
        return cls.HAPPY

print(Mood.favorite_mood())
print(Mood.HAPPY.describe())
str(Mood.ANGRY)
'''
my custom str! 1
('HAPPY', 1)
'my custom str! 2'
'''