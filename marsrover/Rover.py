from marsrover.Control import RoverControl
from marsrover.Point import Point
from marsrover.Direction import initialise_direction
from marsrover.Control import RoverControl
from marsrover.Shape import Shape

class Rover:
    
    def __init__(self, terrain:Shape, startPoint:tuple= (0, 0), startDirection:str= "N"):
        self.position= Point(*startPoint)
        self.direction= initialise_direction(startDirection)
        self.Controls= RoverControl(terrain= terrain) # Plateau object is passed directly from outside
    
    def interpret_command(self, cmd:str):
        if cmd == "M":
            self.position= self.Controls.move(self.direction, self.position)
        elif cmd in ("L", "R"):
            self.direction= self.Controls.change_direction(cmd, self.direction)
        else:
            raise ValueError("Houston: I am not programmed to follow this command: {}".format(cmd))
    
    def __repr__(self):

        message= """my_pos:{}""".format(self.position.__repr__())
        
        return message

