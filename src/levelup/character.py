from levelup.dummy_gamemap import Gamemap
from levelup.position import Position
class Character:
    DEFAULT_NAME = "Bob"
    name = ""
    startingPos = Position(0,0)
    currentPos = Position(0,0)
    gamemap = Gamemap()

    def __init__(self, character_name = DEFAULT_NAME):
        self.name = character_name

    def getName(self):
        return self.name

    def setCurrentPosition(self, currentposition):
        self.currentPos = currentposition

    def enterMap(self, gamemap):
        self.gamemap = gamemap

    def move(self, direction):
        # get new position from map
        newposition = self.gamemap.calculatenewposition(self.currentPos, direction)
        # validate new position
        if not (self.gamemap.validateposition(newposition)):
            # invalid - return current position
            newposition = self.currentPos
        return newposition

    def getPosition(self):
        return self.currentPos