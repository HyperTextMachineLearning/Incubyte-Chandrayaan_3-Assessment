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

if __name__ == '__main__':
    unittest.main()