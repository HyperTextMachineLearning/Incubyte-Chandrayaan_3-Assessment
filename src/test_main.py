import unittest
from translator.constants import *
from main import MainProgram

commands = ['f', 'r', 'u', 'b', 'l']
class MainTest(unittest.TestCase):
    def setUp(self):
        global commands
        self.scraft = MainProgram([0,0,0], NORTH, commands)
    
    def test_movement(self):
        result = self.scraft.executeCommands()
        self.assertEqual(result, '[0, 1, -1] | North')