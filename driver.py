from marsrover.Rover import Rover
from marsrover.Shape import Plateau


def parseStartPoint(text:str):
    coords= list(map(int, text.strip().split(" ")[:-1]))
    direction= text.split(" ")[-1].strip("\n")

    return coords, direction

input_file= "sampleinput.txt"
text= None
with open("sampleinput.txt", "r") as f:
    text= f.readlines()

input_plateau= list(map(int, text[0].split(" ")))
plateau= Plateau(*input_plateau)

i=1
while i<len(text):
    startPoint, start_direction= parseStartPoint(text[i])
    cmds= list(text[i+1].strip("\n"))

    rover= Rover(plateau, startPoint, start_direction)

    for cmd in cmds:
        rover.interpret_command(cmd)
    print (rover.position.x, rover.position.y, rover.direction.getDirectionName()[0])
    i+=2