from levelup.dummy_gamemap import GameMap
from levelup.position import Position
class Character:
    DEFAULT_NAME = "Bob"
    name = ""
    startingPos = Position(1,1)
    currentPos = Position(1,1)
    
    def __init__(self, character_name = DEFAULT_NAME):
        self.name = character_name

    def getName(self):
        return self.name

    def enterMap(self, gamemap):
        self.gamemap = gamemap

    def move(self, direction):
        return self.startingPos

