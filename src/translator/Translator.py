from .constants import *

class Translator:
    def __init__(self, coords, curDirection):
        self.coords = coords
        self.curDirection = curDirection
        # auxDirection helps in determining rotation direction
        # if curDirection is up/down
        self.auxDirection = curDirection
        self.directionToCoordMap = {
            NORTH: [1, 'North'],
            SOUTH: [1, 'South'],
            EAST: [0, 'East'],
            WEST: [0, 'West'],
            UP: [2, 'Up'],
            DOWN:[2, 'Down'],
        }

    def getCurDirection(self):
        return self.directionToCoordMap[self.curDirection][1]
    
    def getCoordinates(self):
        return self.coords

    def forward(self):
        direction = self.directionToCoordMap[self.curDirection][0]
        if self.curDirection in [NORTH, EAST, UP]:
            self.coords[direction] += 1
        else:
            self.coords[direction] -= 1
        
    def backward(self):
        direction = self.directionToCoordMap[self.curDirection][0]
        if self.curDirection in [NORTH, EAST, UP]:
            self.coords[direction] -= 1
        else:
            self.coords[direction] += 1

    def left(self):
        def leftHelper(direction):
            if direction == NORTH:
                return WEST
            return direction - 1

        if self.curDirection in [UP, DOWN]:
            self.curDirection = leftHelper(self.auxDirection)
        else:
            self.curDirection = leftHelper(self.curDirection)

    def right(self):
        def rightHelper(direction):
            if direction == WEST:
                return NORTH
            return direction + 1

        if self.curDirection in [UP, DOWN]:
            self.curDirection = rightHelper(self.auxDirection)
        else:
            self.curDirection = rightHelper(self.curDirection)
    
    def up(self):
        self.auxDirection = self.curDirection
        self.curDirection = 4

    def down(self):
        self.auxDirection = self.curDirection
        self.curDirection = 5