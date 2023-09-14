from constants import *
import unittest
from Translator import Translator

class TranslationTest(unittest.TestCase):
    def setUp(self):
        self.spacecraft = Translator([0, 0, 0], SOUTH)
    
    def test_forward(self):
        self.spacecraft.forward()
        self.assertEqual(self.spacecraft.coords, [0, -1, 0])
    
    def test_backward(self):
        self.spacecraft.backward()
        self.assertEqual(self.spacecraft.coords, [0, 1, 0])

class RotationTest(unittest.TestCase):
    def setUp(self):
        self.spacecraft = Translator([0, 0, 0], NORTH)
        self.spacecraft_up_down = Translator([0, 0, 0], NORTH)
    
    # UP / DOWN testing
    def test_up(self):
        self.spacecraft.up()
        self.assertEqual(self.spacecraft.curDirection, UP)
    def test_down(self):
        self.spacecraft.down()
        self.assertEqual(self.spacecraft.curDirection, DOWN)

    # LEFT and its subtypes Testing
    def test_left(self):
        self.spacecraft.left()
        self.assertEqual(self.spacecraft.curDirection, WEST)
    def test_left_after_up(self):
        self.spacecraft_up_down.up()
        self.spacecraft_up_down.left()
        self.assertEqual(self.spacecraft_up_down.curDirection, WEST)
    def test_left_after_down(self):
        self.spacecraft_up_down.down()
        self.spacecraft_up_down.left()
        self.assertEqual(self.spacecraft_up_down.curDirection, WEST)

    # RIGHT and its subtypes testing
    def test_right(self):
        self.spacecraft.right()
        self.assertEqual(self.spacecraft.curDirection, EAST)
    def test_right_after_up(self):
        self.spacecraft_up_down.up()
        self.spacecraft_up_down.right()
        self.assertEqual(self.spacecraft_up_down.curDirection, EAST)
    def test_right_after_down(self):
        self.spacecraft_up_down.down()
        self.spacecraft_up_down.right()
        self.assertEqual(self.spacecraft_up_down.curDirection, EAST)

if __name__ == '__main__':
    unittest.main()