class Point:
    
    def __init__(self, x, y):
        self.x= x
        self.y= y
    
    def __add__(self, p):
        if isinstance(p, Point):
            return Point(self.x+ p.x, self.y+ p.y)
    
    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)
    
