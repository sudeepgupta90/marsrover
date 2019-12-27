from marsrover.Direction import Direction
from marsrover.Point import Point
from marsrover.Shape import Shape, Plateau
from abc import ABC, abstractmethod

class Control(ABC):

    @abstractmethod
    def change_direction(self, cmd:str, curr_direction: Direction):
        """returns new direction from current_direction"""
        
    @abstractmethod
    def move(self, direction: Direction, curr_pos: Point):
        """return new Coordinate"""


class RoverControl(Control):

    def __init__(self, terrain: Shape):
        self.terrain= terrain

    def change_direction(self, cmd:str, curr_direction: Direction):
        
        if cmd == "L":
            return curr_direction.turn_left()
        elif cmd == "R":
            return curr_direction.turn_right()
        else:
            raise ValueError("{} not implemented".format(cmd))
    
    def move(self, direction: Direction, curr_pos: Point):
        
        dir_vector= direction.getDirectionVector()
        new_pos= dir_vector + curr_pos
        
        if self.terrain.check_point(new_pos):
            return new_pos
        else:
            raise ValueError("Third Law of Robotics: I can't harm myself. {} is not on the terrain".format(new_pos.__repr__()))
