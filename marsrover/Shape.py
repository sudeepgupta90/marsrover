from abc import ABC, abstractmethod
from marsrover.Point import Point

class Shape(ABC):

    @abstractmethod
    def check_point(self, p:Point)-> bool:
        """check if Point lies inside this shape"""

class Plateau(Shape):
    """rectangular plateau initialised with upper right coords"""
    def __init__(self, x, y):
        self.x= x
        self.y= y
    
    def check_point(self, p:Point)-> bool:
        flag_x, flag_y= False, False
        if p.x>=0 and p.x<=self.x:
            flag_x= True
        
        if p.y>=0 and p.y<=self.y:
            flag_y= True
        
        return (flag_x and flag_y)
    
    def __repr__ (self):
        return "Plateau({}, {})".format(self.x, self.y)
    