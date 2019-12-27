from abc import ABC, abstractmethod
from marsrover.Point import Point

class Direction(ABC):

    direction_vector= Point(0, 0)
    
    #return direction
    @abstractmethod
    def turn_left(self):
        pass
    
    #return direction
    @abstractmethod
    def turn_right(self):
        pass
    
    def getDirectionVector(self):
        return self.direction_vector
    
    def getDirectionName(self):
        return self.__class__.__name__


class North(Direction):

    direction_vector= Point(0, 1)

    def turn_left(self):
        return West()
    
    def turn_right(self):
        return East()

class South(Direction):

    direction_vector= Point(0, -1)

    def turn_left(self):
        return East()
    
    def turn_right(self):
        return West()

class East(Direction):

    direction_vector= Point(1, 0)

    def turn_left(self):
        return North()
    
    def turn_right(self):
        return South()

class West(Direction):

    direction_vector= Point(-1, 0)

    def turn_left(self):
        return South()
    
    def turn_right(self):
        return North()

def initialise_direction(cmd:str) -> Direction:
    if cmd in list("NSEW"):
        if cmd == "N":
            return North()
        elif cmd == "S":
            return South()
        elif cmd == "E":
            return East()
        else:
            return West()
    else:
        raise ValueError("Houston, you idiot! {} needs to be a proper direction- NSEW".format(cmd))