'''Imagine you are creating a Super Mario game. You need to 
define a class to represent Mario. What would it look like? 
If you aren't familiar with SuperMario, 
use your own favorite video or board game
to model a player'''

class Coins():
    def __init__(self,image,color,shape,radius,angle):
        self.image = image
        self.color = color
        self.shape = shape
        self.radius = radius
        self.angle = angle
        
white_coins = Coins("img", "white", "circle", 2 ,360)
print(white_coins.color)
print(white_coins.radius)