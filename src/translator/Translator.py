from constants import *

class Translator:
    def __init__(self, coords, curDirection):
        self.directions = [0, 1, 2, 3, 4, 5] # N E S W U D
        self.coords = coords
        self.curDirection = curDirection
        # auxDirection helps in determining rotation direction
        # if curDirection is up/down
        self.auxDirection = curDirection
        self.directionToCoordMap = {
            NORTH: 1,
            SOUTH: 1,
            EAST: 0,
            WEST: 0,
            UP: 2,
            DOWN: 2
        }
