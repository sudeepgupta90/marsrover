import unittest

from marsrover.Direction import East, West, North, South
from marsrover.Point import Point
from marsrover.Shape import Plateau
from marsrover.Control import RoverControl

class SimpleRoverTest(unittest.TestCase):
    
    def test_checkDirection(self):
        direction= East()
        new_direction= direction.turn_left()

        self.assertIsInstance(new_direction, North)


    def test_checkPointInShape(self):
        p= Plateau(5,5)

        self.assertTrue(p.check_point(Point(2,2)))

    def test_checkPointNotInShape(self):
        p= Plateau(5,5)

        self.assertFalse(p.check_point(Point(6, 6)))

if __name__ == "__main__":
    unittest.main()
