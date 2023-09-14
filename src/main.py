from translator.Translator import Translator
from translator.constants import *

class MainProgram:
    def __init__(self, coords, init_direction, commands):
        self.spacecraft = Translator(coords, init_direction)
        self.commands = commands
        self.commandToFuncMap = {
            'f': self.spacecraft.forward,
            'b': self.spacecraft.backward,
            'r': self.spacecraft.right,
            'l': self.spacecraft.left,
            'u': self.spacecraft.up,
            'd': self.spacecraft.down
        }

    def executeCommands(self):
        for command in self.commands:
            self.commandToFuncMap[command]()
        return f"{self.spacecraft.getCoordinates()} | {self.spacecraft.getCurDirection()}"

if __name__ == '__main__':
    commands = ['f', 'r', 'u', 'b', 'l']
    mp = MainProgram([0,0,0], NORTH, commands)
    print(mp.executeCommands())